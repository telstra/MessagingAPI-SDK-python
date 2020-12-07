"""Tests for creating subscriptions."""

import pytest

from messaging import subscription


def test_create(_valid_credentials):
    """
    GIVEN
    WHEN create is called
    THEN a subscription is provisioned.
    """
    returned_subscription = subscription.create()

    assert returned_subscription.destination_address is not None
    assert returned_subscription.active_days is not None
