"""Tests for subscriptions."""

from unittest import mock
from urllib import error, request

import pytest

from messaging import subscription, exceptions


def test_create(_valid_credentials):
    """
    GIVEN
    WHEN create is called
    THEN a subscription is provisioned.
    """
    returned_subscription = subscription.create()

    assert returned_subscription.destination_address is not None
    assert returned_subscription.active_days is not None


def test_create_error(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN create is called
    THEN SubscriptionError is raised.
    """
    code = 401
    msg = "msg 1"
    mock_urlopen = mock.MagicMock()
    mock_urlopen.side_effect = error.HTTPError(
        url="url 1", code=code, msg=msg, hdrs={}, fp=mock.MagicMock()
    )
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    with pytest.raises(exceptions.SubscriptionError) as exc:
        subscription.create()

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)
