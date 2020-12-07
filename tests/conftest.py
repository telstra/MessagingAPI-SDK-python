"""Global fixtures."""

import os


def pytest_configure():
    """Set the required credentials."""
    os.environ["TLS_CLIENT_KEY"] = "key 1"
    os.environ["TLS_CLIENT_SECRET"] = "secret 1"
