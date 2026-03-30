# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserProfile"]


class UserProfile(BaseModel):
    id: str

    name: str

    username: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    followers: Optional[int] = None

    following: Optional[int] = None

    location: Optional[str] = None

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    verified: Optional[bool] = None
