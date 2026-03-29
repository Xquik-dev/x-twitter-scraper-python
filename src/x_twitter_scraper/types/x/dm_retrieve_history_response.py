# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DmRetrieveHistoryResponse", "Message"]


class Message(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    receiver_id: Optional[str] = FieldInfo(alias="receiverId", default=None)

    sender_id: Optional[str] = FieldInfo(alias="senderId", default=None)

    text: Optional[str] = None


class DmRetrieveHistoryResponse(BaseModel):
    has_next_page: bool

    messages: List[Message]

    next_cursor: str
