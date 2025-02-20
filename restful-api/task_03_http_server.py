#!/usr/bin/python3
"""
This module provides a class that build a server
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Server(BaseHTTPRequestHandler):
    """
    This class provides function to handle request
    """

    def send_text(self, data, status=200):
        """
        This function send text
        """
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status=200):
        """
        This function send a json
        """
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """
        This function perform request
        """
        if self.path == "/data":
            self.send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self.send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
                })
        elif self.path == "/status":
            self.send_text("OK")
        elif self.path == "/":
            self.send_text("Hello, this is a simple API!")
        else:
            self.send_text("Endpoint not found", 404)


if __name__ == "__main__":
    server_adress = ("localhost", 8000)
    run_serv = HTTPServer(server_adress, Server)
    print(f"Server on http://{server_adress[0]}:{server_adress[1]}")
    run_serv.serve_forever()
