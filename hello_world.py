import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "dev")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            body = "ok"
        elif self.path == "/version":
            body = VERSION
        else:
            body = f"Hello, World! version={VERSION}"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
