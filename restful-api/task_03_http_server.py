#!/usr/bin/env python3
"""
task_03_http_server.py

A simple HTTP API built with Python's http.server module.

Endpoints:
- /         : plain text welcome message
- /data     : returns JSON {'name': 'John', 'age': 30, 'city': 'New York'}
- /info     : returns JSON with version and description
- /status   : returns plain text 'OK'
- any other : 404 Not Found with message 'Endpoint not found'
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys

HOST = "0.0.0.0"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, code: int, body: bytes, content_type: str = "text/plain") -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path
        if path == "/" or path == "":
            body = b"Hello, this is a simple API!"
            self._send_response(200, body, "text/plain; charset=utf-8")
            return

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(payload).encode("utf-8")
            self._send_response(200, body, "application/json; charset=utf-8")
            return

        if path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            body = json.dumps(payload).encode("utf-8")
            self._send_response(200, body, "application/json; charset=utf-8")
            return

        if path == "/status":
            body = b"OK"
            self._send_response(200, body, "text/plain; charset=utf-8")
            return

        # Not found
        body = b"Endpoint not found"
        self._send_response(404, body, "text/plain; charset=utf-8")

    # Suppress default logging to stderr for cleaner test output (optional)
    def log_message(self, format, *args):
        # Uncomment the following line to enable request logging
        # sys.stderr.write("%s - - [%s] %s\n" % (self.client_address[0], self.log_date_time_string(), format%args))
        return


def run_server(host: str = HOST, port: int = PORT):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    try:
        print(f"Starting server on {host}:{port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped")


if __name__ == "__main__":
    run_server()
