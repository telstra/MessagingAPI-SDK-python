"""Handle virtual numbers."""

import dataclasses
import json
import typing
from urllib import error, parse, request

from . import exceptions, oauth, types
from .utils import callback_url as callback_url_util
from .utils import error_response as error_response_util
from .utils import querystring
from .utils import virtual_number as virtual_number_util

_URL = "https://products.api.telstra.com/messaging/v3/virtual-numbers"


@dataclasses.dataclass
class TVirtualNumber:
    """
    A virtual phone number.

    Attrs:
        reply_callback_url: URL that replies to the Virtual Number
        should be sent to.
        tags: List of strings used as tags to the virtual number.

    """

    virtual_number: str
    last_use: str
    reply_callback_url: types.TStatusCallbackUrl | None = None
    tags: types.TTags | None = None


@dataclasses.dataclass
class TPaging:
    """
    Paging.

    Attrs:
        next_page:
        previous_page:
        last_page:
        total_count:

    """

    next_page: str
    previous_page: str
    last_page: str
    total_count: int = 0


@dataclasses.dataclass
class TVirtualNumbers:
    """
    List of virtual phone numbers.

    Attrs:
        virtual_numbers:
        paging:

    """

    virtual_numbers: list[TVirtualNumber]
    paging: TPaging


@dataclasses.dataclass
class TRecipientOptout:
    """
    A recipient optout mobile number.

    Attrs:
        message_id: A unique identifier for the message sent.
        optout_number: Recipient optout number.
        virtual_number: A virtual number assigned to your account.
        create_timestamp:

    """

    message_id: str
    virtual_number: str
    optout_number: str
    create_timestamp: str


@dataclasses.dataclass
class TRecipientOptouts:
    """
    List of recipient optout numbers.

    Attrs:
        recipient_optouts:
        paging:

    """

    recipient_optouts: list[TRecipientOptout]
    paging: TPaging


