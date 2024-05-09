"""Utilities for the callback URL."""

import typing

from .. import exceptions, types


def validate(
    *,
    name: str,
    value: typing.Optional[types.TStatusCallbackUrl],
    exception: typing.Type[exceptions.MessagingBaseException],
) -> None:
    """Validate the callback_url parameter for send."""
    if value is not None:
        if not isinstance(value, str):
            raise exception(
                f'the value of "{name}" is not valid, expected a string, '
                f'received "{value}"'
            )
        if not value.lower().startswith("https"):
            raise exception(
                f'the value of "{name}" is not valid, '
                f'it must start with https, received "{value}"'
            )
