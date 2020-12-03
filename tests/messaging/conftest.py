"""Messaging API fixtures."""

import os
from unittest import mock

import pytest

from messaging.utils import environment


@pytest.fixture
def _valid_credentials(monkeypatch):
    """Valid client id and secret."""
    client_id = os.getenv("VALID_CLIENT_ID")
    client_secret = os.getenv("VALID_CLIENT_SECRET")
    mock_environment = environment.TEnvironment(
        client_id=client_id, client_secret=client_secret
    )
    mock_get = mock.MagicMock()
    mock_get.return_value = mock_environment
    monkeypatch.setattr(environment, "get", mock_get)
