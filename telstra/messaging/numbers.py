"""Handle numbers."""

import dataclasses
import json
import typing
from urllib import error, request

from . import exceptions, oauth, types
from .utils import notify_url as notify_url_util

_URL = "https://tapi.telstra.com/v2/messages/provisioning/subscriptions"


@dataclasses.dataclass
class TNumbers:
    """
    A phone number.

    Attrs:
        destination_address: The phone number that a message can be sent to.
        active_days: The number of days left.

    """

    destination_address: str
    active_days: int


def create(
    active_days: int = 30, notify_url: typing.Optional[types.TNotifyUrl] = None
) -> TNumbers:
    """
    Create a number.

    Raises NumbersError if anything goes wrong.

    Args:
        active_days: The number of days the number will be active.
        notify_url: A notification URL that will be POSTed to whenever a new message
            (i.e. a reply to a message sent) arrives at this destination address.

    """
    # Validate active_days
    if not isinstance(active_days, int) or isinstance(active_days, bool):
        raise exceptions.NumbersError(
            'the value of "active_days" is not valid, expected an integer, '
            f'received "{active_days}"'
        )
    # Validate notify_url
    notify_url_util.validate(value=notify_url, exception=exceptions.NumbersError)

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.NumbersError(f"Could not create number: {exc}") from exc

    data: typing.Dict[str, typing.Any] = {"activeDays": active_days}
    if notify_url is not None:
        data["notifyURL"] = notify_url
    data_str = json.dumps(data).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(
        _URL, data=data_str, headers=headers, method="POST"
    )
    try:
        with request.urlopen(numbers_request) as response:
            numbers_dict = json.loads(response.read().decode())
            return TNumbers(
                destination_address=numbers_dict["destinationAddress"],
                active_days=numbers_dict["activeDays"],
            )
    except error.HTTPError as exc:
        raise exceptions.NumbersError(f"Could not create number: {exc}") from exc


def get() -> TNumbers:
    """
    Retrieve current number.

    Raises NumbersError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.NumbersError(f"Could not retrieve number: {exc}") from exc

    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(numbers_request) as response:
            numbers_dict = json.loads(response.read().decode())
            return TNumbers(
                destination_address=numbers_dict["destinationAddress"],
                active_days=numbers_dict["activeDays"],
            )
    except error.HTTPError as exc:
        raise exceptions.NumbersError(f"Could not delete number: {exc}") from exc


def delete() -> None:
    """
    Delete current number.

    Raises NumbersError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.NumbersError(f"Could not delete number: {exc}") from exc

    data = json.dumps({"emptyArr": 0}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(_URL, data=data, headers=headers, method="DELETE")
    try:
        with request.urlopen(numbers_request):
            return
    except error.HTTPError as exc:
        raise exceptions.NumbersError(f"Could not delete number: {exc}") from exc
