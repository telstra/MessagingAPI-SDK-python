"""Used to work with Trial Numbers for the free trial."""

import json
import typing
from urllib import error, request

from . import exceptions, oauth
from .utils import phone_number

TPhoneNumbers = typing.List[str]
_URL = "https://tapi.telstra.com/v2/messages/freetrial/bnum"


def register(phone_numbers: TPhoneNumbers) -> TPhoneNumbers:
    """
    Register phone numbers as b party's in the free trial.

    Args:
        phone_numbers: The phone numbers to register.

    Returns:
        The phone numbers that have been registered.

    """
    if not isinstance(phone_numbers, list):
        raise exceptions.TrialNumbersError(
            f'invalid value for "phone_numbers" argument, expecting list of strings, '
            f'received "{phone_numbers}"'
        )
    result = next(
        filter(lambda result: not result.valid, map(phone_number.check, phone_numbers)),
        None,
    )
    if result is not None:
        raise exceptions.TrialNumbersError(
            f'invalid value for "phone_numbers" argument, {result.reason}'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.TrialNumbersError(
            f"Could register phone numbers: {exc}"
        ) from exc

    data = json.dumps({"bnum": phone_numbers}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    trail_numbers_request = request.Request(
        _URL, data=data, headers=headers, method="POST"
    )
    try:
        with request.urlopen(trail_numbers_request) as response:
            trial_numbers_dict = json.loads(response.read().decode())
            return trial_numbers_dict["bnum"]
    except error.HTTPError as exc:
        raise exceptions.TrialNumbersError(
            f"Could register phone numbers: {exc}"
        ) from exc


def get() -> TPhoneNumbers:
    """
    Retrieve the registered phone numbers as b party's in the free trial.

    Returns:
        The phone numbers that have been registered.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.TrialNumbersError(
            f"Could retrieve phone numbers: {exc}"
        ) from exc

    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    trail_numbers_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(trail_numbers_request) as response:
            data = response.read().decode()
            if data is not None and isinstance(data, str) and len(data) > 0:
                trial_numbers_dict = json.loads(data)
                return trial_numbers_dict["bnum"]
            else:
                return []

    except error.HTTPError as exc:
        raise exceptions.TrialNumbersError(
            f"Could retrieve phone numbers: {exc}"
        ) from exc
