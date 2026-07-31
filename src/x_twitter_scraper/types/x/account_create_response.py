# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccountCreateResponse",
    "SanitizedXAccount",
    "XAccountConnectionAttemptPending",
    "XAccountConnectionChallenge",
]


class SanitizedXAccount(BaseModel):
    """Sanitized X account summary returned by connect and reauth."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    health: Literal["healthy", "locked", "needsReauth", "recovering", "suspended", "temporaryIssue"]

    status: Literal["active"]

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")


class XAccountConnectionAttemptPending(BaseModel):
    """The connection is still in progress."""

    id: str

    object: Literal["x_account_connection_attempt"]

    poll_after_ms: int = FieldInfo(alias="pollAfterMs")

    status: Literal["pending"]


class XAccountConnectionChallenge(BaseModel):
    """Resumable account connection challenge.

    Submit the email code to finish the same connection attempt.
    """

    id: str

    expires_at: datetime = FieldInfo(alias="expiresAt")

    message: str

    object: Literal["x_account_connection_challenge"]

    status: Literal["requires_email_code"]

    username: str


AccountCreateResponse: TypeAlias = Union[
    SanitizedXAccount, XAccountConnectionAttemptPending, XAccountConnectionChallenge
]
