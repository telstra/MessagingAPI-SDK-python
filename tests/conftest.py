"""Global fixtures."""

import os


def pytest_configure():
    """Set the required credentials."""
    os.environ["CLIENT_ID"] = "client 1"
    os.environ["CLIENT_SECRET"] = "secret 1"