def assign(
    reply_callback_url: typing.Optional[types.TStatusCallbackUrl] = None,
    tags: typing.Optional[typing.List[types.TTags]] = None,
) -> TVirtualNumber:
    """
    Assign a virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    Args:
        reply_callback_url: URL that replies to the Virtual Number
        should be sent to.
        tags: List of strings used as tags to the virtual number.

    """
    # Validate tags
    if (tags is not None and not isinstance(tags, list)) or (
        tags is not None
        and isinstance(tags, list)
        and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.VirtualNumbersError(
            'the value of "tags" is not valid, expected a list of strings '
            "with alteast one tag or a maximum of 10, "
            f'received "{tags}"'
        )
    # Validate reply_callback_url
    callback_url_util.validate(
        name="reply_callback_url",
        value=reply_callback_url,
        exception=exceptions.VirtualNumbersError,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {}
    if reply_callback_url is not None:
        data["replyCallbackUrl"] = reply_callback_url
    if tags is not None:
        data["tags"] = tags
    data_str = json.dumps(data).encode()
    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(
        _URL, data=data_str, headers=headers, method="POST"
    )
    try:
        with request.urlopen(numbers_request) as response:
            virtual_numbers_dict = json.loads(response.read().decode())
            return TVirtualNumber(
                virtual_number=virtual_numbers_dict.get("virtualNumber"),
                reply_callback_url=virtual_numbers_dict.get("replyCallbackUrl", None),
                tags=virtual_numbers_dict.get("tags", None),
                last_use=virtual_numbers_dict.get("lastUse"),
            )
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
            raise exceptions.VirtualNumbersError(
                f"Could not assign virtual number: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not assign virtual number. {suggested_actions_string}"
        ) from exc


def _validate_get_all_args(
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
    filter_: typing.Optional[types.TFilter] = None,
) -> None:
    # Validate limit
    if (limit is not None and not isinstance(limit, types.TLimit)) or (
        limit is not None
        and isinstance(limit, types.TLimit)
        and (limit < 1 or limit > 50)
    ):
        raise exceptions.VirtualNumbersError(
            'the value of "limit" is not valid, expected a int value '
            f'between 1 and 50, received "{limit}"'
        )

    # Validate offset
    if (offset is not None and not isinstance(offset, types.TOffset)) or (
        offset is not None
        and isinstance(offset, types.TOffset)
        and (offset < 0 or offset > 999999)
    ):
        raise exceptions.VirtualNumbersError(
            'the value of "offset" is not valid, expected a int value '
            f'between 0 and 999999, received "{offset}"'
        )

    # Validate filter
    if filter_ is not None and not isinstance(filter_, types.TFilter):
        raise exceptions.VirtualNumbersError(
            'the value of "filter" is not valid, expected a string, '
            f'received "{filter_}"'
        )


def get_all(
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
    filter_: typing.Optional[types.TFilter] = None,
) -> TVirtualNumbers:
    """
    Retrieve all virtual numbers assigned to you.

    Raises VirtualNumbersError if anything goes wrong.

    """

    _validate_get_all_args(limit=limit, offset=offset, filter_=filter_)

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    virtual_numbers_request = request.Request(
        f"{_URL}" f"{querystring.build(limit=limit, offset=offset, filter=filter_)}",
        headers=headers,
        method="GET",
    )
    try:
        with request.urlopen(virtual_numbers_request) as response:
            virtual_numbers: list[TVirtualNumber] = []
            virtual_numbers_response_dict = json.loads(response.read().decode())
            virtual_numbers_list = virtual_numbers_response_dict.get(
                "virtualNumbers", []
            )

            if virtual_numbers_list is not None and len(virtual_numbers_list) > 0:
                virtual_numbers = [
                    TVirtualNumber(
                        virtual_number=d.get("virtualNumber"),
                        reply_callback_url=d.get("replyCallbackUrl", None),
                        tags=d.get("tags", None),
                        last_use=d.get("lastUse"),
                    )
                    for d in virtual_numbers_list
                ]
            paging = TPaging(
                next_page=virtual_numbers_response_dict["paging"].get("nextPage", ""),
                previous_page=virtual_numbers_response_dict["paging"].get(
                    "previousPage", ""
                ),
                last_page=virtual_numbers_response_dict["paging"].get("lastPage", ""),
                total_count=virtual_numbers_response_dict["paging"].get(
                    "totalCount", 0
                ),
            )
            return TVirtualNumbers(
                virtual_numbers=([] if virtual_numbers is None else virtual_numbers),
                paging=paging,
            )
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
            raise exceptions.VirtualNumbersError(
                f"Could not retrieve virtual numbers: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve virtual numbers. {suggested_actions_string}"
        ) from exc


def get(virtual_number: str) -> TVirtualNumber:
    """
    Retrieve virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    """
    # Validate virtual_number
    result = virtual_number_util.check(virtual_number)
    if not result.valid:
        raise exceptions.VirtualNumbersError(
            f'the value of "virtual_number" is not valid, {result.reason}'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    virtual_numbers_request = request.Request(
        f"{_URL}/{parse.quote(virtual_number)}", headers=headers, method="GET"
    )
    try:
        with request.urlopen(virtual_numbers_request) as response:
            virtual_numbers_dict = json.loads(response.read().decode())
            return TVirtualNumber(
                virtual_number=virtual_numbers_dict.get("virtualNumber"),
                reply_callback_url=virtual_numbers_dict.get("replyCallbackUrl", None),
                tags=virtual_numbers_dict.get("tags", None),
                last_use=virtual_numbers_dict.get("lastUse"),
            )
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
            raise exceptions.VirtualNumbersError(
                f"Could not retrieve virtual number: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve virtual number. {suggested_actions_string}"
        ) from exc


def update(
    virtual_number: str,
    reply_callback_url: typing.Optional[types.TStatusCallbackUrl] = None,
    tags: typing.Optional[typing.List[types.TTags]] = None,
) -> TVirtualNumber:
    """
    Update a virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    Args:
        virtual_number: virtual_number you want to update.
        reply_callback_url: URL that replies to the Virtual Number
        should be sent to.
        tags: List of strings used as tags to the virtual number.

    """
    # Validate virtual_number
    result = virtual_number_util.check(virtual_number)
    if not result.valid:
        raise exceptions.VirtualNumbersError(
            f'the value of "virtual_number" is not valid, {result.reason}'
        )

    # Validate tags
    if (tags is not None and not isinstance(tags, list)) or (
        tags is not None
        and isinstance(tags, list)
        and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.VirtualNumbersError(
            'the value of "tags" is not valid, expected a list of '
            "strings with alteast one tag or a maximum of 10, "
            f'received "{tags}"'
        )

    # Validate reply_callback_url
    callback_url_util.validate(
        name="reply_callback_url",
        value=reply_callback_url,
        exception=exceptions.VirtualNumbersError,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {}
    if reply_callback_url is not None:
        data["replyCallbackUrl"] = reply_callback_url
    if tags is not None:
        data["tags"] = tags
    data_str = json.dumps(data).encode()
    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    virtual_numbers_update_request = request.Request(
        f"{_URL}/{parse.quote(virtual_number)}",
        data=data_str,
        headers=headers,
        method="PUT",
    )
    try:
        with request.urlopen(virtual_numbers_update_request) as response:
            virtual_numbers_dict = json.loads(response.read().decode())
            return TVirtualNumber(
                virtual_number=virtual_numbers_dict.get("virtualNumber"),
                reply_callback_url=virtual_numbers_dict.get("replyCallbackUrl", None),
                tags=virtual_numbers_dict.get("tags", None),
                last_use=virtual_numbers_dict.get("lastUse"),
            )
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
            raise exceptions.VirtualNumbersError(
                f"Could not update virtual number: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not update virtual number. {suggested_actions_string}"
        ) from exc


def delete(virtual_number: str) -> None:
    """
    Delete virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    """
    # Validate virtual_number
    result = virtual_number_util.check(virtual_number)
    if not result.valid:
        raise exceptions.VirtualNumbersError(
            f'the value of "virtual_number" is not valid, {result.reason}'
        )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(
        f"{_URL}/{parse.quote(virtual_number)}", headers=headers, method="DELETE"
    )
    try:
        with request.urlopen(numbers_request):
            return
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
            raise exceptions.VirtualNumbersError(
                f"Could not delete virtual number: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not delete virtual number. {suggested_actions_string}"
        ) from exc


def get_optouts(
    virtual_number: str,
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
) -> TRecipientOptouts:
    """
    Retrieve all virtual numbers assigned to you.

    Raises VirtualNumbersError if anything goes wrong.

    """

    _validate_get_all_args(limit=limit, offset=offset, filter_=None)

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    optouts_request = request.Request(
        f"{_URL}"
        f"/{virtual_number}/optouts"
        f"{querystring.build(limit=limit, offset=offset)}",
        headers=headers,
        method="GET",
    )
    try:
        with request.urlopen(optouts_request) as response:
            optouts: list[TRecipientOptout] = []
            optouts_response_dict = json.loads(response.read().decode())
            optouts_list = optouts_response_dict.get("recipientOptouts", [])

            if optouts_list is not None and len(optouts_list) > 0:
                optouts = [
                    TRecipientOptout(
                        message_id=d.get("messageId"),
                        virtual_number=d.get("virtualNumber"),
                        optout_number=d.get("optoutNumber"),
                        create_timestamp=d.get("createTimestamp"),
                    )
                    for d in optouts_list
                ]
            paging = TPaging(
                next_page=optouts_response_dict["paging"].get("nextPage", ""),
                previous_page=optouts_response_dict["paging"].get("previousPage", ""),
                last_page=optouts_response_dict["paging"].get("lastPage", ""),
                total_count=optouts_response_dict["paging"].get("totalCount", 0),
            )
            return TRecipientOptouts(
                recipient_optouts=([] if optouts is None else optouts),
                paging=paging,
            )
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
            raise exceptions.VirtualNumbersError(
                f"Could not retrieve the list of optout numbers: {exc}"
            ) from exc
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve the list of optout numbers. {suggested_actions_string}"
        ) from exc
