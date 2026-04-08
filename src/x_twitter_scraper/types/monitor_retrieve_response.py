# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MonitorRetrieveResponse"]


class MonitorRetrieveResponse(BaseModel):
    """Account monitor that tracks activity for a given X user."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[
        Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]
    ] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    is_active: bool = FieldInfo(alias="isActive")

    username: str

    x_user_id: str = FieldInfo(alias="xUserId")
