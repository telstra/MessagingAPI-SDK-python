"""Handle numbers."""

import dataclasses
import json
import ssl
import typing
from urllib import error, request, parse

from . import exceptions, oauth, types
from .utils import callback_url as callback_url_util
from .utils import querystring

_URL = "https://products.api.telstra.com/messaging/v3/virtual-numbers"  # "https://qa.org005.t-dev.telstra.net/messaging/v3/virtual-numbers"
# gcontext = (
#     ssl._create_unverified_context()
# )  ## TODO Remove this line, only for NP to circumvent certificate issue


@dataclasses.dataclass
class TVirtualNumber:
    """
    A virtual phone number.

    Attrs:
        reply_callback_url: URL that replies to the Virtual Number should be sent to.
        tags: List of strings used as tags to the virtual number.

    """

    virtual_number: str
    last_use: str
    reply_callback_url: types.TStatusCallbackUrl = None
    tags: types.TTags = None


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


def assign(
    reply_callback_url: typing.Optional[types.TStatusCallbackUrl] = None,
    tags: typing.Optional[typing.List[types.TTags]] = None,
) -> TVirtualNumber:
    """
    Assign a virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    Args:
        reply_callback_url: URL that replies to the Virtual Number should be sent to.
        tags: List of strings used as tags to the virtual number.

    """
    # Validate tags
    if (tags is not None and not isinstance(tags, list)) or (
        tags is not None
        and isinstance(tags, list)
        and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.MessageError(
            'the value of "tags" is not valid, expected a list of strings with alteast one tag or a maximum of 10, '
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
        "Telstra-api-version": "3.1.0",
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
        raise exceptions.VirtualNumbersError(
            f"Could not assign virtual number: {exc}"
        ) from exc


def _validate_get_all_args(
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
    filter: typing.Optional[types.TFilter] = None,
) -> None:
    # Validate limit
    if (limit is not None and not isinstance(limit, types.TLimit)) or (
        limit is not None
        and isinstance(limit, types.TLimit)
        and (limit < 1 or limit > 50)
    ):
        raise exceptions.MessageError(
            'the value of "limit" is not valid, expected a int value between 1 and 50, '
            f'received "{limit}"'
        )

    # Validate offset
    if (offset is not None and not isinstance(offset, types.TOffset)) or (
        offset is not None
        and isinstance(offset, types.TOffset)
        and (offset < 0 or limit > 999999)
    ):
        raise exceptions.MessageError(
            'the value of "offset" is not valid, expected a int value between 0 and 999999, '
            f'received "{offset}"'
        )

    # Validate filter
    if filter is not None and not isinstance(filter, types.TFilter):
        raise exceptions.MessageError(
            'the value of "filter" is not valid, expected a string, '
            f'received "{filter}"'
        )


def get_all(
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
    filter: typing.Optional[types.TFilter] = None,
) -> TVirtualNumbers:
    """
    Retrieve all virtual numbers assigned to you.

    Raises VirtualNumbersError if anything goes wrong.

    """

    _validate_get_all_args(limit=limit, offset=offset, filter=filter)

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.1.0",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
    }
    virtual_numbers_request = request.Request(
        f"{_URL}{querystring.build(limit=limit, offset=offset, filter=filter)}",
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

            if virtual_numbers_list is not None and len(virtual_numbers_list) > 1:
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
                virtual_numbers=[] if virtual_numbers is None else virtual_numbers,
                paging=paging,
            )
    except error.HTTPError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve virtual number: {exc}"
        ) from exc


def get(virtual_number: str) -> TVirtualNumber:
    """
    Retrieve virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.1.0",
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
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve virtual number: {exc}"
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
        reply_callback_url: URL that replies to the Virtual Number should be sent to.
        tags: List of strings used as tags to the virtual number.

    """
    # Validate tags
    if (tags is not None and not isinstance(tags, list)) or (
        tags is not None
        and isinstance(tags, list)
        and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.MessageError(
            'the value of "tags" is not valid, expected a list of strings with alteast one tag or a maximum of 10, '
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
        "Telstra-api-version": "3.1.0",
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
        raise exceptions.VirtualNumbersError(
            f"Could not update virtual number: {exc}"
        ) from exc


def delete(virtual_number: str) -> None:
    """
    Delete virtual number.

    Raises VirtualNumbersError if anything goes wrong.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
        "Cache-Control": "no-cache",
    }
    numbers_request = request.Request(
        f"{_URL}/{parse.quote(virtual_number)}", headers=headers, method="DELETE"
    )
    try:
        with request.urlopen(numbers_request):
            return
    except error.HTTPError as exc:
        raise exceptions.VirtualNumbersError(
            f"Could not delete virtual number: {exc}"
        ) from exc
