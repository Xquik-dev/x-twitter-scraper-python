# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .event import Event
from .._models import BaseModel

__all__ = ["EventListResponse"]


class EventListResponse(BaseModel):
    events: List[Event]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
