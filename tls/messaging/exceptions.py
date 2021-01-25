"""The exceptions for the messaging API."""


class MessagingBaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(MessagingBaseException):
    """Raised when required credentials are not provided."""


class SubscriptionError(MessagingBaseException):
    """Raised when a subscription request failed."""


class SmsError(MessagingBaseException):
    """Raised when a sms request failed."""


class BnumError(MessagingBaseException):
    """Raised when a bnum request failed."""
