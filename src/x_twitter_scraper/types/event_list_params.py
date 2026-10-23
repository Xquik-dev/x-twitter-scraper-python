# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType
from .monitors.post_monitor import PostEventType

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor.

    The after alias also works. Offset pagination is not supported.
    """

    event_type: Annotated[Union[EventType, PostEventType], PropertyInfo(alias="eventType")]
    """Filter events by type"""

    keyword_monitor_id: Annotated[str, PropertyInfo(alias="keywordMonitorId")]
    """Keyword monitor ID. The keyword_monitor_id alias also works."""

    limit: int
    """Maximum items per page: 1 to 100, default 50.

    Credits can reduce paid results. With none affordable, it returns 402
    insufficient_credits.
    """

    monitor_id: Annotated[str, PropertyInfo(alias="monitorId")]
    """Account monitor ID. The monitor_id alias also works."""

    post_monitor_id: Annotated[str, PropertyInfo(alias="postMonitorId")]
    """Post monitor ID. The post_monitor_id alias also works."""
