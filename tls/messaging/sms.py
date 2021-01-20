"""Used to send messages."""

import dataclasses
import json
import re
import typing
from urllib import error, parse, request

from tls.messaging.utils import notify_url as notify_url_util
from tls.messaging.utils import phone_number

from . import exceptions, oauth, types
from .utils import phone_number

_URL = "https://tapi.telstra.com/v2/messages/sms"


@dataclasses.dataclass
class TSms:
    """
    A sms.

    Attrs:
        to: The destination mobile number.
        delivery_status: Whether the delivery has been completed.
        message_id: Unique identifier for the message.
        message_status_url: URL to retrieve the current delivery status.

    """

    to: typing.Union[types.TTo, typing.List[types.TTo]]
    delivery_status: str
    message_id: types.TMessageId
    message_status_url: str


_VALID_FROM = re.compile(r"^[a-zA-Z0-9]+$")


def _send_validate_to(to: typing.Union[types.TTo, typing.List[types.TTo]]) -> None:
    """Validate the to parameter for send."""
    if not isinstance(to, str) and not isinstance(to, list):
        raise exceptions.SmsError(
            f'the value of "to" is not valid, expecting a string or a list of string, '
            f'received "{to}"'
        )
    if isinstance(to, str):
        result = phone_number.check(value=to)
        if not result.valid:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {result.reason}'
            )
    if isinstance(to, list):
        first_invalid_result = next(
            filter(lambda result: not result.valid, map(phone_number.check, to)),
            None,
        )
        if first_invalid_result is not None:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {first_invalid_result.reason}'
            )


def _send_validate_from(from_: typing.Optional[types.TFrom]) -> None:
    """Validate the from_ parameter for send."""
    if from_ is not None:
        if not isinstance(from_, str):
            raise exceptions.SmsError(
                'the value of "from_" is not valid, expected a string, received '
                f'"{from_}"'
            )
        if len(from_) > 11:
            raise exceptions.SmsError(
                'the value of "from_" has too many characters, expected at most 11 '
                f'characters, received "{from_}"'
            )
        if not _VALID_FROM.search(from_):
            raise exceptions.SmsError(
                'the value of "from_" contains invalid characters, expected alpha '
                f'numeric characters, received "{from_}"'
            )
        result = phone_number.check(value=from_)
        if result.valid:
            raise exceptions.SmsError(
                'the value of "from_" is a phone number, expected alpha '
                f'numeric characters that are not phone numbers, received "{from_}"'
            )


def _validate_send_args(  # pylint: disable=too-many-arguments
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    body: types.TBody,
    from_: typing.Optional[types.TFrom],
    validity: typing.Optional[types.TValidity],
    scheduled_delivery: typing.Optional[types.TScheduledDelivery],
    notify_url: typing.Optional[types.TNotifyUrl],
    priority: typing.Optional[types.TPriority],
    reply_request: typing.Optional[types.TReplyRequest],
    receipt_off: typing.Optional[types.TReceiptOff],
    user_msg_ref: typing.Optional[types.TUsrMsgRef],
) -> None:
    """Validate the arguments for send."""
    # Validate to
    _send_validate_to(to)
    # Validate body
    if not isinstance(body, str):
        raise exceptions.SmsError(
            f'the value of "body" is not valid, expected a string, received "{body}"'
        )
    # Validate from_
    _send_validate_from(from_)
    # Validate validity
    if validity is not None and (
        not isinstance(validity, int) or isinstance(validity, bool)
    ):
        raise exceptions.SmsError(
            'the value of "validity" is not valid, expected an integer, received '
            f'"{validity}"'
        )
    # Validate scheduled_delivery
    if scheduled_delivery is not None and (
        not isinstance(scheduled_delivery, int) or isinstance(scheduled_delivery, bool)
    ):
        raise exceptions.SmsError(
            'the value of "scheduled_delivery" is not valid, expected an integer, '
            f'received "{scheduled_delivery}"'
        )
    # Validate notify_url
    notify_url_util.validate(value=notify_url, exception=exceptions.SmsError)
    # Validate priority
    if priority is not None and not isinstance(priority, bool):
        raise exceptions.SmsError(
            'the value of "priority" is not valid, expected an boolean, '
            f'received "{priority}"'
        )
    # Validate reply_request
    if reply_request is not None and not isinstance(reply_request, bool):
        raise exceptions.SmsError(
            'the value of "reply_request" is not valid, expected an boolean, '
            f'received "{reply_request}"'
        )
    # Validate receipt_off
    if receipt_off is not None and not isinstance(receipt_off, bool):
        raise exceptions.SmsError(
            'the value of "receipt_off" is not valid, expected an boolean, '
            f'received "{receipt_off}"'
        )
    # Validate user_msg_ref
    if user_msg_ref is not None and not isinstance(user_msg_ref, str):
        raise exceptions.SmsError(
            'the value of "user_msg_ref" is not valid, expected an string, '
            f'received "{user_msg_ref}"'
        )


