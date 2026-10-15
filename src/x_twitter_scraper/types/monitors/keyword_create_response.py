# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.event_type import EventType

__all__ = ["KeywordCreateResponse"]


class KeywordCreateResponse(BaseModel):
    """Keyword monitor that tracks matching public X activity."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[EventType] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    is_active: bool = FieldInfo(alias="isActive")

    next_billing_at: datetime = FieldInfo(alias="nextBillingAt")
    """Next hourly credit charge time for this keyword query monitor."""

    query: str

    name: Optional[str] = None
    """Customer-set label of the keyword monitor, when set."""

    paused_at: Optional[datetime] = FieldInfo(alias="pausedAt", default=None)
    """When Xquik paused this keyword monitor."""

    paused_reason: Optional[Literal["insufficient_credits"]] = FieldInfo(alias="pausedReason", default=None)
    """Why Xquik paused this keyword monitor.

    The balance could not pay an hour, so add credits & resume. Absent when the
    monitor is active or you paused it yourself.
    """
