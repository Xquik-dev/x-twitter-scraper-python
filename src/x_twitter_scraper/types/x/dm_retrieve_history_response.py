# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DmRetrieveHistoryResponse", "Message"]


class Message(BaseModel):
    id: str

    receiver_id: str = FieldInfo(alias="receiverId")

    sender_id: str = FieldInfo(alias="senderId")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)
    """URL of attached media (image, GIF, or video).

    Omitted when the message has no media attachment.
    """

    text: Optional[str] = None


class DmRetrieveHistoryResponse(BaseModel):
    has_next_page: bool

    messages: List[Message]

    next_cursor: str
