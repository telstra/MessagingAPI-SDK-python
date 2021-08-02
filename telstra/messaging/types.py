"""Shared types for messaging."""

from enum import Enum

TTo = str
TFrom = str
TNotifyUrl = str
TMessageId = str
TBody = str
TSentTimestamp = str
TValidity = int
TScheduledDelivery = int
TReplyRequest = bool
TPriority = bool
TReceiptOff = bool
TUsrMsgRef = str
TSubject = str
TMessageType = str


class TMMSContentType(Enum):
    """MMS Content Type"""

    AUDIO_AMR: str = "audio/amr"
    AUDIO_AAC: str = "audio/aac"
    AUDIO_MP3: str = "audio/mp3"
    AUDIO_MPEG3: str = "audio/mpeg3"
    AUDIO_MPEG: str = "audio/mpeg"
    AUDIO_MPG: str = "audio/mpg"
    AUDIO_WAV: str = "audio/wav"
    AUDIO_3GPP: str = "audio/3gpp"
    AUDIO_MP4: str = "audio/mp4"
    IMAGE_GIF: str = "image/gif"
    IMAGE_JPEG: str = "image/jpeg"
    IMAGE_JPG: str = "image/jpg"
    IMAGE_PNG: str = "image/png"
    IMAGE_BMP: str = "image/bmp"
    VIDEO_MPEG4: str = "video/mpeg4"
    VIDEO_MP4: str = "video/mp4"
    VIDEO_MPEG: str = "video/mpeg"
    VIDEO_3GPP: str = "video/3gpp"
    VIDEO_3GP: str = "video/3gp"
    VIDEO_H263: str = "video/h263"
    TEXT_PLAIN: str = "text/plain"
    TEXT_X_VCARD: str = "text/x-vCard"
    TEXT_X_VCALENDAR: str = "text/x-vCalendar"


class TMMSContent:
    """MMS Content Object"""

    type: TMMSContentType
    filename: str
    payload: str
