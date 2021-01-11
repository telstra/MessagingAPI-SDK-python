"""Handle subscriptions."""

import dataclasses
import json
from urllib import error, request

from . import exceptions, oauth

_URL = "https://tapi.telstra.com/v2/messages/provisioning/subscriptions"


@dataclasses.dataclass
class TSubscription:
    """
    A phone number subscription.

    Attrs:
        destination_address: The phone number that a message can be sent to.
        active_days: The number of days left on the subscription.

    """

    destination_address: str
    active_days: int


def create(active_days: int = 30) -> TSubscription:
    """
    Create a subscription.

    Raises SubscriptionError if anything goes wrong.

    Args:
        active_days: The number of days the subscription will be active.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SubscriptionError(
            f"Could not create subscription: {exc}"
        ) from exc

    data = json.dumps({"activeDays": active_days}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    subscription_request = request.Request(
        _URL, data=data, headers=headers, method="POST"
    )
    try:
        with request.urlopen(subscription_request) as response:
            subscription_dict = json.loads(response.read().decode())
            return TSubscription(
                destination_address=subscription_dict["destinationAddress"],
                active_days=subscription_dict["activeDays"],
            )
    except error.HTTPError as exc:
        raise exceptions.SubscriptionError(
            f"Could not create subscription: {exc}"
        ) from exc


def get() -> TSubscription:
    """
    Retrieve current subscription.

    Raises SubscriptionError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SubscriptionError(
            f"Could not retrieve subscription: {exc}"
        ) from exc

    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    subscription_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(subscription_request) as response:
            subscription_dict = json.loads(response.read().decode())
            return TSubscription(
                destination_address=subscription_dict["destinationAddress"],
                active_days=subscription_dict["activeDays"],
            )
    except error.HTTPError as exc:
        raise exceptions.SubscriptionError(
            f"Could not delete subscription: {exc}"
        ) from exc


def delete() -> None:
    """
    Delete current subscription.

    Raises SubscriptionError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SubscriptionError(
            f"Could not delete subscription: {exc}"
        ) from exc

    data = json.dumps({"emptyArr": 0}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    subscription_request = request.Request(
        _URL, data=data, headers=headers, method="DELETE"
    )
    try:
        with request.urlopen(subscription_request):
            return
    except error.HTTPError as exc:
        raise exceptions.SubscriptionError(
            f"Could not delete subscription: {exc}"
        ) from exc
