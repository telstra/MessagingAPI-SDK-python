"""The exceptions for the messaging API."""


class BaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(BaseException):
    """Raised when required credentials are not provided."""


class SubscriptionError(BaseException):
    """Raised when a subscription request failed."""


class SmsError(BaseException):
    """Raised when a sms request failed."""


class BnumError(BaseException):
    """Raised when a bnum request failed."""
