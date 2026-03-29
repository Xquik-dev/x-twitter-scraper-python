# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetRetrieveResponse", "Tweet", "Author"]


class Tweet(BaseModel):
    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)


class Author(BaseModel):
    id: str

    followers: int

    username: str

    verified: bool

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)


class TweetRetrieveResponse(BaseModel):
    tweet: Tweet

    author: Optional[Author] = None
