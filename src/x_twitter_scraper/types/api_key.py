# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_active: bool = FieldInfo(alias="isActive")

    name: str

    prefix: str

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
