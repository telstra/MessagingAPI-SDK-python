"""Used to work with health check of messaging services."""

from urllib import error, request

from . import exceptions, oauth

_URL = "https://products.api.telstra.com/messaging/v3/health-check"


def get() -> None:
    """
    Check operational status of the messaging service.

    Returns nothing

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.HealthCheckError(
            f"Could not retrieve an OAuth token: {exc}"
        ) from exc

    headers = {
        "Authorization": token.authorization,
        "Telstra-api-version": "3.x",
        "Content-Language": "en-au",
        "Accept-Charset": "utf-8",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    health_check_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(health_check_request):
            return
    except error.HTTPError as exc:
        raise exceptions.HealthCheckError(f"Health check failed: {exc}") from exc
