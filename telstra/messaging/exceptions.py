"""The exceptions for the messaging API."""


class MessagingBaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(MessagingBaseException):
    """Raised when required credentials are not provided."""


class NumbersError(MessagingBaseException):
    """Raised when a numbers request failed."""


class SmsError(MessagingBaseException):
    """Raised when a sms request failed."""


class TrialNumbersError(MessagingBaseException):
    """Raised when a trial numbers request failed."""
