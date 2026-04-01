# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DrawRetrieveResponse", "Draw", "Winner"]


class Draw(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    total_entries: int = FieldInfo(alias="totalEntries")

    tweet_author_username: str = FieldInfo(alias="tweetAuthorUsername")

    tweet_id: str = FieldInfo(alias="tweetId")

    tweet_like_count: int = FieldInfo(alias="tweetLikeCount")

    tweet_quote_count: int = FieldInfo(alias="tweetQuoteCount")

    tweet_reply_count: int = FieldInfo(alias="tweetReplyCount")

    tweet_retweet_count: int = FieldInfo(alias="tweetRetweetCount")

    tweet_text: str = FieldInfo(alias="tweetText")

    tweet_url: str = FieldInfo(alias="tweetUrl")

    valid_entries: int = FieldInfo(alias="validEntries")

    drawn_at: Optional[datetime] = FieldInfo(alias="drawnAt", default=None)


class Winner(BaseModel):
    author_username: str = FieldInfo(alias="authorUsername")

    is_backup: bool = FieldInfo(alias="isBackup")

    position: int

    tweet_id: str = FieldInfo(alias="tweetId")


class DrawRetrieveResponse(BaseModel):
    draw: Draw

    winners: List[Winner]
