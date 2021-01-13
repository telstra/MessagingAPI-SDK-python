"""Tests for the messaging API."""

from tls.messaging import sms, subscription


def test_send_sms():
    """
    GIVEN credentials in the environment
    WHEN send is called
    THEN no errors are raised.
    """
    subscription_value = subscription.get()
    sms.send(to=subscription_value.destination_address, body="Test")
