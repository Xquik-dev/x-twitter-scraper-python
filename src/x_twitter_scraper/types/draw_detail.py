# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from pydantic import Field as FieldInfo

from .draw_list_item import DrawListItem

__all__ = ["DrawDetail"]


class DrawDetail(DrawListItem):
    """Full giveaway draw with tweet metrics, entries, and timing."""

    tweet_author_username: str = FieldInfo(alias="tweetAuthorUsername")

    tweet_id: str = FieldInfo(alias="tweetId")

    tweet_like_count: int = FieldInfo(alias="tweetLikeCount")
    """Whole number from 0."""

    tweet_quote_count: int = FieldInfo(alias="tweetQuoteCount")
    """Whole number from 0."""

    tweet_reply_count: int = FieldInfo(alias="tweetReplyCount")
    """Whole number from 0."""

    tweet_retweet_count: int = FieldInfo(alias="tweetRetweetCount")
    """Whole number from 0."""

    tweet_text: str = FieldInfo(alias="tweetText")
