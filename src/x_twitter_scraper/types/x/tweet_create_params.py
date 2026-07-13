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
    """Array of public media URLs to attach.

    Supports up to 4 images or exactly 1 MP4 video up to 100 MB. Each URL must be
    publicly reachable. Attached media adds 2 credits per started MB across all
    files.
    """

    reply_to_tweet_id: str

    text: str
    """Tweet text (optional when media is provided)"""
