"""Configuration for requests."""

import os
import typing

from .. import exceptions

TClientId = str
TClientSecret = str


class Config:
    """
    Configuration for requests.

    Attrs:
        telstra_client_id: The OAuth client id
        telstra_client_secret: The OAuth client secret

    """

    def __init__(
        self,
        *,
        telstra_client_id: typing.Optional[TClientId] = None,
        telstra_client_secret: typing.Optional[TClientSecret] = None,
    ) -> None:
        """Construct."""
        if telstra_client_id is not None:
            self.telstra_client_id = telstra_client_id
        if telstra_client_secret is not None:
            self.telstra_client_secret = telstra_client_secret

    _telstra_client_id: typing.Optional[TClientId] = None
    _telstra_client_secret: typing.Optional[TClientSecret] = None

    @property
    def telstra_client_id(self) -> TClientId:
        """Get the telstra_client_id."""
        if self._telstra_client_id is None:
            telstra_client_id_env_name = "TELSTRA_CLIENT_ID"
            telstra_client_id = os.getenv(telstra_client_id_env_name)
            if not isinstance(telstra_client_id, TClientId):
                raise exceptions.CredentialError(
                    "The client id was not configured. "
                    "It can be retrieved from here: "
                    "https://dev.telstra.com/user/me/apps. "
                    f"Then it can be provided as the '{telstra_client_id_env_name}' "
                    "environment variable or "
                    "using the following code: \n"
                    "from telstra.messaging.utils.config import CONFIG\n"
                    "CONFIG.telstra_client_id = '<client id>'"
                )
            self._telstra_client_id = telstra_client_id
        return self._telstra_client_id

    @telstra_client_id.setter
    def telstra_client_id(self, telstra_client_id: TClientId) -> None:
        """Set the telstra_client_id."""
        if not isinstance(telstra_client_id, TClientId):
            raise exceptions.CredentialError(
                "The provided client id is not valid, "
                f"expecting a {TClientId}, "
                f"received {telstra_client_id}."
            )
        self._telstra_client_id = telstra_client_id

    @property
    def telstra_client_secret(self) -> TClientSecret:
        """Get the telstra_client_secret."""
        if self._telstra_client_secret is None:
            telstra_client_secret_env_name = "TELSTRA_CLIENT_SECRET"
            telstra_client_secret = os.getenv(telstra_client_secret_env_name)
            if not isinstance(telstra_client_secret, TClientSecret):
                raise exceptions.CredentialError(
                    "The client secret was not configured. "
                    "It can be retrieved from here: "
                    "https://dev.telstra.com/user/me/apps. "
                    "Then it can be provided as the "
                    f"'{telstra_client_secret_env_name}'' environment variable or "
                    "using the following code: \n"
                    "from telstra.messaging.utils.config import CONFIG\n"
                    "CONFIG.telstra_client_secret = '<client secret>'"
                )
            self._telstra_client_secret = telstra_client_secret
        return self._telstra_client_secret

    @telstra_client_secret.setter
    def telstra_client_secret(self, telstra_client_secret: TClientSecret) -> None:
        """Set the telstra_client_secret."""
        if not isinstance(telstra_client_secret, TClientSecret):
            raise exceptions.CredentialError(
                "The provided client secret is not valid, "
                f"expecting a {TClientSecret}, "
                f"received {telstra_client_secret}."
            )
        self._telstra_client_secret = telstra_client_secret


CONFIG = Config()


def get() -> Config:
    """Get the configuration."""
    return CONFIG
