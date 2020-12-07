"""Tests for sms."""

from messaging import sms, subscription


def test_send(_valid_credentials):
    """
    GIVEN
    WHEN send is called
    THEN a sms is provisioned.
    """
    to = subscription.create().destination_address
    body = "body 1"

    returned_sms = sms.send(to=to, body=body)

    assert returned_sms.to == to
    assert returned_sms.delivery_status is not None
    assert returned_sms.message_id is not None
    assert returned_sms.message_status_url is not None
