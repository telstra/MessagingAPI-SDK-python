"""Used to work with Trial Numbers for the free trial."""

import ssl
from urllib import error, request

from . import exceptions, oauth

_URL = "https://products.api.telstra.com/messaging/v3/health-check"
# gcontext = (
#     ssl._create_unverified_context()
# )  ## TODO Remove this line, only for NP to circumvent certificate issue


def get() -> None:
    """
    Check operational status of the messaging service.

    Returns nothing

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.FreeTrialNumbersError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.1.0",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    health_check_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(health_check_request) as response:
            return
    except error.HTTPError as exc:
        raise exceptions.HealthCheckError(f"Health check failed: {exc}") from exc
