"""Used to send messages."""

import dataclasses
import json
import re
import typing
from urllib import error, parse, request

from . import exceptions, oauth, types
from .utils import callback_url as callback_url_util
from .utils import error_response as error_response_util
from .utils import free_trial_number
from .utils import message_id as message_id_util
from .utils import querystring
from .utils import schedule_send as schedule_send_iso_date_util

_URL = "https://products.api.telstra.com/messaging/v3/messages"


@dataclasses.dataclass
class Multimedia:
    """Data class for mms content."""

    type: str
    fileName: str
    payload: str


class MultimediaEncoder(json.JSONEncoder):
    """Encoder class for Multimedia class."""

    def default(self, obj):
        """Class default function."""
        if isinstance(obj, Multimedia):
            return obj.__dict__
        # Base class default() raises TypeError:
        return json.JSONEncoder.default(self, obj)


@dataclasses.dataclass
class TMessage:
    """
    A message.

    Attrs:
        message_id: List of unique identifiers for the messages sent.
        to: List of the destination mobile numbers.
        from_: Alphanumeric string.
        message_content: The text content of the message.
        multimedia: Multimedia content of the message.
        retry_timeout: How long the platform should keep attempting to resend
                       a message (in minutes), default is 10 minutes.
        schedule_send: ISO format GMT time string. You can schedule a message
                       up to 10 days into the future.
        delivery_notification: Accepts boolean, to receive a notification when
                               your SMS has been delivered.
        status_callback_url: URL you want the API to call when the status of
                             your SMS updates.
        tags: List of strings used as tags to the message.

    """

    message_id: typing.Union[types.TMessageId, typing.List[types.TMessageId]]
    delivery_status: str
    to: typing.Union[types.TTo, typing.List[types.TTo]]
    from_: types.TFrom
    message_content: types.TMessageContent
    multimedia: Multimedia
    retry_timeout: types.TRetryTimeout
    schedule_send: types.TScheduleSend
    delivery_notification: types.TDeliveryNotification
    status_callback_url: types.TStatusCallbackUrl
    tags: types.TTags
    direction: str | None = None
    queue_priority: int = 2
    create_timestamp: str | None = None
    sent_timestamp: str | None = None
    received_timestamp: str | None = None


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
class TMessages:
    """
    List of messages.

    Attrs:
        messages:
        paging:

    """

    messages: list[TMessage]
    paging: TPaging


_VALID_FROM = re.compile(r"^[a-zA-Z0-9]+$")


def _send_validate_to(to: typing.Union[types.TTo, typing.List[types.TTo]]) -> None:
    """Validate the to parameter for send."""
    if not isinstance(to, str) and not isinstance(to, list):
        raise exceptions.MessageError(
            'the value of "to" is not valid, '
            "expecting a string or a list of string, "
            f'received "{to}"'
        )
    if isinstance(to, str):
        result = free_trial_number.check(value=to)
        if not result.valid:
            raise exceptions.MessageError(
                f'the value of "to" is not valid, {result.reason}'
            )
    if isinstance(to, list):
        first_invalid_result = next(
            filter(lambda result: not result.valid, map(free_trial_number.check, to)),
            None,
        )
        if first_invalid_result is not None:
            raise exceptions.MessageError(
                f'the value of "to" is not valid, {first_invalid_result.reason}'
            )


def _send_validate_from(from_: typing.Optional[types.TFrom]) -> None:
    """Validate the from_ parameter for send."""
    if not isinstance(from_, str):
        raise exceptions.MessageError(
            'the value of "from_" is not valid, expected a string, received '
            f'"{from_}"'
        )
    if len(from_) > 13:
        raise exceptions.MessageError(
            'the value of "from_" has too many characters, expected at most 13'
            f' characters, received "{from_}"'
        )
    if not _VALID_FROM.search(from_):
        raise exceptions.MessageError(
            'the value of "from_" contains invalid characters, expected alpha '
            f'numeric characters, received "{from_}"'
        )


