"""Handles OAuth interactions."""

import dataclasses
from urllib import request
from urllib import parse
import time
import json
import math

from .utils import environment


@dataclasses.dataclass
class TToken:
    """OAuth token."""

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
        return time.time() >= self.retrieved_at + self.expires_in


def get_token() -> TToken:
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
    with request.urlopen(url, data) as response:
        return TToken(**json.loads(response.read().decode()))
