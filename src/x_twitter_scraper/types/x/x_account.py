# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["XAccount"]


class XAccount(BaseModel):
    """Linked X account summary with username and connection status."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    health: Literal["healthy", "locked", "needsReauth", "recovering", "suspended", "temporaryIssue"]
    """Derived login/cookie health.

    `healthy` = cookies valid. `needsReauth` = user must submit fresh credentials.
    `locked` = X locked the account; unlock on x.com first. `suspended` = X banned
    the account. `recovering` = past cooldown, will auto-retry on next use.
    `temporaryIssue` = transient backend problem; retry shortly.
    """

    status: str

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")
