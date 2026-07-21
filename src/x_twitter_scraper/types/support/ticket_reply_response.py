# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketReplyResponse", "Attachment"]


class Attachment(BaseModel):
    public_id: str = FieldInfo(alias="publicId")

    status: Literal["pending", "ready", "failed"]


class TicketReplyResponse(BaseModel):
    attachments: Optional[List[Attachment]] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)
