# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """Webhook endpoint registered to receive event deliveries."""

    id: str

    consecutive_failures: int = FieldInfo(alias="consecutiveFailures")
    """Consecutive failed delivery attempts since the last success."""

    created_at: datetime = FieldInfo(alias="createdAt")

    delivery_status: Literal["active", "paused", "needs_attention"] = FieldInfo(alias="deliveryStatus")
    """Endpoint delivery state.

    needs_attention means delivery stopped after repeated failures.
    """

    event_types: List[EventType] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    failure_hard_cap: int = FieldInfo(alias="failureHardCap")
    """Consecutive delivery failures that pause the endpoint."""

    is_active: bool = FieldInfo(alias="isActive")

    url: str
