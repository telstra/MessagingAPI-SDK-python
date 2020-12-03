"""Reading variables from the environment."""

import dataclasses
import os

from .. import exceptions


@dataclasses.dataclass
class TEnvironment:
    """Environment variable values."""

    # The OAuth client id
    client_id: str
    # The OAuth client secret
    client_secret: str


def _read_environment() -> TEnvironment:
    """Read environment variables."""
    client_id = os.getenv("CLIENT_ID", default=None)
    if not isinstance(client_id, str):
        raise exceptions.CredentialError(
            "The CLIENT_ID environment variable needs to be set."
        )
    client_secret = os.getenv("CLIENT_SECRET", default=None)
    if not isinstance(client_secret, str):
        raise exceptions.CredentialError(
            "The CLIENT_SECRET environment variable needs to be set."
        )

    return TEnvironment(client_id=client_id, client_secret=client_secret)


_ENVIRONMENT = _read_environment()


def get() -> TEnvironment:
    """Get the environment variables."""
    return _ENVIRONMENT
