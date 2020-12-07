"""Tests for sms."""

from unittest import mock
from urllib import error, request

import pytest

from messaging import sms, subscription, exceptions


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


def test_send_error(monkeypatch):
    """
    GIVEN urlopen that raises an error
    WHEN send is called
    THEN SmsError is raised.
    """
    code = 401
    msg = "msg 1"
    mock_urlopen = mock.MagicMock()
    mock_urlopen.side_effect = error.HTTPError(
        url="url 1", code=code, msg=msg, hdrs={}, fp=mock.MagicMock()
    )
    monkeypatch.setattr(request, "urlopen", mock_urlopen)

    with pytest.raises(exceptions.SmsError) as exc:
        sms.send(to="to 1", body="body 1")

    assert msg in str(exc.value)
    assert str(code) in str(exc.value)
