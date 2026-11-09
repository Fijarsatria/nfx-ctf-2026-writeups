#!/usr/bin/env python3
"""Tiny HTTP capture server for ChangeTrack OOB webhook exfil."""
import http.server
import sys
import time

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 18080
OUT = sys.argv[2] if len(sys.argv) > 2 else "oob-capture.log"


class H(http.server.BaseHTTPRequestHandler):
    def _log(self, body=b""):
        with open(OUT, "ab") as f:
            f.write(b"\n===== " + time.strftime("%H:%M:%S").encode() + b" =====\n")
            f.write((self.command + " " + self.path + "\n").encode())
            for k, v in self.headers.items():
                f.write(f"{k}: {v}\n".encode())
            f.write(b"---- body ----\n")
            f.write(body + b"\n")
        print(self.command, self.path, body[:200], flush=True)

    def do_GET(self):
        self._log()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n)
        self._log(body)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *a):
        pass


http.server.HTTPServer(("0.0.0.0", PORT), H).serve_forever()
