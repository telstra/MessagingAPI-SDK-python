"""Configuration for requests."""

import os
import typing

from .. import exceptions

TTlsClientKey = str
TTlsClientSecret = str


class Config:
    """
    Configuration for requests.

    Attrs:
        tls_client_key: The OAuth client id
        tls_client_secret: The OAuth client secret

    """

    def __init__(
        self,
        *,
        tls_client_key: typing.Optional[TTlsClientKey] = None,
        tls_client_secret: typing.Optional[TTlsClientSecret] = None,
    ) -> None:
        """Construct."""
        if tls_client_key is not None:
            self.tls_client_key = tls_client_key
        if tls_client_secret is not None:
            self.tls_client_secret = tls_client_secret

    _tls_client_key: typing.Optional[TTlsClientKey] = None
    _tls_client_secret: typing.Optional[TTlsClientSecret] = None

    @property
    def tls_client_key(self) -> TTlsClientKey:
        """Get the tls_client_key."""
        if self._tls_client_key is None:
            tls_client_key_env_name = "TLS_CLIENT_KEY"
            tls_client_key = os.getenv(tls_client_key_env_name)
            if not isinstance(tls_client_key, TTlsClientKey):
                raise exceptions.CredentialError(
                    "The client key was not configured. "
                    "It can be retrieved from here: "
                    "https://dev.telstra.com/user/me/apps. "
                    f"Then it can be provided as the '{tls_client_key_env_name}' "
                    "environment variable or "
                    "using the following code: \n"
                    "from tls.messaging.utils import CONFIG\n"
                    "CONFIG.tls_client_key = '<client key>'"
                )
            self._tls_client_key = tls_client_key
        return self._tls_client_key

    @tls_client_key.setter
    def tls_client_key(self, tls_client_key: TTlsClientKey) -> None:
        """Set the tls_client_key."""
        if not isinstance(tls_client_key, TTlsClientKey):
            raise exceptions.CredentialError(
                "The provided client key is not valid, "
                f"expecting a {TTlsClientKey}, "
                f"received {tls_client_key}."
            )
        self._tls_client_key = tls_client_key

    @property
    def tls_client_secret(self) -> TTlsClientSecret:
        """Get the tls_client_secret."""
        if self._tls_client_secret is None:
            tls_client_secret_env_name = "TLS_CLIENT_SECRET"
            tls_client_secret = os.getenv(tls_client_secret_env_name)
            if not isinstance(tls_client_secret, TTlsClientSecret):
                raise exceptions.CredentialError(
                    "The client secret was not configured. "
                    "It can be retrieved from here: "
                    "https://dev.telstra.com/user/me/apps. "
                    f"Then it can be provided as the '{tls_client_secret_env_name}'' "
                    "environment variable or "
                    "using the following code: \n"
                    "from tls.messaging.utils import CONFIG\n"
                    "CONFIG.tls_client_secret = '<client secret>'"
                )
            self._tls_client_secret = tls_client_secret
        return self._tls_client_secret

    @tls_client_secret.setter
    def tls_client_secret(self, tls_client_secret: TTlsClientSecret) -> None:
        """Set the tls_client_secret."""
        if not isinstance(tls_client_secret, TTlsClientSecret):
            raise exceptions.CredentialError(
                "The provided client secret is not valid, "
                f"expecting a {TTlsClientSecret}, "
                f"received {tls_client_secret}."
            )
        self._tls_client_secret = tls_client_secret


CONFIG = Config()


def get() -> Config:
    """Get the configuration."""
    return CONFIG
