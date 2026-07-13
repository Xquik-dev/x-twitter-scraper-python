# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["EventDetail"]


class EventDetail(BaseModel):
    """Full monitor event including payload data and optional X event ID."""

    id: str

    data: Dict[str, object]
    """Event payload - shape varies by event type (JSON)"""

    monitor_id: str = FieldInfo(alias="monitorId")
    """Monitor ID associated with this detailed event payload."""

    monitor_type: Literal["account", "keyword"] = FieldInfo(alias="monitorType")
    """Source monitor type for this detailed event."""

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: EventType
    """Type of monitor event fired when account activity occurs."""

    keyword_monitor_id: Optional[str] = FieldInfo(alias="keywordMonitorId", default=None)
    """Keyword monitor ID included on detailed keyword events."""

    query: Optional[str] = None
    """Keyword query for this detailed monitor event."""

    username: Optional[str] = None
    """Account username for this detailed monitor event."""

    x_event_id: Optional[str] = FieldInfo(alias="xEventId", default=None)
