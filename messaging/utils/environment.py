"""Reading variables from the environment."""

import dataclasses
import os

from .. import exceptions


@dataclasses.dataclass
class TEnvironment:
    """Environment variable values."""

    # The OAuth client id
    tls_client_key: str
    # The OAuth client secret
    tls_client_secret: str


def _read_environment() -> TEnvironment:
    """Read environment variables."""
    tls_client_key = os.getenv("TLS_CLIENT_KEY", default=None)
    if not isinstance(tls_client_key, str):
        raise exceptions.CredentialError(
            "The TLS_CLIENT_KEY environment variable needs to be set, find it here: "
            "https://dev.telstra.com/user/me/apps."
        )
    tls_client_secret = os.getenv("TLS_CLIENT_SECRET", default=None)
    if not isinstance(tls_client_secret, str):
        raise exceptions.CredentialError(
            "The TLS_CLIENT_SECRET environment variable needs to be set, find it "
            "here: https://dev.telstra.com/user/me/apps."
        )

    return TEnvironment(
        tls_client_key=tls_client_key, tls_client_secret=tls_client_secret
    )


_ENVIRONMENT = _read_environment()


def get() -> TEnvironment:
    """Get the environment variables."""
    return _ENVIRONMENT
