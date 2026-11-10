# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["XAccountConnectionLink"]


class XAccountConnectionLink(BaseModel):
    """A link where a person connects an X account on Xquik's page."""

    id: str

    account_id: Optional[str] = FieldInfo(alias="accountId")

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt")

    created_at: datetime = FieldInfo(alias="createdAt")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    failure: Optional[str]
    """Why the last login didn't finish."""

    health: Optional[str]

    object: Literal["x_account_connection_link"]

    purpose: Literal["connect", "reconnect"]

    reference: Optional[str]

    return_url: Optional[str] = FieldInfo(alias="returnUrl")

    status: Literal["pending", "connecting", "requires_email_code", "connected", "failed", "expired", "revoked"]
    """`failed` means 5 logins were refused, so make a new link."""

    x_user_id: Optional[str] = FieldInfo(alias="xUserId")

    x_username: Optional[str] = FieldInfo(alias="xUsername")

    url: Optional[str] = None
    """Present only in the response that creates the link."""
