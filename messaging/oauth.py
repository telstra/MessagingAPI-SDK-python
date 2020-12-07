"""Handles OAuth interactions."""

import typing
import dataclasses
from urllib import error
from urllib import request
from urllib import parse
import time
import json
import math

from . import exceptions
from .utils import environment


@dataclasses.dataclass
class TToken:
    """
    OAuth token.

    Attrs:
        access_token: The OAuth access token.
        token_type: The type of the token.
        expires_in: The number of seconds until the token expires.
        retrieved_at: The time when the token was retrieved.

        expired: Whether the token is expired.
        authorization: The value of the Authorization header with the token.

    """

    def __init__(self, access_token: str, token_type: str, expires_in: str):
        """Construct."""
        self.retrieved_at = math.ceil(time.time())
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = int(expires_in)

    # The access token
    access_token: str
    # The type of the token
    token_type: str
    # The time to expiry
    expires_in: int
    # The time it was created
    retrieved_at: int

    @property
    def expired(self):
        """Whether the tokens are expired."""
        return math.ceil(time.time()) >= self.retrieved_at + self.expires_in

    @property
    def authorization(self):
        """Create the value of the Authorization header."""
        return f"Bearer {self.access_token}"


def _reuse_token(func):
    """Decorator to reuse tokens that are not expired."""
    cache = {"old_token": None}

    def _get_token() -> TToken:
        """Decorator."""
        if cache["old_token"] is None or cache["old_token"].expired:
            cache["old_token"] = func()
        return cache["old_token"]

    return _get_token


def _get_token() -> TToken:
    """
    Retrieve the OAuth tokens.

    Returns:
        The oauth tokens.

    """
    url = "https://tapi.telstra.com/v2/oauth/token"
    data = parse.urlencode(
        {
            "grant_type": "client_credentials",
            "client_id": environment.get().client_id,
            "client_secret": environment.get().client_secret,
            "scope": "NSMS",
        }
    ).encode("ascii")
    try:
        with request.urlopen(url, data) as response:
            return TToken(**json.loads(response.read().decode()))
    except error.HTTPError as exc:
        raise exceptions.CredentialError(f"Could not retrieve token: {exc}") from exc


get_token = _reuse_token(_get_token)
