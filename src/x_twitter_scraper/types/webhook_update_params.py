# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType
from .monitors.post_monitor import PostEventType

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    event_types: Annotated[List[Union[EventType, PostEventType]], PropertyInfo(alias="eventTypes")]
    """Array of event types to subscribe to."""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    url: str
