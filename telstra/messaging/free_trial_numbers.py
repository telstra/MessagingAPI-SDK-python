"""Used to work with Free Trial Numbers."""

import json
import typing
from urllib import error, request

from . import exceptions, oauth
from .utils import error_response as error_response_util
from .utils import free_trial_number

_URL = "https://products.api.telstra.com/messaging/v3/free-trial-numbers"
TFreeTrialNumbers = typing.List[str]


def create(phone_numbers: TFreeTrialNumbers) -> TFreeTrialNumbers:
    """
    Register phone numbers as b party's in the free trial.

    Args:
        phone_numbers: The phone numbers to register.

    Returns:
        The phone numbers that have been registered.

    """
    if not isinstance(phone_numbers, list):
        raise exceptions.FreeTrialNumbersError(
            'invalid value for "phone_numbers" argument, '
            "expecting list of strings, "
            f'received "{phone_numbers}"'
        )
    result = next(
        filter(
            lambda result: not result.valid, map(free_trial_number.check, phone_numbers)
        ),
        None,
    )
    if result is not None:
        raise exceptions.FreeTrialNumbersError(
            f'invalid value for "phone_numbers" argument, {result.reason}'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.FreeTrialNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data = json.dumps({"freeTrialNumbers": phone_numbers}).encode()
    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    trail_numbers_request = request.Request(
        _URL, data=data, headers=headers, method="POST"
    )
    try:
        with request.urlopen(trail_numbers_request) as response:
            free_trial_numbers_dict = json.loads(response.read().decode())
            return free_trial_numbers_dict["freeTrialNumbers"]
    except error.HTTPError as exc:
        suggested_actions_string = ""
        try:
            error_response = json.loads(exc.read().decode())
            list_of_error_dicts = error_response.get("errors", [])
            suggested_actions_string = (
                error_response_util.get_suggeted_actions_list_str(
                    list_of_error_dicts=list_of_error_dicts, key="suggested_action"
                )
            )
        except Exception:
            raise exceptions.FreeTrialNumbersError(
                f"Could not register free trial numbers: {exc}"
            ) from exc
        raise exceptions.FreeTrialNumbersError(
            f"Could not register free trial numbers. {suggested_actions_string}"
        ) from exc


def get_all() -> TFreeTrialNumbers:
    """
    Retrieve the free trial numbers.

    Returns:
        The list of phone numbers that have been added
          to your free trial numbers list.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.FreeTrialNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    free_trail_numbers_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(free_trail_numbers_request) as response:
            data = response.read().decode()
            if data is not None and isinstance(data, str) and len(data) > 0:
                free_trial_numbers_dict = json.loads(data)
                return free_trial_numbers_dict["freeTrialNumbers"]
            else:
                return []

    except error.HTTPError as exc:
        suggested_actions_string = ""
        try:
            error_response = json.loads(exc.read().decode())
            list_of_error_dicts = error_response.get("errors", [])
            suggested_actions_string = (
                error_response_util.get_suggeted_actions_list_str(
                    list_of_error_dicts=list_of_error_dicts, key="suggested_action"
                )
            )
        except Exception:
            raise exceptions.FreeTrialNumbersError(
                f"Could not retrieve free trial numbers: {exc}"
            ) from exc
        raise exceptions.FreeTrialNumbersError(
            f"Could not retrieve free trial numbers. {suggested_actions_string}"
        ) from exc
