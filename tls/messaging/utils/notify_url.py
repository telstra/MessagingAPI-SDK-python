"""Utilities for the notify URL."""

import typing

from .. import exceptions, types


def validate(
    *,
    value: typing.Optional[types.TNotifyUrl],
    exception: typing.Type[exceptions.MessagingBaseException],
) -> None:
    """Validate the notify_url parameter for send."""
    if value is not None:
        if not isinstance(value, str):
            raise exception(
                'the value of "notify_url" is not valid, expected a string, received '
                f'"{value}"'
            )
        if not value.lower().startswith("https"):
            raise exception(
                'the value of "notify_url" is not valid, it must start with https, '
                f'received "{value}"'
            )
