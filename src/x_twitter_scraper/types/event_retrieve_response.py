# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EventRetrieveResponse"]


class EventRetrieveResponse(BaseModel):
    id: str

    data: Dict[str, object]
    """Event payload — shape varies by event type (JSON)"""

    monitor_id: str = FieldInfo(alias="monitorId")

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]

    username: str

    x_event_id: Optional[str] = FieldInfo(alias="xEventId", default=None)
