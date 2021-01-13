"""Handles OAuth interactions."""

import dataclasses
import json
import math
import time
from urllib import error, parse, request

from . import exceptions
from .utils import config


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


_CACHE = {"old_token": None}


def _reuse_token(func):
    """Decorate to reuse tokens that are not expired."""

    def inner() -> TToken:
        """Decorator."""
        if _CACHE["old_token"] is None or _CACHE["old_token"].expired:
            _CACHE["old_token"] = func()
        assert _CACHE["old_token"] is not None
        return _CACHE["old_token"]

    return inner


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
            "client_id": config.get().tls_client_key,
            "client_secret": config.get().tls_client_secret,
            "scope": "NSMS",
        }
    ).encode("ascii")
    try:
        with request.urlopen(url, data) as response:
            return TToken(**json.loads(response.read().decode()))
    except error.HTTPError as exc:
        raise exceptions.CredentialError(f"Could not retrieve token: {exc}") from exc


get_token = _reuse_token(_get_token)
