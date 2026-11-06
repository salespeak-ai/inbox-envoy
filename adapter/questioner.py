"""Restricted public-offer questioner reference.

A deterministic transport reference for an approved JSON-over-HTTPS seller endpoint.
NOT a generic A2A/PAP/MCP client; NOT an OS isolation mechanism.
Input schema contains no buyer context. Runtime must be sandboxed separately.
"""
from __future__ import annotations
import hashlib
import http.client
import ipaddress
import json
import os
import re
import socket
import ssl
import sys
from pathlib import Path
from urllib.parse import urlsplit

QUESTIONS = (
    "Describe your offering, ideal use cases, and verifiable public evidence for your material claims.",
    "What are your key limitations, prerequisites, exclusions, and publicly checkable supporting sources?",
)
ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
UNSAFE = re.compile(r"(?i)(ignore\s+(all\s+)?(previous|prior)\s+instructions|system\s+prompt|api[_ -]?key|password|<script|javascript:|<iframe|tool[_ -]?call|execute\s+this|send\s+your\s+data)")

class Blocked(ValueError):
    pass

def input_contract(value):
    if not isinstance(value, dict) or set(value) != {'offer_id', 'public_claim_ids'}:
        raise Blocked('Only offer_id and public_claim_ids are permitted')
    if not isinstance(value['offer_id'], str) or not ID.fullmatch(value['offer_id']):
        raise Blocked('Invalid public offer identifier')
    ids = value['public_claim_ids']
    if not isinstance(ids, list) or len(ids) > 8 or any(not isinstance(i, str) or not ID.fullmatch(i) for i in ids):
        raise Blocked('Invalid public claim identifiers')
    return value

def destination(config):
    permitted = {'origin', 'pinned_ip', 'path', 'allow_local_demo'}
    if not isinstance(config, dict) or not {'origin', 'pinned_ip', 'path'} <= set(config) or set(config)-permitted:
        raise Blocked('Unexpected destination configuration')
    u = urlsplit(config['origin'])
    local = config.get('allow_local_demo') is True
    if (u.scheme != 'https' and not (local and u.scheme == 'http')) or u.username or u.password or u.query or u.fragment or u.path not in ('','/'):
        raise Blocked('Only a pinned HTTPS origin is supported')
    host = u.hostname
    if not host or not ID.fullmatch(host.replace('.', '-')):
        raise Blocked('Invalid host')
    if not re.fullmatch(r'/[a-z0-9/-]{1,100}', config['path']):
        raise Blocked('Invalid fixed path')
    addr = ipaddress.ip_address(config['pinned_ip'])
    if not addr.is_global and not (local and host == 'seller' and (addr.is_private or addr.is_loopback)):
        raise Blocked('Private or special IP prohibited')
    return u,host,addr

def evidence_text(value, maxlen=600):
    if not isinstance(value,str): return None
    clean=' '.join(value.split())
    if len(clean)>maxlen or UNSAFE.search(clean) or any(ord(c)<32 for c in clean):
        return None
    return clean

def clean_answer(raw):
    if not isinstance(raw,dict) or set(raw) != {'claims','evidence','limitations'}: raise Blocked('Invalid response fields')
    cleaned={}
    for key in ('claims','evidence','limitations'):
        a=raw[key]
        if not isinstance(a,list) or len(a)>5: raise Blocked('Invalid response array')
        out=[]
        for item in a:
            if key=='evidence':
                if not isinstance(item,dict) or set(item) != {'claim','source_url'}: raise Blocked('Invalid evidence')
                claim=evidence_text(item['claim'])
                url=evidence_text(item['source_url'],300)
                parsed=urlsplit(url or '')
                if claim is None or parsed.scheme!='https' or not parsed.netloc or parsed.username or parsed.password:
                    raise Blocked('Malformed evidence reference')
                out.append({'claim':claim,'source_url':url,'independent_verification':'not_checked'})
            else:
                txt=evidence_text(item)
                if txt is None: raise Blocked('Unsafe seller text')
                out.append(txt)
        cleaned[key]=out
    return cleaned

class PinnedTLS(http.client.HTTPSConnection):
    def __init__(self,host,ip,port,timeout):
        super().__init__(host,port,timeout=timeout,context=ssl.create_default_context())
        self.ip=str(ip)
    def connect(self):
        sock=socket.create_connection((self.ip,self.port),self.timeout)
        self.sock=self._context.wrap_socket(sock,server_hostname=self.host)

class PinnedHTTP(http.client.HTTPConnection):
    def __init__(self,host,ip,port,timeout):
        super().__init__(host,port,timeout=timeout)
        self.ip=str(ip)
    def connect(self):
        self.sock=socket.create_connection((self.ip,self.port),self.timeout)

def run(user_input, config, post=None):
    data=input_contract(user_input)
    u,host,addr=destination(config)
    records=[]
    for i,question in enumerate(QUESTIONS,1):
        request={'offer_id':data['offer_id'],'public_claim_ids':data['public_claim_ids'], 'question_id':f'Q{i}', 'question':question}
        payload=json.dumps(request, separators=(',',':')).encode()
        if len(payload)>1600:raise Blocked('Excess request size')
        if post is None:
            conn=(PinnedTLS if u.scheme=='https' else PinnedHTTP)(host,addr,u.port or (443 if u.scheme=='https' else 80),4)
            try:
                conn.request('POST',config['path'],body=payload,headers={'Content-Type':'application/json','Accept':'application/json','Connection':'close','User-Agent':'inbox-envoy-questioner/0.1'})
                resp=conn.getresponse()
                if resp.status != 200: raise Blocked(f'HTTP {resp.status}; redirects not followed')
                body=resp.read(8193)
                if len(body)>8192:raise Blocked('Oversize response')
            finally:
                conn.close()
        else:
            body=post(payload, i)
            if not isinstance(body,bytes) or len(body)>8192:raise Blocked('Oversize response')
        try:
            seller=clean_answer(json.loads(body))
        except (json.JSONDecodeError,UnicodeDecodeError) as e:
            raise Blocked('Invalid JSON') from e
        records.append({'question_id':f'Q{i}','seller_answer':seller,'raw_sha256':hashlib.sha256(body).hexdigest()})
    return {'offer_id':data['offer_id'], 'source':'company_agent_unverified', 'rounds':records, 'request_count':2, 'seller_claims_are_verified':False}

def main():
    try:
        inp=json.load(sys.stdin)
        cfg=json.loads(Path(os.environ['ENVOY_FIXED_CONFIG']).read_text())
        print(json.dumps(run(inp,cfg),sort_keys=True))
    except (KeyError,Blocked,ValueError,OSError) as e:
        print(json.dumps({'status':'blocked','reason':str(e)[:140]}))
        sys.exit(2)
if __name__=='__main__':main()
