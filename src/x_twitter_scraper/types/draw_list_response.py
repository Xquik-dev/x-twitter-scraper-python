# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DrawListResponse", "Draw"]


class Draw(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    total_entries: int = FieldInfo(alias="totalEntries")

    tweet_url: str = FieldInfo(alias="tweetUrl")

    valid_entries: int = FieldInfo(alias="validEntries")

    drawn_at: Optional[datetime] = FieldInfo(alias="drawnAt", default=None)


class DrawListResponse(BaseModel):
    draws: List[Draw]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
