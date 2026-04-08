# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetGetRetweetersResponse", "User"]


class User(BaseModel):
    """X user profile with bio, follower counts, and verification status."""

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


class TweetGetRetweetersResponse(BaseModel):
    """Paginated list of user profiles with cursor-based navigation."""

    has_next_page: bool

    next_cursor: str

    users: List[User]
