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
    """Cursor for keyset pagination from prior response next_cursor"""

    event_type: Annotated[EventType, PropertyInfo(alias="eventType")]
    """Filter events by type"""

    limit: int
    """Maximum number of items to return (1-100, default 50).

    For paid per-result endpoints, the returned count may be lower when remaining
    credits cannot cover the requested page. If zero paid results are affordable,
    the endpoint returns 402 insufficient_credits.
    """

    monitor_id: Annotated[str, PropertyInfo(alias="monitorId")]
    """Filter events by monitor ID"""
