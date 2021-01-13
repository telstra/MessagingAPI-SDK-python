"""Tests for subscriptions."""

from unittest import mock
from urllib import error, request

import pytest

from telstra.messaging import exceptions, oauth, subscription


@pytest.mark.subscription
def test_create_get_delete(_valid_credentials):
    """
    GIVEN
    WHEN create, get and delete is called
    THEN a subscription is provisioned, returned and deleted.
    """
    created_subscription = subscription.create()

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
def test_error_oauth(func, monkeypatch):
    """
    GIVEN subscription function and oauth that raises an error
    WHEN function is called
    THEN SubscriptionError is raised.
    """
    mock_get_token = mock.MagicMock()
    message = "message 1"
    mock_get_token.side_effect = exceptions.CredentialError(message)
    monkeypatch.setattr(oauth, "get_token", mock_get_token)

    with pytest.raises(exceptions.SubscriptionError) as exc:
        func()

    assert message in str(exc.value)


@pytest.mark.parametrize(
    "func",
    [
        pytest.param(subscription.create, id="create"),
        pytest.param(subscription.get, id="get"),
        pytest.param(subscription.delete, id="delete"),
    ],
)
@pytest.mark.subscription
def test_error_http(func, monkeypatch):
    """
    GIVEN subscription function and urlopen that raises an error
    WHEN function is called
    THEN SubscriptionError is raised.
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

    with pytest.raises(exceptions.SubscriptionError) as exc:
        func()

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)
