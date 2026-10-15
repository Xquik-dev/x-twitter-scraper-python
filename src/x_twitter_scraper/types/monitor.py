# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["Monitor"]


class Monitor(BaseModel):
    """Account monitor that tracks activity for a given X user."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[EventType] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    is_active: bool = FieldInfo(alias="isActive")

    next_billing_at: datetime = FieldInfo(alias="nextBillingAt")
    """Next hourly credit charge time for this account monitor."""

    username: str

    x_user_id: str = FieldInfo(alias="xUserId")

    name: Optional[str] = None
    """Customer-set label of the account monitor, when set."""

    paused_at: Optional[datetime] = FieldInfo(alias="pausedAt", default=None)
    """When Xquik paused this account monitor."""

    paused_reason: Optional[Literal["insufficient_credits", "x_account_protected", "x_user_not_found"]] = FieldInfo(
        alias="pausedReason", default=None
    )
    """Why Xquik paused this account monitor.

    `insufficient_credits` means the balance could not pay an hour, so add credits &
    resume. The other 2 mean X stopped showing the account. Absent when the monitor
    is active or you paused it yourself.
    """
