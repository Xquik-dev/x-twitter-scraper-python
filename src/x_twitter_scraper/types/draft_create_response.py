# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DraftCreateResponse"]


class DraftCreateResponse(BaseModel):
    """Full tweet draft including update timestamp."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    text: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    goal: Optional[str] = None

    topic: Optional[str] = None
