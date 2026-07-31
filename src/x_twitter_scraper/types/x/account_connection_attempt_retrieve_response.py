# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AccountConnectionAttemptRetrieveResponse",
    "XAccountConnectionAttemptPending",
    "XAccountConnectionAttemptSuccess",
    "XAccountConnectionAttemptFailed",
    "XAccountConnectionChallenge",
]


class XAccountConnectionAttemptPending(BaseModel):
    """The connection is still in progress."""

    id: str

    object: Literal["x_account_connection_attempt"]

    poll_after_ms: int = FieldInfo(alias="pollAfterMs")

    status: Literal["pending"]


class XAccountConnectionAttemptSuccess(BaseModel):
    """The account connected successfully."""

    id: str

    object: Literal["x_account_connection_attempt"]

    status: Literal["success"]


class XAccountConnectionAttemptFailed(BaseModel):
    """The connection reached a final failure."""

    id: str

    error: str

    object: Literal["x_account_connection_attempt"]

    retryable: bool

    status: Literal["failed"]

    reason: Optional[str] = None


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


AccountConnectionAttemptRetrieveResponse: TypeAlias = Annotated[
    Union[
        XAccountConnectionAttemptPending,
        XAccountConnectionAttemptSuccess,
        XAccountConnectionAttemptFailed,
        XAccountConnectionChallenge,
    ],
    PropertyInfo(discriminator="status"),
]
