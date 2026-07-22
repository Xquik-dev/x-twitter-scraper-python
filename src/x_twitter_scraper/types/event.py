# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["Event"]


class Event(BaseModel):
    """Monitor event summary with source metadata and occurrence time."""

    id: str

    data: Dict[str, object]

    monitor_id: str = FieldInfo(alias="monitorId")
    """
    Account monitor ID for account events, or keyword monitor ID for keyword events.
    """

    monitor_type: Literal["account", "keyword"] = FieldInfo(alias="monitorType")
    """Source monitor type."""

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: EventType
    """Type of monitor event fired when account activity occurs."""

    keyword_monitor_id: Optional[str] = FieldInfo(alias="keywordMonitorId", default=None)
    """Keyword monitor ID, present for keyword monitor events."""

    query: Optional[str] = None
    """Keyword query, present for keyword monitor events."""

    username: Optional[str] = None
    """Account username, present for account monitor events."""