def _validate_send_args(  # pylint: disable=too-many-arguments
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    from_: typing.Optional[types.TFrom],
    message_content: typing.Optional[types.TMessageContent],
    multimedia: typing.Optional[Multimedia],
    retry_timeout: typing.Optional[types.TRetryTimeout],
    schedule_send: typing.Optional[types.TScheduleSend],
    delivery_notification: typing.Optional[types.TDeliveryNotification],
    status_callback_url: typing.Optional[types.TStatusCallbackUrl],
    tags: typing.Optional[typing.List[types.TTags]],
) -> None:
    """Validate the arguments for send."""
    # Validate to
    _send_validate_to(to)
    # Validate from_
    _send_validate_from(from_)
    # Validate message_content & multimedia
    if (message_content is not None and not isinstance(message_content, str)) or (
        message_content is not None and len(message_content) > 1600
    ):
        raise exceptions.MessageError(
            'the value of "message_content" is not valid, expected a string '
            f'with maximum 1600 characters, received "{message_content}"'
        )
    if (multimedia is not None and not isinstance(multimedia, list)) or (
        multimedia is not None and len(multimedia) > 5
    ):
        raise exceptions.MessageError(
            'the value of "multimedia" is not valid, expected list with '
            f'maximum 5 multimedia, received "{multimedia}"'
        )
    if message_content is None and multimedia is None:
        raise exceptions.MessageError(
            'a value of "messageContent" or "multimedia" must be supplied, '
            f'received message_content: "{message_content}" '
            f'multimedia: "{multimedia}"'
        )

    # Validate retry_timeout
    if retry_timeout is not None and not isinstance(retry_timeout, int):
        raise exceptions.MessageError(
            'the value of "retry_timeout" is not valid, expected an integer, '
            f'received "{retry_timeout}"'
        )
    # Validate schedule_send
    schedule_send_iso_date_util.validate(
        value=schedule_send, exception=exceptions.MessageError
    )
    # Validate delivery_notification
    if delivery_notification is not None and not isinstance(
        delivery_notification, bool
    ):
        raise exceptions.MessageError(
            'the value of "delivery_notification" is not valid, '
            f'expected a bool, received "{delivery_notification}"'
        )

    # Validate status_callback_url
    callback_url_util.validate(
        name="status_callback_url",
        value=status_callback_url,
        exception=exceptions.MessageError,
    )
    # Validate tags
    if (tags is not None and not isinstance(tags, list)) or (
        tags is not None
        and isinstance(tags, list)
        and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.MessageError(
            'the value of "tags" is not valid, expected a list of strings '
            f'with alteast one tag or a maximum of 10, received "{tags}"'
        )


def send(  # pylint: disable=too-many-arguments,too-many-locals
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    from_: typing.Optional[types.TFrom] = None,
    message_content: typing.Optional[types.TMessageContent] = None,
    multimedia: typing.Optional[Multimedia] = None,
    retry_timeout: typing.Optional[types.TRetryTimeout] = None,
    schedule_send: typing.Optional[types.TScheduleSend] = None,
    delivery_notification: typing.Optional[types.TDeliveryNotification] = None,
    status_callback_url: typing.Optional[types.TStatusCallbackUrl] = None,
    tags: typing.Optional[typing.List[types.TTags]] = None,
) -> TMessage:
    """
    Send a message.

    Raises MessageError is anything goes wrong whilst sending a message.

    Args:
        to: The destination mobile number.
        from: You can choose whether they'll see a privateNumber,
            virtualNumber or senderName (paid plans only) in the from field.
        message_content: The text content of the message.
            Use this field to send an SMS.
        multimedia: Multimedia content of the message.
            Use this field to send an MMS.
        retry_timeout: How long the platform should keep attempting to resend
            a message (in minutes), default is 10 minutes.
        schedule_send: ISO format GMT time string. You can schedule a
            message up to 10 days into the future.
        delivery_notification: Accepts boolean, to receive a notification
            when your SMS has been delivered.
        status_callback_url: URL you want the API to call when the status
            of your SMS updates.
        tags: List of strings used as tags to the message.

    Returns:
        The message that was sent.

    """
    _validate_send_args(
        to=to,
        from_=from_,
        message_content=message_content,
        multimedia=multimedia,
        retry_timeout=retry_timeout,
        schedule_send=schedule_send,
        delivery_notification=delivery_notification,
        status_callback_url=status_callback_url,
        tags=tags,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {"to": to, "from": from_}
    if message_content is not None:
        data["messageContent"] = message_content
    if multimedia is not None:
        multimedia = json.loads(json.dumps(multimedia, cls=MultimediaEncoder))
        data["multimedia"] = multimedia
    if retry_timeout is not None:
        data["retryTimeout"] = retry_timeout
    if schedule_send is not None:
        data["scheduleSend"] = schedule_send
    if delivery_notification is not None:
        data["deliveryNotification"] = delivery_notification
    if status_callback_url is not None:
        data["statusCallbackUrl"] = status_callback_url
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
    }
    message_request = request.Request(
        f"{_URL}",
        data=data_str,
        headers=headers,
        method="POST",
    )
    try:
        with request.urlopen(message_request) as response:
            message_dict = json.loads(response.read().decode())

            return TMessage(
                message_id=message_dict.get("messageId"),
                to=message_dict.get("to"),
                from_=message_dict.get("from"),
                delivery_status=message_dict.get("status", None),
                message_content=message_dict.get("messageContent", None),
                multimedia=message_dict.get("multimedia", None),
                retry_timeout=message_dict.get("retryTimeout", None),
                schedule_send=message_dict.get("scheduleSend", None),
                delivery_notification=message_dict.get("deliveryNotification", None),
                status_callback_url=message_dict.get("statusCallbackUrl", None),
                tags=message_dict.get("tags", None),
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
            raise exceptions.MessageError(f"Could not send message: {exc}") from exc
        raise exceptions.MessageError(
            f"Could not send message. {suggested_actions_string}"
        ) from exc


def _validate_update_args(  # pylint: disable=too-many-arguments
    message_id: typing.Optional[types.TMessageId],
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    from_: typing.Optional[types.TFrom],
    message_content: typing.Optional[types.TMessageContent],
    multimedia: typing.Optional[Multimedia],
    retry_timeout: typing.Optional[types.TRetryTimeout],
    schedule_send: typing.Optional[types.TScheduleSend],
    delivery_notification: typing.Optional[types.TDeliveryNotification],
    status_callback_url: typing.Optional[types.TStatusCallbackUrl],
    tags: typing.Optional[typing.List[types.TTags]],
) -> None:
    """Validate the arguments for send."""
    message_id_util.validate(value=message_id, exception=exceptions.MessageError)

    _validate_send_args(
        to=to,
        from_=from_,
        message_content=message_content,
        multimedia=multimedia,
        retry_timeout=retry_timeout,
        schedule_send=schedule_send,
        delivery_notification=delivery_notification,
        status_callback_url=status_callback_url,
        tags=tags,
    )


def update(  # pylint: disable=too-many-arguments,too-many-locals
    message_id: types.TMessageId,
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    from_: typing.Optional[types.TFrom] = None,
    message_content: typing.Optional[types.TMessageContent] = None,
    multimedia: typing.Optional[Multimedia] = None,
    retry_timeout: typing.Optional[types.TRetryTimeout] = None,
    schedule_send: typing.Optional[types.TScheduleSend] = None,
    delivery_notification: typing.Optional[types.TDeliveryNotification] = None,
    status_callback_url: typing.Optional[types.TStatusCallbackUrl] = None,
    tags: typing.Optional[typing.List[types.TTags]] = None,
) -> TMessage:
    """
    Update a message.

    Raises MessageError is anything goes wrong whilst updating a message.

    Args:
        message_id: Unique identifier for the message.
        to: The destination mobile number.
        from: You can choose whether they'll see a privateNumber,
            virtualNumber or senderName (paid plans only) in the from field.
        message_content: The text content of the message.
            Use this field to send an SMS.
        multimedia: Multimedia content of the message.
            Use this field to send an MMS.
        retry_timeout: How long the platform should keep attempting to resend
            a message (in minutes), default is 10 minutes.
        schedule_send: ISO format GMT time string. You can schedule a message
            up to 10 days into the future.
        delivery_notification: Accepts boolean, to receive a notification when
            your SMS has been delivered.
        status_callback_url: URL you want the API to call when the status
            of your SMS updates.
        tags: List of strings used as tags to the message.

    Returns:
        The message that was sent.

    """
    _validate_update_args(
        message_id=message_id,
        to=to,
        from_=from_,
        message_content=message_content,
        multimedia=multimedia,
        retry_timeout=retry_timeout,
        schedule_send=schedule_send,
        delivery_notification=delivery_notification,
        status_callback_url=status_callback_url,
        tags=tags,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {"to": to, "from": from_}
    if message_content is not None:
        data["messageContent"] = message_content
    if multimedia is not None:
        multimedia = json.loads(json.dumps(multimedia, cls=MultimediaEncoder))
        data["multimedia"] = multimedia
    if retry_timeout is not None:
        data["retryTimeout"] = retry_timeout
    if schedule_send is not None:
        data["scheduleSend"] = schedule_send
    if delivery_notification is not None:
        data["deliveryNotification"] = delivery_notification
    if status_callback_url is not None:
        data["statusCallbackUrl"] = status_callback_url
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
    }
    message_request = request.Request(
        f"{_URL}/{parse.quote(message_id)}",
        data=data_str,
        headers=headers,
        method="PUT",
    )
    try:
        with request.urlopen(message_request) as response:
            message_dict = json.loads(response.read().decode())
            return TMessage(
                message_id=message_dict.get("messageId"),
                to=message_dict.get("to"),
                from_=message_dict.get("from"),
                delivery_status=message_dict.get("status", None),
                message_content=message_dict.get("messageContent", None),
                multimedia=message_dict.get("multimedia", None),
                retry_timeout=message_dict.get("retryTimeout", None),
                schedule_send=message_dict.get("scheduleSend", None),
                delivery_notification=message_dict.get("deliveryNotification", None),
                status_callback_url=message_dict.get("statusCallbackUrl", None),
                queue_priority=message_dict.get("queuePriority", None),
                tags=message_dict.get("tags", None),
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
            raise exceptions.MessageError(f"Could not update message: {exc}") from exc
        raise exceptions.MessageError(
            f"Could not update message. {suggested_actions_string}"
        ) from exc


def _validate_update_tags_args(  # pylint: disable=too-many-arguments
    message_id: typing.Optional[types.TMessageId],
    tags: typing.Optional[typing.List[types.TTags]],
) -> None:
    """Validate the arguments for update_tags."""
    message_id_util.validate(value=message_id, exception=exceptions.MessageError)

    # Validate tags
    if (not isinstance(tags, list)) or (
        isinstance(tags, list) and (len(tags) < 1 or len(tags) > 10)
    ):
        raise exceptions.MessageError(
            'the value of "tags" is not valid, expected a list of strings '
            f'with alteast one tag or a maximum of 10, received "{tags}"'
        )


def update_tags(  # pylint: disable=too-many-arguments,too-many-locals
    message_id: types.TMessageId,
    tags: typing.Optional[typing.List[types.TTags]],
) -> None:
    """
    Update a message tags.

    Raises MessageError is anything goes wrong whilst updating a message tags.

    Args:
        message_id: Unique identifier for the message.
        tags: List of strings used as tags to the message.

    Returns:
        None

    """
    _validate_update_tags_args(
        message_id=message_id,
        tags=tags,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    data: typing.Dict[str, typing.Any] = {"tags": tags}
    data_str = json.dumps(data).encode()
    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    update_tags_request = request.Request(
        f"{_URL}/{parse.quote(message_id)}",
        data=data_str,
        headers=headers,
        method="PATCH",
    )
    try:
        with request.urlopen(update_tags_request):
            return None
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
            raise exceptions.MessageError(
                f"Could not update message tags: {exc}"
            ) from exc
        raise exceptions.MessageError(
            f"Could not update message tags. {suggested_actions_string}"
        ) from exc


def get(message_id: types.TMessageId) -> TMessage:
    """
    Retrieve the status of a message.

    Raises MessageError is anything goes wrong whilst retrieving the status.

    Args:
        message_id: Unique identifier for the message.

    Returns:
        The status of the message.

    """

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
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
    message_get_request = request.Request(
        f"{_URL}/{parse.quote(message_id)}",
        headers=headers,
        method="GET",
    )
    try:
        with request.urlopen(message_get_request) as response:
            message_get_dict = json.loads(response.read().decode())
            return TMessage(
                message_id=message_get_dict.get("messageId"),
                to=message_get_dict.get("to"),
                from_=message_get_dict.get("from"),
                delivery_status=message_get_dict.get("status", None),
                message_content=message_get_dict.get("messageContent", None),
                multimedia=message_get_dict.get("multimedia", None),
                retry_timeout=message_get_dict.get("retryTimeout", None),
                schedule_send=message_get_dict.get("scheduleSend", None),
                delivery_notification=message_get_dict.get(
                    "deliveryNotification", None
                ),
                status_callback_url=message_get_dict.get("statusCallbackUrl", None),
                tags=message_get_dict.get("tags", None),
                queue_priority=message_get_dict.get("queuePriority", None),
                direction=message_get_dict.get("direction", None),
                create_timestamp=message_get_dict.get("createTimestamp", None),
                sent_timestamp=message_get_dict.get("sentTimestamp", None),
                received_timestamp=message_get_dict.get("receivedTimestamp", None),
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
            raise exceptions.MessageError(
                f"Could not retrieve the message: {exc}"
            ) from exc
        raise exceptions.MessageError(
            f"Could not retrieve the message. {suggested_actions_string}"
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
        raise exceptions.MessageError(
            'the value of "limit" is not valid, expected a int value between '
            f'1 and 50, received "{limit}"'
        )

    # Validate offset
    if (offset is not None and not isinstance(offset, types.TOffset)) or (
        offset is not None
        and isinstance(offset, types.TOffset)
        and (offset < 0 or offset > 999999)
    ):
        raise exceptions.MessageError(
            'the value of "offset" is not valid, expected a int value '
            f'between 0 and 999999, received "{offset}"'
        )

    # Validate filter
    if filter_ is not None and not isinstance(filter_, types.TFilter):
        raise exceptions.MessageError(
            'the value of "filter" is not valid, expected a string, '
            f'received "{filter_}"'
        )


def get_all(
    limit: typing.Optional[types.TLimit] = None,
    offset: typing.Optional[types.TOffset] = None,
    filter_: typing.Optional[types.TFilter] = None,
) -> TMessages:
    """
    Retrieve all messages.

    Raises MessageError is anything goes wrong whilst retrieving messages.

    Returns:
        List of messages.

    """

    _validate_get_all_args(limit=limit, offset=offset, filter_=filter_)

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
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
    messages_get_request = request.Request(
        f"{_URL}{querystring.build(limit=limit, offset=offset, filter_=filter_)}",
        headers=headers,
        method="GET",
    )
    try:
        with request.urlopen(messages_get_request) as response:
            messages: list[TMessage] = []
            messages_response_dict = json.loads(response.read().decode())
            messages_list = messages_response_dict.get("messages", [])
            if messages_list is not None and len(messages_list) > 0:
                messages = [
                    TMessage(
                        message_id=d.get("messageId"),
                        to=d.get("to"),
                        from_=d.get("from"),
                        delivery_status=d.get("status", None),
                        message_content=d.get("messageContent", None),
                        multimedia=d.get("multimedia", None),
                        retry_timeout=d.get("retryTimeout", None),
                        schedule_send=d.get("scheduleSend", None),
                        delivery_notification=d.get("deliveryNotification", None),
                        status_callback_url=d.get("statusCallbackUrl", None),
                        tags=d.get("tags", None),
                        queue_priority=d.get("queuePriority", None),
                        direction=d.get("direction", None),
                        create_timestamp=d.get("createTimestamp", None),
                        sent_timestamp=d.get("sentTimestamp", None),
                        received_timestamp=d.get("receivedTimestamp", None),
                    )
                    for d in messages_list
                ]
            paging = TPaging(
                next_page=messages_response_dict["paging"].get("nextPage", ""),
                previous_page=messages_response_dict["paging"].get("previousPage", ""),
                last_page=messages_response_dict["paging"].get("lastPage", ""),
                total_count=messages_response_dict["paging"].get("totalCount", 0),
            )
            return TMessages(
                messages=[] if messages is None else messages,
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
            raise exceptions.MessageError(
                f"Could not retrieve messages: {exc}"
            ) from exc
        raise exceptions.MessageError(
            f"Could not retrieve messages. {suggested_actions_string}"
        ) from exc


def delete(message_id: types.TMessageId) -> None:
    """
    Delete a message that's been scheduled for sending, but hasn't yet sent.

    Raises MessageError is anything goes wrong whilst deleting the message.

    Args:
        message_id: Unique identifier for the message.

    Returns:
        None.

    """

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.MessageError(
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
    delete_request = request.Request(
        f"{_URL}/{parse.quote(message_id)}",
        headers=headers,
        method="DELETE",
    )
    try:
        with request.urlopen(delete_request):
            return None
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
            raise exceptions.MessageError(
                f"Could not delete the message: {exc}"
            ) from exc
        raise exceptions.MessageError(
            f"Could not delete the message. {suggested_actions_string}"
        ) from exc
