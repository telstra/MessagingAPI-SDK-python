"""Used to send messages."""

from messaging.utils import phone_number
import typing
import dataclasses
import json
from urllib import request, error

from . import oauth, exceptions
from .utils import phone_number


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

    to: typing.Union[str, typing.List[str]]
    delivery_status: str
    message_id: str
    message_status_url: str


def send(to: typing.Union[str, typing.List[str]], body: str) -> TSms:
    """
    Send an SMS.

    Args:
        to: The destination mobile number.
        body: The body of the message.

    """
    # Validate input
    if not isinstance(to, str) and not isinstance(to, list):
        raise exceptions.SmsError(
            f'the value of "to" is not valid, expecting a string or a list of string, '
            f'received "{to}"'
        )
    if isinstance(to, str):
        result = phone_number.check(value=to)
        if not result.valid:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {result.reason}'
            )
    if isinstance(to, list):
        result = next(
            filter(lambda result: not result.valid, map(phone_number.check, to)),
            None,
        )
        if result is not None:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {result.reason}'
            )
    if not isinstance(body, str):
        raise exceptions.SmsError(
            f'the value of "body" is not valid, expected a string, received "{body}"'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

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
