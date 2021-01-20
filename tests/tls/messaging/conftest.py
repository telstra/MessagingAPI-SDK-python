"""Messaging API fixtures."""
# pylint: disable=unused-argument,redefined-outer-name

import os
import typing
from unittest import mock
from urllib import error, request

import pytest

from tls.messaging import exceptions, oauth, subscription
from tls.messaging.utils import config


@pytest.fixture
def _valid_credentials(monkeypatch):
    """Valid client id and secret."""
    tls_client_key = os.getenv("VALID_TLS_CLIENT_KEY")
    tls_client_secret = os.getenv("VALID_TLS_CLIENT_SECRET")
    mock_config = config.Config(
        tls_client_key=tls_client_key, tls_client_secret=tls_client_secret
    )
    mock_get = mock.MagicMock()
    mock_get.return_value = mock_config
    monkeypatch.setattr(config, "get", mock_get)

    yield

    try:
        subscription.delete()
    except exceptions.SubscriptionError:
        pass


@pytest.fixture
def mocked_auth_get_token(monkeypatch):
    """Mock oauth.get_token."""
    mock_get_token = mock.MagicMock()
    mock_token = mock.MagicMock()
    mock_token.authorization = "authorization 1"
    mock_get_token.return_value = mock_token
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

    yield mock_token


@pytest.fixture
def _mocked_oauth_get_token(mocked_auth_get_token):
    """Wrapper for mocked_get_token to avoid unused argument linting errors."""


@pytest.fixture
def mocked_oauth_get_token_error(monkeypatch):
    """Mock oauth.get_token to raise an error."""
    mock_get_token = mock.MagicMock()
    message = "message 1"
    mock_get_token.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

    yield message


class UrlopenError(typing.NamedTuple):
    """Information for the mocked urlopen error."""

    code: int
    message: str


@pytest.fixture
def mocked_request_urlopen_error(monkeypatch):
    """Mock request.urlopen to raise an error."""
    code = 401
    message = "msg 1"
    mock_urlopen = mock.MagicMock()
    mock_urlopen.side_effect = error.HTTPError(
        url="url 1", code=code, msg=message, hdrs={}, fp=mock.MagicMock()
    )
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    yield UrlopenError(code=code, message=message)
