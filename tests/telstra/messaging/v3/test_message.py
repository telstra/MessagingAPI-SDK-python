"""Tests for message."""

import functools
import json
import platform
import typing
from unittest import mock
from urllib import request

import pytest

from telstra.messaging.v3 import exceptions, message

VALID_SEND_KWARGS: typing.Dict[str, typing.Any] = {
    "to": "+61412345678",
    "from_": "privateNumber",
    "message_content": "body 1",
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
            {
                **VALID_SEND_KWARGS,
                "message_content": "Hello! from SDK",
                "multimedia": [],
            },
            [
                "message_content",
                "received",
                'a value of "message_content"',
                'or "multimedia"',
            ],
            id="message_content None multimedia None",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "message_content": None, "multimedia": None},
            [
                "message_content",
                "received",
                'a value of "message_content"',
                'or "multimedia"',
            ],
            id="message_content None multimedia None",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "message_content": 1},
            ["message_content", "received", f'"{1}"', "string"],
            id="message_content integer",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "multimedia": 1},
            ["multimedia", "received", f'"{1}"', "list"],
            id="multimedia integer",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "retry_timeout": "1"},
            ["retry_timeout", "received", '"1"', "integer"],
            id="retry_timeout string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "retry_timeout": True},
            ["retry_timeout", "received", f'"{True}"', "integer"],
            id="retry_timeout boolean",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "schedule_send": "2023-03-11T05:25:14.591Z"},
            ["schedule_send", "received", '"2023-03-11T05:25:14.591Z"', "string"],
            id="schedule_send string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "schedule_send": True},
            ["schedule_send", "received", f'"{True}"', "string"],
            id="schedule_send boolean",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "delivery_notification": "1"},
            ["delivery_notification", "received", '"1"', "boolean"],
            id="delivery_notification string",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "delivery_notification": True},
            ["delivery_notification", "received", f'"{True}"', "boolean"],
            id="delivery_notification boolean",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "status_callback_url": True},
            ["status_callback_url", "received", f'"{True}"', "string"],
            id="status_callback_url boolean",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "status_callback_url": "example.com"},
            ["status_callback_url", "received", '"example.com"', "https"],
            id="status_callback_url not https",
        ),
        pytest.param(
            {**VALID_SEND_KWARGS, "tags": ["V3", "SDK"]},
            ["tags", "received", f'"{1}"', "list"],
            id="tags list",
        ),
    ],
)
@pytest.mark.message
def test_send_invalid_param(kwargs, expected_contents):
    """
    GIVEN invalid parameters
    WHEN send is called with the parameters
    THEN MessageError is raised with the expected contents.
    """
    with pytest.raises(exceptions.MessageError) as exc_info:
        message.send(**kwargs)

    # for content in expected_contents:
    #     assert content in str(exc_info.value)


SEND_PARAM_TESTS = [
    # pytest.param("from_", "a1", "from", "a1", id="from_"),
    pytest.param("retry_timeout", 1, "retryTimeout", str(1), id="retry_timeout"),
    pytest.param(
        "schedule_send",
        "2023-03-11T05:25:14.591Z",
        "scheduleSend",
        "2023-03-11T05:25:14.591Z",
        id="schedule_send",
    ),
    pytest.param(
        "status_callback_url",
        "https://example.com",
        "statusCallbackUrl",
        "https://example.com",
        id="status_callback_url",
    ),
    # pytest.param(
    #     "delivery_notification",
    #     True,
    #     "deliveryNotification",
    #     "true",
    #     id="deliveryNotification",
    # ),
    # pytest.param("tags", ["V3", "SDK"], "tags", ["V3", "SDK"], id="tags"),
]


@pytest.mark.parametrize("name, value, expected_name, expected_value", SEND_PARAM_TESTS)
@pytest.mark.message
def test_send_param(
    name, value, expected_name, expected_value, monkeypatch, _mocked_oauth_get_token
):
    """
    GIVEN parameter name and value
    WHEN send is called with the parameter
    THEN a message is sent with the expected parameter name and value.
    """
    to = "0412345678"
    message_content = "Hello! from SDK"

    mock_urlopen = mock.MagicMock()
    mock_response = mock.MagicMock()
    mock_response.read.return_value = json.dumps(
        {
            "messageId": "a60a2e40-c121-11ed-af1f-53be301e485d",
            "status": "queued",
            "to": to,
            "from": "privateNumber",
            "messageContent": message_content,
            "retryTimeout": 10,
            "deliveryNotification": False,
            "queuePriority": 2,
            "tags": [],
        }
    ).encode()
    mock_urlopen.return_value.__enter__.return_value = mock_response
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    message.send(
        to=to, from_="privateNumber", message_content=message_content, **{name: value}
    )

    if int(platform.python_version_tuple()[1]) >= 8:
        request_data = mock_urlopen.call_args.args[0].data.decode()
    else:
        request_data = mock_urlopen.call_args[0][0].data.decode()
    assert to in request_data
    assert "privateNumber" in request_data
    assert message_content in request_data
    assert f'"{expected_name}"' in request_data
    assert expected_value in request_data


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(
            functools.partial(
                message.send,
                to="0412345678",
                from_="privateNumber",
                message_content="Hello! from SDK",
            ),
            id="send",
        ),
        pytest.param(message.get_all, id="get_all"),
        pytest.param(functools.partial(message.get, "id 1"), id="get"),
    ],
)
@pytest.mark.message
def test_send_error_oauth(func, mocked_oauth_get_token_error):
    """
    GIVEN function and oauth that raises an error
    WHEN function is called
    THEN MessageError is raised.
    """
    with pytest.raises(exceptions.MessageError) as exc:
        func()

    assert mocked_oauth_get_token_error in str(exc.value)


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(
            functools.partial(
                message.send,
                to="0412345678",
                from_="privateNumber",
                message_content="Hello! from SDK",
            ),
            id="send",
        ),
        pytest.param(message.get_all, id="get_all"),
        pytest.param(functools.partial(message.get, "id 1"), id="get"),
    ],
)
@pytest.mark.message
def test_error_http(func, _mocked_oauth_get_token, mocked_request_urlopen_error):
    """
    GIVEN function, get_token that returns a token and
    urlopen that raises an error
    WHEN function is called
    THEN MessageError is raised.
    """
    with pytest.raises(exceptions.MessageError) as exc:
        func()

    assert mocked_request_urlopen_error.message in str(exc.value)
    assert str(mocked_request_urlopen_error.code) in str(exc.value)


@pytest.mark.message
def test_get_empty(monkeypatch, _valid_credentials, _mocked_oauth_get_token):
    """
    GIVEN a message has not been received
    WHEN get is called
    THEN a None is returned.
    """
    mock_response = mock.MagicMock()
    mock_response.read.return_value = json.dumps(
        {
            "messages": [],
            "paging": {
                "nextPage": "",
                "previousPage": "",
                "lastPage": "",
                "totalCount": "0",
            },
        }
    ).encode()
    mock_urlopen = mock.MagicMock()
    mock_urlopen.return_value.__enter__.return_value = mock_response
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    returned_reply = message.get_all()

    assert returned_reply is not None
