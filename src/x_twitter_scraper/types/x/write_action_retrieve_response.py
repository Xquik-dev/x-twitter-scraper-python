# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WriteActionRetrieveResponse", "Media"]


class Media(BaseModel):
    count: int

    credits: str

    kind: Literal["none", "image", "video"]

    total_bytes: str = FieldInfo(alias="totalBytes")


class WriteActionRetrieveResponse(BaseModel):
    action: str

    charged: bool

    charged_credits: str = FieldInfo(alias="chargedCredits")

    created_at: datetime = FieldInfo(alias="createdAt")

    media: Media

    retryable: Literal[False]

    send_dispatched: bool = FieldInfo(alias="sendDispatched")

    status: Literal["success", "failed", "pending_confirmation"]

    write_action_id: str = FieldInfo(alias="writeActionId")

    confirmation_attempts: Optional[int] = FieldInfo(alias="confirmationAttempts", default=None)

    confirmation_checked_at: Optional[datetime] = FieldInfo(alias="confirmationCheckedAt", default=None)

    confirmation_source: Optional[str] = FieldInfo(alias="confirmationSource", default=None)

    confirmed_at: Optional[datetime] = FieldInfo(alias="confirmedAt", default=None)

    message: Optional[str] = None

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    send_dispatched_at: Optional[datetime] = FieldInfo(alias="sendDispatchedAt", default=None)

    target_id: Optional[str] = FieldInfo(alias="targetId", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
