# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StyleCompareResponse", "Style1", "Style1Tweet", "Style2", "Style2Tweet"]


class Style1Tweet(BaseModel):
    id: str

    text: str

    author_username: Optional[str] = FieldInfo(alias="authorUsername", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)


class Style1(BaseModel):
    """Full style profile with sampled tweets used for tone analysis."""

    fetched_at: datetime = FieldInfo(alias="fetchedAt")

    is_own_account: bool = FieldInfo(alias="isOwnAccount")

    tweet_count: int = FieldInfo(alias="tweetCount")

    tweets: List[Style1Tweet]

    x_username: str = FieldInfo(alias="xUsername")


class Style2Tweet(BaseModel):
    id: str

    text: str

    author_username: Optional[str] = FieldInfo(alias="authorUsername", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)


class Style2(BaseModel):
    """Full style profile with sampled tweets used for tone analysis."""

    fetched_at: datetime = FieldInfo(alias="fetchedAt")

    is_own_account: bool = FieldInfo(alias="isOwnAccount")

    tweet_count: int = FieldInfo(alias="tweetCount")

    tweets: List[Style2Tweet]

    x_username: str = FieldInfo(alias="xUsername")


class StyleCompareResponse(BaseModel):
    style1: Style1
    """Full style profile with sampled tweets used for tone analysis."""

    style2: Style2
    """Full style profile with sampled tweets used for tone analysis."""
