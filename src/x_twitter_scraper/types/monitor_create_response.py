# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["MonitorCreateResponse"]


class MonitorCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[EventType] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    is_active: bool = FieldInfo(alias="isActive")

    next_billing_at: datetime = FieldInfo(alias="nextBillingAt")
    """Next hourly credit charge time. New active monitors are due immediately."""

    username: str

    x_user_id: str = FieldInfo(alias="xUserId")
