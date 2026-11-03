# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import builtins
from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ActivityRecord",
    "Timestamps",
    "Request",
    "Caller",
    "CallerAPIKey",
    "CallerOAuthClient",
    "Charge",
    "Related",
]


class Timestamps(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    confirmed_at: Optional[datetime] = FieldInfo(alias="confirmedAt", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    occurred_at: Optional[datetime] = FieldInfo(alias="occurredAt", default=None)

    discovered_at: Optional[datetime] = FieldInfo(alias="discoveredAt", default=None)

    posted_at: Optional[datetime] = FieldInfo(alias="postedAt", default=None)

    first_attempted_at: Optional[datetime] = FieldInfo(alias="firstAttemptedAt", default=None)

    delivered_at: Optional[datetime] = FieldInfo(alias="deliveredAt", default=None)

    next_retry_at: Optional[datetime] = FieldInfo(alias="nextRetryAt", default=None)

    exhausted_at: Optional[datetime] = FieldInfo(alias="exhaustedAt", default=None)

    drawn_at: Optional[datetime] = FieldInfo(alias="drawnAt", default=None)

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)

    paused_at: Optional[datetime] = FieldInfo(alias="pausedAt", default=None)


class Request(BaseModel):
    """The API request behind this activity.

    Null for activity from before Oct 30, 2026, and for activity no API request
    starts, such as a monitor event, a webhook delivery or a credit grant.
    """

    method: Literal["DELETE", "PATCH", "POST", "PUT"]

    path: str

    http_status: int = FieldInfo(alias="httpStatus")

    duration_ms: int = FieldInfo(alias="durationMs")

    ip_address: Optional[str] = FieldInfo(alias="ipAddress")

    user_agent: Optional[str] = FieldInfo(alias="userAgent")

    at: datetime


class CallerAPIKey(BaseModel):
    """Name and prefix of the API key used. Never its value."""

    name: str

    prefix: str


class CallerOAuthClient(BaseModel):
    id: str

    name: str


class Caller(BaseModel):
    auth_method: Optional[Literal["api_key", "oauth", "session"]] = FieldInfo(alias="authMethod")

    api_key: Optional[CallerAPIKey] = FieldInfo(alias="apiKey")
    """Name and prefix of the API key used. Never its value."""

    oauth_client: Optional[CallerOAuthClient] = FieldInfo(alias="oauthClient")


class Charge(BaseModel):
    """Credits charged for this activity."""

    credits: int

    balance_after: int = FieldInfo(alias="balanceAfter")

    at: datetime


class Related(BaseModel):
    id: str

    type: str

    status: Literal["completed", "running", "failed", "canceled"]

    created_at: datetime = FieldInfo(alias="createdAt")

    url: str


class ActivityRecord(BaseModel):
    """Full technical record of 1 activity.

    Timestamps are ISO 8601 in UTC to the millisecond.
    """

    object: Literal["activity"]

    id: str
    """Activity ID."""

    kind: Literal[
        "write_action",
        "extraction",
        "monitor_change",
        "api_key",
        "billing",
        "giveaway_draw",
        "monitor_event",
        "media_download",
        "media_share",
        "support_ticket",
        "webhook_delivery",
        "webhook_endpoint",
        "x_account_connection",
    ]
    """Kind of the activity. Only a signed-in dashboard session sees an `api_key` record."""

    type: str
    """Type of the activity within its kind, the same as the type of its Activity log row.

    Examples are a write action type, an extraction tool type, a monitor change, a
    monitor event type or a ledger entry type.
    """

    status: Literal["completed", "running", "failed", "canceled"]

    url: str
    """Dashboard page of this activity."""

    request_id: Optional[str] = FieldInfo(alias="requestId")
    """ID of the API request behind this activity."""

    timestamps: Timestamps

    request: Optional[Request]
    """The API request behind this activity.

    Null for activity from before Oct 30, 2026, and for activity no API request
    starts, such as a monitor event, a webhook delivery or a credit grant.
    """

    caller: Caller

    charge: Optional[Charge]
    """Credits charged for this activity."""

    details: Dict[str, builtins.object]
    """Fields of this kind of activity, such as its target.

    A field can hold JSON, such as the data of a monitor event or the payload of a
    webhook delivery.
    """

    related: List[Related]
    """Up to 5 other activities on the same subject within 7 days, newest first."""
