"""Tests for the messaging API."""

from tls.messaging import exceptions, sms, subscription


def test_send_sms():
    """
    GIVEN credentials in the environment
    WHEN send is called
    THEN no errors are raised.
    """
    subscription_value = subscription.get()
    sms.send(to=subscription_value.destination_address, body="Test")


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
