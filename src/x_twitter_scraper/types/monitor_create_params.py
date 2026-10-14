# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["MonitorCreateParams"]


class MonitorCreateParams(TypedDict, total=False):
    event_types: Required[Annotated[List[EventType], PropertyInfo(alias="eventTypes")]]
    """Array of event types to subscribe to."""

    username: Required[str]
    """X username to monitor, with or without @"""

    name: str
    """Your label for the monitor.

    Its events carry it as monitorName. Whitespace is normalized.
    """
