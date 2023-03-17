"""Helper for virtual numbers."""

import dataclasses
import re
import typing


@dataclasses.dataclass
class Result:
    """
    Result of the check.

    Attrs:
        valid: Whether the virtual number is valid.
        reason: If the virtual number is not valid, the reason why.

    """

    valid: bool
    reason: typing.Optional[str]


_PHONE_REGEX = re.compile(r"^(04)\d{8}$")


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

    if not value.startswith("04"):
        return Result(
            valid=False,
            reason=(
                "expecting a virtual number starting with 04 "
                f'followed by 8 digits, received "{value}"'
            ),
        )

    if value.startswith("04") and len(value) != 10:
        return Result(
            valid=False,
            reason=(
                "the virtual number has an incorrect number of characters, "
                f'expecting 10, received "{value}" which has {len(value)} '
                "characters"
            ),
        )

    if _PHONE_REGEX.search(value) is None:
        return Result(
            valid=False,
            reason=(
                "the virtual number contains invalid characters, "
                "expecting a phone number starting with 04 "
                f'followed by 8 digits, received "{value}"'
            ),
        )

    return Result(valid=True, reason=None)
