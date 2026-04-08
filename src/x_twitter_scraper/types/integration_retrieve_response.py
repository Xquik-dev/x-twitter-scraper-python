# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationRetrieveResponse"]


class IntegrationRetrieveResponse(BaseModel):
    """Third-party integration (e.g. Telegram) subscribed to monitor events."""

    id: str

    config: Dict[str, object]
    """Integration config — shape varies by type (JSON)"""

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[
        Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]
    ] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    is_active: bool = FieldInfo(alias="isActive")

    name: str

    type: Literal["telegram"]

    filters: Optional[Dict[str, object]] = None
    """Event filter rules (JSON)"""

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)

    scope_all_monitors: Optional[bool] = FieldInfo(alias="scopeAllMonitors", default=None)

    silent_push: Optional[bool] = FieldInfo(alias="silentPush", default=None)
