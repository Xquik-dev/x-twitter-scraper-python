# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor. Offset pagination is not supported."""

    event_type: Annotated[EventType, PropertyInfo(alias="eventType")]
    """Filter events by type"""

    keyword_monitor_id: Annotated[str, PropertyInfo(alias="keywordMonitorId")]
    """Keyword monitor ID."""

    limit: int
    """Maximum items per page: 1 to 100, default 50.

    Credits can reduce paid results. The endpoint returns 402 insufficient_credits
    when none are affordable.
    """

    monitor_id: Annotated[str, PropertyInfo(alias="monitorId")]
    """Account monitor ID."""
