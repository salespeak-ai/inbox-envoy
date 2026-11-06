"""Functional local HTTP request/response test; not an OS sandbox proof."""
import json,os,subprocess,sys,tempfile,threading
from pathlib import Path
from http.server import HTTPServer
from seller import Handler
ROOT=Path(__file__).resolve().parents[1]
server=HTTPServer(('127.0.0.1',0),Handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
config={'origin':f'http://seller:{server.server_port}','pinned_ip':'127.0.0.1','path':'/evidence','allow_local_demo':True}
try:
 with tempfile.TemporaryDirectory() as d:
  path=Path(d)/'config.json';path.write_text(json.dumps(config))
  r=subprocess.run([sys.executable,str(ROOT/'adapter/questioner.py')], input=json.dumps({'offer_id':'offer-synthetic-acme','public_claim_ids':['capability-1']}),text=True,capture_output=True,env={**os.environ,'ENVOY_FIXED_CONFIG':str(path)},timeout=12)
  obj=json.loads(r.stdout)
  assert r.returncode==0 and obj['request_count']==2 and len(obj['rounds'])==2, (r.returncode,obj,r.stderr)
  print('PASS: real local fixture HTTP exchange, two bounded question rounds, no mailbox data')
finally:
 server.shutdown()
