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
    """Array of public image URLs to attach (max 4).

    Each URL must be publicly reachable - the browser composer fetches them
    directly.
    """

    reply_to_tweet_id: str

    text: str
    """Tweet text (optional when media is provided)"""
