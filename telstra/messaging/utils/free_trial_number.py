"""Helper for free trial numbers."""

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


_PHONE_REGEX = re.compile(r"^(?:\+61|0)4\d{8}$|^\+\d{1,3}\d{4,14}$")


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

    if value.startswith("+614") and len(value) != 12:
        return Result(
            valid=False,
            reason=(
                "the phone number has an incorrect number of characters, "
                f'expecting 12, received "{value}" which has {len(value)} '
                "characters"
            ),
        )

    if value.startswith("04") and len(value) != 10:
        return Result(
            valid=False,
            reason=(
                "the phone number has an incorrect number of characters, "
                f'expecting 10, received "{value}" which has {len(value)} '
                "characters"
            ),
        )

    if _PHONE_REGEX.search(value) is None:
        return Result(
            valid=False,
            reason=(
                "the phone number contains invalid characters, " f'received "{value}"'
            ),
        )

    return Result(valid=True, reason=None)
