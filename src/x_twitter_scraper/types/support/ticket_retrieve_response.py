# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketRetrieveResponse", "Message", "MessageAttachment"]


class MessageAttachment(BaseModel):
    """Downloadable image or video attached to a support message."""

    content_type: Literal[
        "image/jpeg", "image/png", "image/gif", "image/webp", "video/mp4", "video/quicktime", "video/webm"
    ] = FieldInfo(alias="contentType")
    """Validated media type."""

    filename: str

    kind: Literal["image", "video"]
    """Attachment media class."""

    public_id: str = FieldInfo(alias="publicId")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    status: Literal["pending", "ready", "failed"]
    """Storage processing state."""

    url: str


class Message(BaseModel):
    attachments: List[MessageAttachment]

    body: str

    created_at: datetime = FieldInfo(alias="createdAt")

    sender: Literal["user", "support", "system"]


class TicketRetrieveResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    messages: List[Message]

    public_id: str = FieldInfo(alias="publicId")

    status: Literal["open", "in_progress", "resolved", "closed"]

    subject: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
