# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StyleUpdateResponse", "Tweet"]


class Tweet(BaseModel):
    id: str

    text: str

    author_username: Optional[str] = FieldInfo(alias="authorUsername", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)


class StyleUpdateResponse(BaseModel):
    fetched_at: datetime = FieldInfo(alias="fetchedAt")

    is_own_account: bool = FieldInfo(alias="isOwnAccount")

    tweet_count: int = FieldInfo(alias="tweetCount")

    tweets: List[Tweet]

    x_username: str = FieldInfo(alias="xUsername")
