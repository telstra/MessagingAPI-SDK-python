"""Messaging API fixtures."""

import os
from unittest import mock

import pytest

from messaging.utils import environment
from messaging import subscription, exceptions


@pytest.fixture
def _valid_credentials(monkeypatch):
    """Valid client id and secret."""
    tls_client_key = os.getenv("VALID_TLS_CLIENT_KEY")
    tls_client_secret = os.getenv("VALID_TLS_CLIENT_SECRET")
    mock_environment = environment.TEnvironment(
        tls_client_key=tls_client_key, tls_client_secret=tls_client_secret
    )
    mock_get = mock.MagicMock()
    mock_get.return_value = mock_environment
    monkeypatch.setattr(environment, "get", mock_get)

    yield

    try:
        subscription.delete()
    except exceptions.SubscriptionError:
        pass
