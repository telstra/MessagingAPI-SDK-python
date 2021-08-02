"""The exceptions for the messaging API."""


class MessagingBaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(MessagingBaseException):
    """Raised when required credentials are not provided."""


class NumbersError(MessagingBaseException):
    """Raised when a numbers request failed."""


class MessageError(MessagingBaseException):
    """Raised when a message request failed."""


class TrialNumbersError(MessagingBaseException):
    """Raised when a trial numbers request failed."""
