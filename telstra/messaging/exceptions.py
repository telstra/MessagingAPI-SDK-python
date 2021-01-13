"""The exceptions for the messaging API."""


class SmsBaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(SmsBaseException):
    """Raised when required credentials are not provided."""


class SubscriptionError(SmsBaseException):
    """Raised when a subscription request failed."""


class SmsError(SmsBaseException):
    """Raised when a sms request failed."""


class BnumError(SmsBaseException):
    """Raised when a bnum request failed."""
