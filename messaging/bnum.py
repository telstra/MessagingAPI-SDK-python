"""Used to work with BNUMs for the free trial."""

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
        raise exceptions.BnumError(
            f'invalid value for "phone_numbers" argument, expecting list of strings, '
            f'received "{phone_numbers}"'
        )
    result = next(
        filter(lambda result: not result.valid, map(phone_number.check, phone_numbers)),
        None,
    )
    if result is not None:
        raise exceptions.BnumError(
            f'invalid value for "phone_numbers" argument, {result.reason}'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.BnumError(f"Could register phone numbers: {exc}") from exc

    data = json.dumps({"bnum": phone_numbers}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(_URL, data=data, headers=headers, method="POST")
    try:
        with request.urlopen(sms_request) as response:
            bnum_dict = json.loads(response.read().decode())
            return bnum_dict["bnum"]
    except error.HTTPError as exc:
        raise exceptions.BnumError(f"Could register phone numbers: {exc}") from exc


def get() -> TPhoneNumbers:
    """
    Retrieve the registered phone numbers as b party's in the free trial.

    Returns:
        The phone numbers that have been registered.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.BnumError(f"Could retrieve phone numbers: {exc}") from exc

    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(sms_request) as response:
            data = response.read().decode()
            bnum_dict = json.loads(data)
            return bnum_dict["bnum"]
    except error.HTTPError as exc:
        raise exceptions.BnumError(f"Could retrieve phone numbers: {exc}") from exc
