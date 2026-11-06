"""Local-only, synthetic company fixture. No third-party network calls."""
import json
from http.server import BaseHTTPRequestHandler,HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path!='/evidence': self.send_error(404);return
        length=int(self.headers.get('Content-Length','0'))
        if length>1600: self.send_error(413);return
        try:
            data=json.loads(self.rfile.read(length))
            if data['question_id'] not in ('Q1','Q2'):raise ValueError()
            result={'claims':['Synthetic Acme provides test-only workflow monitoring.'],
                    'evidence':[{'claim':'Synthetic publicly documented feature','source_url':'https://example.com/docs'}],
                    'limitations':['Demo fixture: not evidence of a real product.']}
            payload=json.dumps(result).encode()
            self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)
        except (ValueError,KeyError):self.send_error(400)
    def log_message(self,*a):pass
if __name__=='__main__': HTTPServer(('0.0.0.0',8080),Handler).serve_forever()
