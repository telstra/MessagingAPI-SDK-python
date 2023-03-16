# Standard library imports...
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import socket
from threading import Thread

# Third-party imports...
import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):
    USERS_PATTERN = re.compile(r"/users")
    AUTH_PATTERN = re.compile(r"/v2/oauth/token")
    TRIAL_NUMBERS_PATTERN = re.compile(r"/v3/free-trial-numbers")
    VIRTUAL_NUMBERS_PATTERN = re.compile(r"/v3/virtual-numbers")

    def do_GET(self):
        if re.search(self.USERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(requests.codes.ok)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps([])
            self.wfile.write(response_content.encode("utf-8"))
            return

    def do_POST(self):
        if re.search(self.TRIAL_NUMBERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(requests.codes.ok)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps({"freeTrialNumbers": ["+61412345678"]})
            self.wfile.write(response_content.encode("utf-8"))
            return

        if re.search(self.AUTH_PATTERN, self.path):
            # Add response status code.
            self.send_response(requests.codes.ok)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                    "access_token": "MwL1jqyWlk9w1HdAUTMAwDNZOJBL",
                    "token_type": "Bearer",
                    "expires_in": "3599",
                }
            )
            self.wfile.write(response_content.encode("utf-8"))
            return

        if re.search(self.VIRTUAL_NUMBERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(requests.codes.ok)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                    "virtualNumber": "0400000001",
                    "replyCallbackUrl": "https://example.com",
                    "tags": ["V3"],
                    "lastUse": "",
                }
            )
            self.wfile.write(response_content.encode("utf-8"))
            return


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    address, port = s.getsockname()
    s.close()
    return port


def start_mock_server(port):
    mock_server = HTTPServer(("localhost", port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()
