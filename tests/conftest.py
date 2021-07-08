"""Global fixtures."""

import os


def pytest_configure():
    """Set the required credentials."""
    os.environ["TELSTRA_CLIENT_ID"] = "key 1"
    os.environ["TELSTRA_CLIENT_SECRET"] = "secret 1"
