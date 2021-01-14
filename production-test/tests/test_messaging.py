"""Tests for the messaging API."""

import pytest

from tls.messaging import exceptions, sms, subscription


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param({}, id="empty"),
        pytest.param(
            {
                "from_": "a1",
                "validity": 60,
                "scheduled_delivery": 5,
                "notify_url": "https://example.com",
                "priority": True,
                "user_msg_ref": "ref 1",
            },
            id=(
                "from_, validity, scheduled_delivery, notify_url, priority, "
                "user_msg_ref"
            ),
        ),
        pytest.param({"reply_request": True}, id="reply_request"),
        pytest.param({"receipt_off": True}, id="receipt_off"),
    ],
)
def test_send_sms(kwargs):
    """
    GIVEN credentials in the environment and kwargs
    WHEN send is called with the kwargs
    THEN no errors are raised.
    """
    subscription_value = subscription.get()
    sms.send(to=subscription_value.destination_address, body="Test", **kwargs)


def test_get_reply():
    """
    GIVEN credentials in the environment
    WHEN send and then get_next_unread_reply is called
    THEN no errors are raised.
    """
    subscription_value = subscription.get()
    sms.send(to=subscription_value.destination_address, body="Test")
    sms.get_next_unread_reply()


def test_get_status():
    """
    GIVEN credentials in the environment and a sent SMS
    WHEN get_status is called
    THEN no errors are raised.
    """
    subscription_value = subscription.get()
    sent_sms = sms.send(to=subscription_value.destination_address, body="Test")

    retries = 5
    for retry_counter in range(retries):
        try:
            sms.get_status(sent_sms.message_id)
        except exceptions.SmsError as exc:
            if retry_counter == retries - 1:
                raise exc
