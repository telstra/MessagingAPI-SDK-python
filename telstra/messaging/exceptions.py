"""The exceptions for the messaging API."""


class MessagingBaseException(Exception):
    """The base class for all other exceptions."""


class CredentialError(MessagingBaseException):
    """Raised when required credentials are not provided."""


class VirtualNumbersError(MessagingBaseException):
    """Raised when a virtual numbers request failed."""


class MessageError(MessagingBaseException):
    """Raised when a message request failed."""


class FreeTrialNumbersError(MessagingBaseException):
    """Raised when a free trial numbers request failed."""


class ReportsError(MessagingBaseException):
    """Raised when a reports request failed."""


class HealthCheckError(MessagingBaseException):
    """Raised when a health check request failed."""
