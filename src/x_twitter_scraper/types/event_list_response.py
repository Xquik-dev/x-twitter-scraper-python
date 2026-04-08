# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EventListResponse", "Event"]


class Event(BaseModel):
    """Monitor event summary with type, username, and occurrence time."""

    id: str

    data: Dict[str, object]

    monitor_id: str = FieldInfo(alias="monitorId")

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]
    """Type of monitor event fired when account activity occurs."""

    username: str


class EventListResponse(BaseModel):
    events: List[Event]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
