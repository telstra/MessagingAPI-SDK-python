"""Tests for sms."""

from unittest import mock
from urllib import error, request

import pytest

from messaging import sms, subscription, exceptions, oauth


VALID_SEND_KWARGS = {"to": "+61412345678", "body": "body 1"}


@pytest.mark.parametrize(
    "kwargs, expected_contents",
    [
        pytest.param(
            {**VALID_SEND_KWARGS, "to": None},
            ["to", "received", f'"{None}"', "string", "list", "string"],
            id="to not string and not list",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "to": "invalid"},
            ["to", "received", '"invalid"'],
            id="to invalid string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "to": ["invalid"]},
            ["to", "received", '"invalid"'],
            id="to invalid list single",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "to": ["invalid", "+61412345678"]},
            ["to", "received", '"invalid"'],
            id="to invalid list multiple first",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "to": ["+61412345678", "invalid"]},
            ["to", "received", '"invalid"'],
            id="to invalid list multiple second",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "body": None},
            ["body", "received", f'"{None}"', "expected", "string"],
            id="body not string",
        ),
    ],
)
def test_send_invalid_param(kwargs, expected_contents):
    """
    GIVEN invalid parameters
    WHEN send is called with the parameters
    THEN SmsError is raised with the expected contents.
    """
    with pytest.raises(exceptions.SmsError) as exc:
        sms.send(**kwargs)

    for content in expected_contents:
        assert content in str(exc)


def test_send(_valid_credentials):
    """
    GIVEN
    WHEN send is called with to as a string and then as a list
    THEN a sms is sent.
    """
    to = subscription.get().destination_address
    body = "body 1"

    returned_sms = sms.send(to=to, body=body)

    assert returned_sms.to == to
    assert returned_sms.delivery_status is not None
    assert returned_sms.message_id is not None
    assert returned_sms.message_status_url is not None

    returned_sms = sms.send(to=[to], body=body)

    assert returned_sms.to == to
    assert returned_sms.delivery_status is not None
    assert returned_sms.message_id is not None
    assert returned_sms.message_status_url is not None


def test_send_error_oauth(monkeypatch):
    """
    GIVEN oauth that raises an error
    WHEN send is called
    THEN SmsError is raised.
    """
    mock_oauth = mock.MagicMock()
    message = "message 1"
    mock_oauth.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_oauth)

    with pytest.raises(exceptions.SmsError) as exc:
        sms.send(to="0412345678", body="body 1")

    assert message in str(exc.value)


def test_send_error_http(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN send is called
    THEN SmsError is raised.
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

    with pytest.raises(exceptions.SmsError) as exc:
        sms.send(to="0412345678", body="body 1")

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)
