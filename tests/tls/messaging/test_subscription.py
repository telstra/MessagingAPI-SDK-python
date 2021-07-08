"""Tests for subscriptions."""

import json
import platform
from unittest import mock
from urllib import request

import pytest

from telstra.messaging import exceptions, subscription


@pytest.mark.parametrize(
    "kwargs, expected_contents",
    [
        pytest.param(
            {"active_days": "1"},
            ["active_days", "received", '"1"', "integer"],
            id="active_days string",
        ),
        pytest.param(
            {"active_days": True},
            ["active_days", "received", f'"{True}"', "integer"],
            id="active_days boolean",
        ),
        pytest.param(
            {"notify_url": True},
            ["notify_url", "received", f'"{True}"', "string"],
            id="notify_url not string",
        ),
        pytest.param(
            {"notify_url": "example.com"},
            ["notify_url", "received", '"example.com"', "https"],
            id="notify_url not https",
        ),
    ],
)
@pytest.mark.subscription
def test_create_invalid_param(kwargs, expected_contents):
    """
    GIVEN invalid parameters
    WHEN create is called with the parameters
    THEN SubscriptionError is raised with the expected contents.
    """
    with pytest.raises(exceptions.SubscriptionError) as exc_info:
        subscription.create(**kwargs)

    for content in expected_contents:
        assert content in str(exc_info.value)


CREATE_PARAM_TESTS = [
    pytest.param("active_days", 30, "activeDays", str(30), id="active_days"),
    pytest.param(
        "notify_url",
        "https://example.com",
        "notifyURL",
        "https://example.com",
        id="active_days",
    ),
]


@pytest.mark.parametrize(
    "name, value, expected_name, expected_value", CREATE_PARAM_TESTS
)
@pytest.mark.subscription
def test_create_param(
    name, value, expected_name, expected_value, monkeypatch, _mocked_oauth_get_token
):
    """
    GIVEN parameter name and value
    WHEN create is called with the parameter
    THEN a subscription is created with the expected parameter name and value.
    """
    mock_urlopen = mock.MagicMock()
    mock_response = mock.MagicMock()
    mock_response.read.return_value = json.dumps(
        {"destinationAddress": "address 1", "activeDays": 30}
    ).encode()
    mock_urlopen.return_value.__enter__.return_value = mock_response
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    subscription.create(**{name: value})

    if int(platform.python_version_tuple()[1]) >= 8:
        request_data = mock_urlopen.call_args.args[0].data.decode()
    else:
        request_data = mock_urlopen.call_args[0][0].data.decode()
    assert f'"{expected_name}"' in request_data
    assert expected_value in request_data


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param({}, id="empty"),
        pytest.param(
            {"active_days": 1, "notify_url": "https://example.com"},
            id="active_days, notify_url",
        ),
    ],
)
@pytest.mark.subscription
def test_create_get_delete(kwargs, _valid_credentials):
    """
    GIVEN valid credentials and kwargs
    WHEN create is called with the kwargs, get and delete is called
    THEN a subscription is provisioned, returned and deleted.
    """
    created_subscription = subscription.create(**kwargs)

    assert created_subscription.destination_address is not None
    assert created_subscription.active_days is not None

    retrieved_subscription = subscription.get()

    assert retrieved_subscription.destination_address is not None
    assert retrieved_subscription.active_days is not None

    subscription.delete()


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(subscription.create, id="create"),
        pytest.param(subscription.get, id="get"),
        pytest.param(subscription.delete, id="delete"),
    ],
)
@pytest.mark.subscription
def test_error_oauth(func, mocked_oauth_get_token_error):
    """
    GIVEN subscription function and oauth that raises an error
    WHEN function is called
    THEN SubscriptionError is raised.
    """
    with pytest.raises(exceptions.SubscriptionError) as exc:
        func()

    assert mocked_oauth_get_token_error in str(exc.value)


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(subscription.create, id="create"),
        pytest.param(subscription.get, id="get"),
        pytest.param(subscription.delete, id="delete"),
    ],
)
@pytest.mark.subscription
def test_error_http(func, mocked_request_urlopen_error, _mocked_oauth_get_token):
    """
    GIVEN subscription function and urlopen that raises an error
    WHEN function is called
    THEN SubscriptionError is raised.
    """
    with pytest.raises(exceptions.SubscriptionError) as exc:
        func()

    assert mocked_request_urlopen_error.message in str(exc.value)
    assert str(mocked_request_urlopen_error.code) in str(exc.value)
