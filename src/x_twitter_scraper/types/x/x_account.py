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
    """Derived health.

    `healthy` is ready. `needsReauth` needs credentials. `locked` must be unlocked
    on X. `suspended` is banned. `recovering` can reconnect. Wait before using
    `temporaryIssue`.
    """

    status: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")

    cookies_obtained_at: Optional[datetime] = FieldInfo(alias="cookiesObtainedAt", default=None)
