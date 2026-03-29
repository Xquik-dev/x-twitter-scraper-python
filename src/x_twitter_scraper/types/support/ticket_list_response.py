# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketListResponse", "Ticket"]


class Ticket(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    message_count: Optional[int] = FieldInfo(alias="messageCount", default=None)

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    status: Optional[str] = None

    subject: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class TicketListResponse(BaseModel):
    tickets: Optional[List[Ticket]] = None
