# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    paused_at: Optional[datetime] = FieldInfo(alias="pausedAt", default=None)
    """When Xquik automatically paused this monitor."""

    paused_reason: Optional[Literal["x_user_not_found"]] = FieldInfo(alias="pausedReason", default=None)
    """Why Xquik automatically paused this monitor."""
