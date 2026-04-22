# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TweetCreateParams"]


class TweetCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    attachment_url: str

    community_id: str

    is_note_tweet: bool

    media: SequenceNotStr[str]
    """Array of media URLs to attach (mutually exclusive with media_ids)"""

    media_ids: SequenceNotStr[str]
    """Array of media IDs to attach (mutually exclusive with media)"""

    reply_to_tweet_id: str

    text: str
    """Tweet text (optional when media is provided)"""
