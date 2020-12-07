"""The exceptions for the messaging API."""


class BaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(BaseException):
    """Raised when required credentials are not provided."""


class SubscriptionError(BaseException):
    """Raised when creating a subscription failed."""
