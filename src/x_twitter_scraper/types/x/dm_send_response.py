# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DmSendResponse", "Account", "Billing", "NextAction", "Request", "Result", "Target"]


class Account(BaseModel):
    """Connected account selected for the write."""

    id: str

    username: str


class Billing(BaseModel):
    """plannedCredits is the approved maximum.

    chargedCredits comes from the settled credit ledger. Pending or failed writes are not charged.
    """

    charged: bool

    charged_credits: str = FieldInfo(alias="chargedCredits")

    planned_credits: str = FieldInfo(alias="plannedCredits")

    status: Literal["not_charged", "pending", "charged", "charge_failed", "refunded"]


class NextAction(BaseModel):
    """Exact follow-up an API client or agent should perform."""

    type: Literal["poll", "retry", "verify_result", "fix_request"]

    after_ms: Optional[int] = FieldInfo(alias="afterMs", default=None)

    requires_new_idempotency_key: Optional[bool] = FieldInfo(alias="requiresNewIdempotencyKey", default=None)

    url: Optional[str] = None


class Request(BaseModel):
    """Stable fingerprint and sanitized payload for replay checks."""

    hash: Optional[str] = None
    """Stable hash of account, action, target, and payload."""

    payload: Optional[Dict[str, object]] = None
    """Exact sanitized payload dispatched for this action."""


class Result(BaseModel):
    """Confirmed result produced by the write, when available."""

    id: Optional[str] = None

    state: Optional[str] = None

    type: Optional[Literal["tweet", "direct_message", "media", "community", "state_change"]] = None


class Target(BaseModel):
    """Existing X resource targeted by the write, when applicable."""

    id: str

    type: Literal["tweet", "user", "community"]


class DmSendResponse(BaseModel):
    """Durable write lifecycle record.

    Poll statusUrl until terminal is true. Reusing the original Idempotency-Key returns this same record. Submit a new write only when safeToRetry is true, using a new key.
    """

    id: str

    account: Optional[Account] = None
    """Connected account selected for the write."""

    action: Literal[
        "create_tweet",
        "delete_tweet",
        "like",
        "unlike",
        "retweet",
        "unretweet",
        "follow",
        "unfollow",
        "remove_follower",
        "send_dm",
        "upload_media",
        "update_profile",
        "update_avatar",
        "update_banner",
        "create_community",
        "delete_community",
        "join_community",
        "leave_community",
    ]

    billing: Billing
    """plannedCredits is the approved maximum.

    chargedCredits comes from the settled credit ledger. Pending or failed writes
    are not charged.
    """

    charged: bool

    charged_credits: str = FieldInfo(alias="chargedCredits")

    next_action: Optional[NextAction] = FieldInfo(alias="nextAction", default=None)
    """Exact follow-up an API client or agent should perform."""

    object: Literal["x_write_action"]

    poll_after_ms: Optional[int] = FieldInfo(alias="pollAfterMs", default=None)

    request: Request
    """Stable fingerprint and sanitized payload for replay checks."""

    result: Optional[Result] = None
    """Confirmed result produced by the write, when available."""

    retryable: bool
    """True only when a new attempt can reasonably succeed."""

    safe_to_retry: bool = FieldInfo(alias="safeToRetry")
    """True only when no write was dispatched and a new idempotency key may be used."""

    send_dispatched: bool = FieldInfo(alias="sendDispatched")

    status: Literal["accepted", "dispatching", "pending_confirmation", "success", "failed", "expired"]

    status_url: str = FieldInfo(alias="statusUrl")

    success: bool

    target: Optional[Target] = None
    """Existing X resource targeted by the write, when applicable."""

    target_id: Optional[str] = FieldInfo(alias="targetId", default=None)

    terminal: bool

    write_action_id: str = FieldInfo(alias="writeActionId")

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Compatibility field for a confirmed community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)
    """Confirmed community name when available."""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    confirmation_attempts: Optional[int] = FieldInfo(alias="confirmationAttempts", default=None)

    confirmation_checked_at: Optional[datetime] = FieldInfo(alias="confirmationCheckedAt", default=None)

    confirmed_at: Optional[datetime] = FieldInfo(alias="confirmedAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    details: Optional[Dict[str, builtins.object]] = None
    """Structured recovery context for a failed write."""

    error: Optional[str] = None

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Deadline for resolving a non-terminal write.

    This is not the Idempotency-Key retention deadline.
    """

    idempotent: Optional[bool] = None

    media: Optional[Dict[str, builtins.object]] = None
    """Media count, kind, size, and billing details when used."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """Compatibility field for a confirmed media upload ID."""

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)
    """Public media URL when the upload creates one."""

    message: Optional[str] = None

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """Compatibility field for a confirmed direct message ID."""

    request_hash: Optional[str] = FieldInfo(alias="requestHash", default=None)

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)

    result_id: Optional[str] = FieldInfo(alias="resultId", default=None)
    """Compatibility result ID for other write actions."""

    send_dispatched_at: Optional[datetime] = FieldInfo(alias="sendDispatchedAt", default=None)
    """Dispatch timestamp when the write reached execution."""

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
    """Compatibility field for a confirmed tweet result ID."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
