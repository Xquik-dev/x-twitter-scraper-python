# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetGetQuotesResponse", "Tweet", "TweetAuthor"]


class TweetAuthor(BaseModel):
    id: str

    name: str

    username: str

    verified: Optional[bool] = None


class Tweet(BaseModel):
    """Tweet returned from search results with inline author info."""

    id: str

    text: str

    author: Optional[TweetAuthor] = None

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)
    """True for Note Tweets (long-form content, up to 25,000 characters)"""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)


class TweetGetQuotesResponse(BaseModel):
    """Paginated list of tweets with cursor-based navigation."""

    has_next_page: bool

    next_cursor: str

    tweets: List[Tweet]
