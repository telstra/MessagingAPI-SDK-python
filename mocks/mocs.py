"""Mock server."""

import json
import re
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class MockServerRequestHandler(BaseHTTPRequestHandler):
    """Request handler for mock server."""

    USERS_PATTERN = re.compile(r"/users")
    AUTH_PATTERN = re.compile(r"/v2/oauth/token")
    TRIAL_NUMBERS_PATTERN = re.compile(r"/v3/free-trial-numbers")
    VIRTUAL_NUMBERS_PATTERN = re.compile(r"/v3/virtual-numbers")
    REPORTS_PATTERN = re.compile(r"/v3/reports")

    def do_GET(self):
        """Make GET request."""

        if re.search(self.TRIAL_NUMBERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps({"freeTrialNumbers": ["+61412345678"]})
            self.wfile.write(response_content.encode("utf-8"))
            return

        if re.search(self.REPORTS_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                    "reports": [
                        {
                            "reportId": "6940c774-4335-4d2b-b758-4ecb19412e85",
                            "reportStatus": "completed",
                            "reportType": "messages",
                            "reportExpiry": "2023-01-01",
                        }
                    ]
                }
            )
            self.wfile.write(response_content.encode("utf-8"))
            return

    def do_POST(self):
        """Make a POST request."""

        if re.search(self.TRIAL_NUMBERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps({"freeTrialNumbers": ["+61412345678"]})
            self.wfile.write(response_content.encode("utf-8"))
            return

        if re.search(self.AUTH_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

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
            self.send_response(200)

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

        if re.search(self.REPORTS_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                    "reportId": "6940c774-4335-4d2b-b758-4ecb19412e85",
                    "reportCallbackUrl": "https://www.example.com",
                    "reportStatus": "queued",
                }
            )
            self.wfile.write(response_content.encode("utf-8"))
            return


def get_free_port():
    """Get free port."""

    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def start_mock_server(port):
    """Start mock servers."""

    mock_server = HTTPServer(("localhost", port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.daemon = True
    mock_server_thread.start()
