"""Helper for phone numbers."""

import dataclasses
import re
import typing


@dataclasses.dataclass
class Result:
    """
    Result of the check.

    Attrs:
        valid: Whether the phone number is valid.
        reason: If the phone number is not valid, the reason why.

    """

    valid: bool
    reason: typing.Optional[str]


_PHONE_REGEX = re.compile(r"^((\+614)|(04))\d{8}$")


def check(value: str) -> Result:
    """
    Check whether a phone number is valid.

    Args:
        value: The phone number to check.

    Returns:
        Whether the phone number is valid.

    """
    if not isinstance(value, str):
        return Result(valid=False, reason=f'expecting a string, received "{value}"')

    if not value.startswith("+614") and not value.startswith("04"):
        return Result(
            valid=False,
            reason=(
                "expecting a phone number starting with +614 or 04 followed by 8 "
                f'digits, received "{value}"'
            ),
        )

    if value.startswith("+614") and len(value) != 12:
        return Result(
            valid=False,
            reason=(
                "the phone number has an incorrect number of characters, expecting "
                f'12, received "{value}" which has {len(value)} characters'
            ),
        )

    if value.startswith("04") and len(value) != 10:
        return Result(
            valid=False,
            reason=(
                "the phone number has an incorrect number of characters, expecting "
                f'10, received "{value}" which has {len(value)} characters'
            ),
        )

    if _PHONE_REGEX.search(value) is None:
        return Result(
            valid=False,
            reason=(
                "the phone number contains invalid characters, expecting  a phone "
                "number starting with +614 or 04 followed by 8 digits, received "
                f'"{value}"'
            ),
        )

    return Result(valid=True, reason=None)
