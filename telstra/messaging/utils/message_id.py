"""Utilities for the message id."""

import typing
import uuid

from .. import exceptions, types


def _is_valid_uuid_v1(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str and uuid_obj.version == 1
    except ValueError:
        return False


def validate(
    *,
    value: typing.Optional[types.TMessageId],
    exception: typing.Type[exceptions.MessagingBaseException],
) -> None:
    """Validate the message_id parameter for send."""
    if value is not None:
        if not isinstance(value, str):
            raise exception(
                'the value of "message_id" is not valid, expected a '
                f'uuid format string, received "{value}"'
            )
        if not _is_valid_uuid_v1(value):
            raise exception(
                'the value of "message_id" is not valid, it must be '
                f'uuid of type v1, received "{value}"'
            )
