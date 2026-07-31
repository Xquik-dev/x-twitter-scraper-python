# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketListResponse", "Ticket"]


class Ticket(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    message_count: int = FieldInfo(alias="messageCount")

    public_id: str = FieldInfo(alias="publicId")

    status: Literal["open", "in_progress", "resolved", "closed"]

    subject: str

    updated_at: datetime = FieldInfo(alias="updatedAt")


class TicketListResponse(BaseModel):
    tickets: List[Ticket]
