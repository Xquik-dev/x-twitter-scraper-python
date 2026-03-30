# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SearchTweet", "Author"]


class Author(BaseModel):
    id: str

    name: str

    username: str

    verified: Optional[bool] = None


class SearchTweet(BaseModel):
    id: str

    text: str

    author: Optional[Author] = None

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)
