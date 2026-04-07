# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetHomeTimelineResponse", "Tweet", "TweetAuthor"]


class TweetAuthor(BaseModel):
    id: str

    name: str

    username: str

    verified: Optional[bool] = None


class Tweet(BaseModel):
    id: str

    text: str

    author: Optional[TweetAuthor] = None

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)
    """Whether this is a Note Tweet (long-form post, up to 25,000 characters)"""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)


class XGetHomeTimelineResponse(BaseModel):
    has_next_page: bool

    next_cursor: str

    tweets: List[Tweet]
