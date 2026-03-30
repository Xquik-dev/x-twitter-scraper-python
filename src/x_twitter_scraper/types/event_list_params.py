# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination"""

    event_type: Annotated[EventType, PropertyInfo(alias="eventType")]

    limit: int

    monitor_id: Annotated[str, PropertyInfo(alias="monitorId")]
