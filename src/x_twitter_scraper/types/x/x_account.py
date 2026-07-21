# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["XAccount"]


class XAccount(BaseModel):
    """
    Linked X account summary with connection status, health, and timestamp metadata.
    """

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    health: Literal["healthy", "locked", "needsReauth", "recovering", "suspended", "temporaryIssue"]
    """Derived connection health.

    `healthy` = session active. `needsReauth` = user must submit fresh credentials.
    `locked` = X locked the account; unlock on x.com first. `suspended` = X banned
    the account. `recovering` = past cooldown, will auto-retry on next use.
    `temporaryIssue` = temporary connection problem; retry shortly.
    """

    status: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")

    cookies_obtained_at: Optional[datetime] = FieldInfo(alias="cookiesObtainedAt", default=None)
