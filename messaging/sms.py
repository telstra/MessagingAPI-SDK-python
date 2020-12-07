"""Used to send messages."""

import dataclasses
import json
from urllib import request, error

from . import oauth, exceptions


@dataclasses.dataclass
class TSms:
    """
    A sms.

    Attrs:
        to: The destination.
        delivery_status: Whether the delivery has been completed.
        message_id: Unique identifier.
        message_status_url: URL to retrieve the current delivery status.

    """

    to: str
    delivery_status: str
    message_id: str
    message_status_url: str


def send(to: str, body: str) -> TSms:
    """
    Send an SMS.

    Args:
        to: The destination mobile number.
        body: The body of the message.

    """
    token = oauth.get_token()
    url = "https://tapi.telstra.com/v2/messages/sms"
    data = json.dumps({"to": to, "body": body}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(url, data=data, headers=headers, method="POST")
    try:
        with request.urlopen(sms_request) as response:
            sms_dict = json.loads(response.read().decode())
            return TSms(
                to=sms_dict["messages"][0]["to"],
                delivery_status=sms_dict["messages"][0]["deliveryStatus"],
                message_id=sms_dict["messages"][0]["messageId"],
                message_status_url=sms_dict["messages"][0]["messageStatusURL"],
            )
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not send SMS: {exc}") from exc
