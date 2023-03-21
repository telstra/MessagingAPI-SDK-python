"""Utilities for the schedule send."""

# ISO format example: "2019-08-24T15:39:00Z"
import re
import typing

from .. import exceptions, types


def validate(
    *,
    value: typing.Optional[types.TScheduleSend],
    exception: typing.Type[exceptions.MessagingBaseException],
) -> None:
    """Validate the schedule_send parameter for send."""
    if value is not None:
        is_iso_date_pattern = re.compile(
            r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*)?)(Z)$"
        )
        if not isinstance(value, str):
            raise exception(
                'the value of "schedule_send" is not valid, '
                f'expected a string, received "{value}"'
            )
        if not bool(is_iso_date_pattern.match(value)):
            raise exception(
                'the value of "schedule_send" is not valid, '
                f'it must be ISO format date, received "{value}"'
            )
