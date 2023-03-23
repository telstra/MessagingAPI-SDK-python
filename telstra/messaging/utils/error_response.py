"""Messaging V3 error processor."""

import dataclasses


@dataclasses.dataclass
class TMessagingError:
    """
    MessagingError.

    Attrs:
        code:
        issue:
        value:
        suggested_action:

    """

    code: str
    issue: str
    value: str
    suggested_action: str


def process_errors(errors_dict) -> list[TMessagingError]:
    """Process messaging error response."""

    messaging_errors: list[TMessagingError] = []
    errors_list = errors_dict.get("errors", [])
    if errors_list is not None and len(errors_list) > 0:
        messaging_errors = [
            TMessagingError(
                code=d.get("code", None),
                issue=d.get("issue", None),
                value=d.get("tags", None),
                suggested_action=d.get("suggested_action"),
            )
            for d in errors_list
        ]
    return messaging_errors


def get_suggeted_actions_list_str(list_of_error_dicts, key) -> str:
    """Generate suggested_actions string."""

    suggested_actions = ""
    num_values = 0
    for dictionary in list_of_error_dicts:
        if key in dictionary:
            suggested_actions += dictionary[key] + "\n"
            num_values += 1
    if num_values > 1:
        suggested_actions = suggested_actions.rstrip("\n")
    return suggested_actions
