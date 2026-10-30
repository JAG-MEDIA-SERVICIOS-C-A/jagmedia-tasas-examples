"""Receptor de webhooks JAG-Media — verifica firma HMAC-SHA256.

Corre:   python receptor.py          (escucha en :8080)
Registra: POST /v1/webhooks {"url":"https://tu-dominio.com/hook","events":["*"]}
         → responde {id, secret} — guarda el secret (una sola vez)
"""
import hashlib, hmac, json
from http.server import BaseHTTPRequestHandler, HTTPServer

SECRET = b"whsec_tu_secret"  # lo da POST /v1/webhooks al registrar

class Hook(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        sig = self.headers.get("X-Signature-256", "")
        esperada = "sha256=" + hmac.new(SECRET, body, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, esperada):
            self.send_response(401); self.end_headers()
            self.wfile.write(b'{"detail":"firma invalida"}')
            return
        ev = json.loads(body)
        print("evento:", ev.get("event"), "| data:", ev.get("data"))
        self.send_response(200); self.end_headers()
        self.wfile.write(b'{"received":true}')

HTTPServer(("0.0.0.0", 8080), Hook).serve_forever()