def send(  # pylint: disable=too-many-arguments,too-many-locals
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    body: types.TBody,
    from_: typing.Optional[types.TFrom] = None,
    validity: typing.Optional[types.TValidity] = None,
    scheduled_delivery: typing.Optional[types.TScheduledDelivery] = None,
    notify_url: typing.Optional[types.TNotifyUrl] = None,
    reply_request: typing.Optional[types.TReplyRequest] = None,
    priority: typing.Optional[types.TPriority] = None,
    receipt_off: typing.Optional[types.TReceiptOff] = None,
    user_msg_ref: typing.Optional[types.TUsrMsgRef] = None,
) -> TSms:
    """
    Send an SMS.

    Raises SmsError is anything goes wrong whilst sending a message.

    Args:
        to: The destination mobile number.
        body: The body of the message.
        from: Alpha numeric sender identity.
        validity: How long the platform should attempt to deliver the message for
            (in minutes).
        scheduled_delivery: How long the platform should wait before attempting to send
            the message (in minutes).
        notify_url: Contains a URL that will be called once your message has been
            processed.
        priority: Message will be placed ahead of all messages with a normal priority.
        reply_request: If set to true, the reply message functionality will be
            implemented.
        receipt_off: Whether Delivery Receipt will be sent back or not.
        user_msg_ref: Optional field used by some clients for custom reporting.

    Returns:
        The message that was sent.

    """
    _validate_send_args(
        to=to,
        body=body,
        from_=from_,
        validity=validity,
        scheduled_delivery=scheduled_delivery,
        notify_url=notify_url,
        priority=priority,
        reply_request=reply_request,
        receipt_off=receipt_off,
        user_msg_ref=user_msg_ref,
    )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

    data: typing.Dict[str, typing.Any] = {"to": to, "body": body}
    if from_ is not None:
        data["from"] = from_
    if validity is not None:
        data["validity"] = validity
    if scheduled_delivery is not None:
        data["scheduledDelivery"] = scheduled_delivery
    if notify_url is not None:
        data["notifyURL"] = notify_url
    if priority is not None:
        data["priority"] = priority
    if reply_request is not None:
        data["replyRequest"] = reply_request
    if receipt_off is not None:
        data["receiptOff"] = receipt_off
    if user_msg_ref is not None:
        data["userMsgRef"] = user_msg_ref
    data_str = json.dumps(data).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(_URL, data=data_str, headers=headers, method="POST")
    try:
        with request.urlopen(sms_request) as response:
            sms_dict = json.loads(response.read().decode())
            return TSms(
                to=sms_dict["messages"][0]["to"],
                delivery_status=sms_dict["messages"][0]["deliveryStatus"],
                message_id=sms_dict["messages"][0]["messageId"],
                message_status_url=sms_dict["messages"][0]["messageStatusURL"],
            )
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not send SMS: {exc}") from exc


@dataclasses.dataclass
class TReply:
    """
    A reply.

    Attrs:
        destination_address: Where the message is delivered to.
        sender_address: Who the message is from.
        status: Whether the delivery has been completed.
        message: The body of the message.
        message_id: Unique identifier for the message.
        sent_timestamp: When the message was sent.

    """

    destination_address: str
    sender_address: str
    status: str
    message: str
    message_id: types.TMessageId
    sent_timestamp: types.TSentTimestamp


def get_next_unread_reply() -> typing.Optional[TReply]:
    """
    Get the next unread reply that have been received.

    Raises SmsError is anything goes wrong whilst retrieving the reply.

    Returns:
        The next unread reply or None if there are no more replies.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

    headers = {"Authorization": token.authorization}
    reply_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(reply_request) as response:
            reply_dict = json.loads(response.read().decode())
            try:
                return TReply(
                    status=reply_dict["status"],
                    destination_address=reply_dict["destinationAddress"],
                    sender_address=reply_dict["senderAddress"],
                    message_id=reply_dict["messageId"],
                    message=reply_dict["message"],
                    sent_timestamp=reply_dict["sentTimestamp"],
                )
            except KeyError:
                return None
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not send SMS: {exc}") from exc


@dataclasses.dataclass
class TStatus:
    """
    The status of a message.

    Attrs:
        to: Where the message is delivered to.
        delivery_status: Whether the delivery has been completed.
        received_timestamp: When the message was received.
        sent_timestamp: When the message was sent.

    """

    to: types.TTo
    sent_timestamp: types.TSentTimestamp
    received_timestamp: str
    delivery_status: str


def get_status(message_id: types.TMessageId) -> TStatus:
    """
    Retrieve the status of a message.

    Raises SmsError is anything goes wrong whilst retrieving the status.

    Args:
        message_id: Unique identifier for the message.

    Returns:
        The status of the message.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

    headers = {"Authorization": token.authorization, "Content-Type": "application/json"}
    status_request = request.Request(
        f"{_URL}/{parse.quote(message_id)}/status", headers=headers, method="GET"
    )
    try:
        with request.urlopen(status_request) as response:
            status_dict = json.loads(response.read().decode())
            return TStatus(
                to=status_dict[0]["to"],
                sent_timestamp=status_dict[0]["sentTimestamp"],
                received_timestamp=status_dict[0]["receivedTimestamp"],
                delivery_status=status_dict[0]["deliveryStatus"],
            )
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not retrieve the status: {exc}") from exc
