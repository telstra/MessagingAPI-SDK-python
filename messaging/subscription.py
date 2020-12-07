"""Handle subscriptions."""

import dataclasses
import typing
import json
from urllib import request, error

from . import oauth, exceptions


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

    Args:
        active_days: The number of days the subscription will be active.

    """
    token = oauth.get_token()
    url = "https://tapi.telstra.com/v2/messages/provisioning/subscriptions"
    data = json.dumps({"activeDays": active_days}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    subscription_request = request.Request(
        url, data=data, headers=headers, method="POST"
    )
    try:
        with request.urlopen(subscription_request) as response:
            subscription_dict = json.loads(response.read().decode())
            return TSubscription(
                destination_address=subscription_dict["destinationAddress"],
                active_days=subscription_dict["activeDays"],
            )
    except error.HTTPError as exc:
        raise exceptions.SubscriptionError(f"Could not retrieve token: {exc}") from exc
