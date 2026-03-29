# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketRetrieveResponse", "Message"]


class Message(BaseModel):
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
