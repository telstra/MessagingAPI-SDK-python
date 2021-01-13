"""Tests for sms."""

import json
import typing
from unittest import mock
from urllib import error, request

import pytest

from telstra.messaging import exceptions, oauth, sms, subscription

VALID_SEND_KWARGS: typing.Dict[str, typing.Any] = {
    "to": "+61412345678",
    "body": "body 1",
}


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
        pytest.param(
            {**VALID_SEND_KWARGS, "from_": True},
            ["from_", "received", f'"{True}"', "expected", "string"],
            id="from_ not string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "from_": "0123456789ab"},
            [
                "from_",
                "received",
                '"0123456789ab"',
                "too many characters",
                "expected",
                "at most",
                "11",
                "characters",
            ],
            id="from_ too long",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "from_": "-"},
            ["from_", "received", '"-"', "contains", "invalid", "characters"],
            id="from_ not alpha numeric",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "from_": "0412345678"},
            ["from_", "received", '"0412345678"', "phone number"],
            id="from_ phone number",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "validity": "1"},
            ["validity", "received", '"1"', "integer"],
            id="validity string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "validity": True},
            ["validity", "received", f'"{True}"', "integer"],
            id="validity boolean",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "scheduled_delivery": "1"},
            ["scheduled_delivery", "received", '"1"', "integer"],
            id="scheduled_delivery string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "scheduled_delivery": True},
            ["scheduled_delivery", "received", f'"{True}"', "integer"],
            id="scheduled_delivery boolean",
        ),
    ],
)
@pytest.mark.sms
def test_send_invalid_param(kwargs, expected_contents):
    """
    GIVEN invalid parameters
    WHEN send is called with the parameters
    THEN SmsError is raised with the expected contents.
    """
    with pytest.raises(exceptions.SmsError) as exc_info:
        sms.send(**kwargs)

    for content in expected_contents:
        assert content in str(exc_info.value)


@pytest.mark.sms
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

    sms.send(to=to, body=body, from_="a")


SEND_PARAM_TESTS = [
    pytest.param("from_", "a1", "from", id="from_"),
    pytest.param("validity", 1, "validity", id="validity"),
    pytest.param("scheduled_delivery", 1, "scheduledDelivery", id="scheduled_delivery"),
]


@pytest.mark.parametrize("name, value, expected_name", SEND_PARAM_TESTS)
@pytest.mark.sms
def test_send_param(name, value, expected_name, monkeypatch):
    """
    GIVEN parameter name and value
    WHEN send is called with the parameter
    THEN a sms is sent with the expected parameter name.
    """
    to = "0412345678"
    body = "body 1"

    mock_get_token = mock.MagicMock()
    mock_token = mock.MagicMock()
    mock_token.authorization = "authorization 1"
    mock_get_token.return_value = mock_token
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

    mock_urlopen = mock.MagicMock()
    mock_response = mock.MagicMock()
    mock_response.read.return_value = json.dumps(
        {
            "messages": [
                {
                    "to": to,
                    "deliveryStatus": "status 1",
                    "messageId": "id 1",
                    "messageStatusURL": "url 1",
                }
            ]
        }
    ).encode()
    mock_urlopen.return_value.__enter__.return_value = mock_response
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    sms.send(to=to, body=body, **{name: value})

    request_data = mock_urlopen.call_args.args[0].data.decode()
    assert to in request_data
    assert body in request_data
    assert f'"{expected_name}"' in request_data
    assert str(value) in request_data


@pytest.mark.sms
def test_send_error_oauth(monkeypatch):
    """
    GIVEN oauth that raises an error
    WHEN send is called
    THEN SmsError is raised.
    """
    mock_get_token = mock.MagicMock()
    message = "message 1"
    mock_get_token.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

    with pytest.raises(exceptions.SmsError) as exc:
        sms.send(to="0412345678", body="body 1")

    assert message in str(exc.value)


@pytest.mark.sms
def test_send_error_http(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN send is called
    THEN SmsError is raised.
    """
    mock_get_token = mock.MagicMock()
    mock_token = mock.MagicMock()
    mock_token.authorization = "authorization 1"
    mock_get_token.return_value = mock_token
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

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
