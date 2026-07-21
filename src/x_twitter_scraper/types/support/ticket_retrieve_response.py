# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketRetrieveResponse", "Message", "MessageAttachment"]


class MessageAttachment(BaseModel):
    content_type: Literal[
        "image/jpeg", "image/png", "image/gif", "image/webp", "video/mp4", "video/quicktime", "video/webm"
    ] = FieldInfo(alias="contentType")

    filename: str

    kind: Literal["image", "video"]

    public_id: str = FieldInfo(alias="publicId")

    size_bytes: int = FieldInfo(alias="sizeBytes")

    status: Literal["pending", "ready", "failed"]

    url: str


class Message(BaseModel):
    attachments: Optional[List[MessageAttachment]] = None

    body: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    sender: Optional[str] = None


class TicketRetrieveResponse(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    messages: Optional[List[Message]] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    status: Optional[str] = None

    subject: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
