"""Utilities for the querystring."""

from urllib.parse import urlencode


def build(**kwargs) -> str:
    """Build a querystring."""
    params = kwargs.get("params")
    if params:
        query_dict = eval(params)
    else:
        query_dict = {
            k: "true" if v is True else "false" if v is False else v
            for k, v in kwargs.items()
            if v is not None
        }
    query_string = urlencode(query_dict)
    if query_string:
        return f"?{query_string}"
    return ""
