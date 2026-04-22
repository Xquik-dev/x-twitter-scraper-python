# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .radar_item import RadarItem

__all__ = ["RadarRetrieveTrendingTopicsResponse"]


class RadarRetrieveTrendingTopicsResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    items: List[RadarItem]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Opaque cursor for the next page (present only when hasMore is true)."""
