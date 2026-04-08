# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .draw_list_item import DrawListItem

__all__ = ["DrawListResponse"]


class DrawListResponse(BaseModel):
    draws: List[DrawListItem]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
