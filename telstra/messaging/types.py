"""Shared types for messaging."""

from enum import Enum

TTo = str
TFrom = str
TMessageId = str
TMessageContent = str
TRetryTimeout = int
TScheduleSend = str
TDeliveryNotification = bool
TStatusCallbackUrl = str
TTags = str
TSentTimestamp = str
TLimit = int
TOffset = int
TFilter = str


class TMultimediaContentTypes(Enum):
    """MMS Content Type."""

    AUDIO_AMR: str = "audio/amr"
    AUDIO_MP3: str = "audio/mp3"
    AUDIO_MPEG3: str = "audio/mpeg3"
    AUDIO_MIDI: str = "audio/midi"
    AUDIO_WAV: str = "audio/wav"
    AUDIO_BASIC: str = "audio/basic"
    IMAGE_GIF: str = "image/gif"
    IMAGE_JPEG: str = "image/jpeg"
    IMAGE_PNG: str = "image/png"
    IMAGE_BMP: str = "image/bmp"
    VIDEO_MPEG4: str = "video/mpeg4"
    VIDEO_MP4: str = "video/mp4"
    VIDEO_MPG: str = "video/mpg"
    VIDEO_MPEG: str = "video/mpeg"
    VIDEO_3GPP: str = "video/3gpp"
    VIDEO_3GP: str = "video/3gp"
