"""Tests for bun."""

from unittest import mock
from urllib import error, request

import pytest

from messaging import bnum, exceptions, oauth


def test_register(_valid_credentials):
    """
    GIVEN
    WHEN register is called
    THEN phone numbers are registered.
    """
    phone_numbers = ["+61412345678"]

    returned_phone_numbers = bnum.register(phone_numbers=phone_numbers)

    assert returned_phone_numbers == phone_numbers


def test_register_error_oauth(monkeypatch):
    """
    GIVEN oauth get_token that raises an error
    WHEN register is called
    THEN BnumError is raised.
    """
    mock_oauth = mock.MagicMock()
    message = "message 1"
    mock_oauth.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_oauth)

    with pytest.raises(exceptions.BnumError) as exc:
        bnum.register(phone_numbers=[])

    assert message in str(exc.value)


def test_register_error_http(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN register is called
    THEN BnumError is raised.
    """
    mock_oauth = mock.MagicMock()
    mock_token = mock.MagicMock()
    mock_token.authorization = "authorization 1"
    mock_oauth.return_value = mock_token

    code = 401
    msg = "msg 1"
    mock_urlopen = mock.MagicMock()
    mock_urlopen.side_effect = error.HTTPError(
        url="url 1", code=code, msg=msg, hdrs={}, fp=mock.MagicMock()
    )
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    with pytest.raises(exceptions.BnumError) as exc:
        bnum.register(phone_numbers=[])

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)


@pytest.mark.xfail
def test_get(_valid_credentials):
    """
    GIVEN
    WHEN get is called
    THEN phone numbers are returned.
    """
    returned_phone_numbers = bnum.get()

    assert isinstance(returned_phone_numbers, list)


def test_get_error_oauth(monkeypatch):
    """
    GIVEN oauth get_token that raises an error
    WHEN get is called
    THEN BnumError is raised.
    """
    mock_oauth = mock.MagicMock()
    message = "message 1"
    mock_oauth.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_oauth)

    with pytest.raises(exceptions.BnumError) as exc:
        bnum.get()

    assert message in str(exc.value)


def test_get_error_http(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN get is called
    THEN BnumError is raised.
    """
    mock_oauth = mock.MagicMock()
    mock_token = mock.MagicMock()
    mock_token.authorization = "authorization 1"
    mock_oauth.return_value = mock_token

    code = 401
    msg = "msg 1"
    mock_urlopen = mock.MagicMock()
    mock_urlopen.side_effect = error.HTTPError(
        url="url 1", code=code, msg=msg, hdrs={}, fp=mock.MagicMock()
    )
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    with pytest.raises(exceptions.BnumError) as exc:
        bnum.get()

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)
