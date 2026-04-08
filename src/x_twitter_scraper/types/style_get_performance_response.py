# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StyleGetPerformanceResponse", "Tweet"]


class Tweet(BaseModel):
    id: str

    text: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)


class StyleGetPerformanceResponse(BaseModel):
    tweet_count: int = FieldInfo(alias="tweetCount")

    tweets: List[Tweet]

    x_username: str = FieldInfo(alias="xUsername")
