"""Used to work with BNUMs for the free trial."""

import dataclasses
import typing
import json
from urllib import request, error

from . import oauth, exceptions


TPhoneNumbers = typing.List[str]


def register(phone_numbers: TPhoneNumbers) -> TPhoneNumbers:
    """
    Register phone numbers as b party's in the free trial.

    Args:
        phone_numbers: The phone numbers to register.

    Returns:
        The phone numbers that have been registered.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.BnumError(f"Could register phone numbers: {exc}") from exc

    url = "https://tapi.telstra.com/v2/messages/freetrial/bnum"
    data = json.dumps({"bnum": phone_numbers}).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(url, data=data, headers=headers, method="POST")
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

    url = "https://tapi.telstra.com/v2/messages/freetrial/bnumm"
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(url, headers=headers, method="GET")
    try:
        with request.urlopen(sms_request) as response:
            bnum_dict = json.loads(response.read().decode())
            return bnum_dict["bnum"]
    except error.HTTPError as exc:
        raise exceptions.BnumError(f"Could retrieve phone numbers: {exc}") from exc
