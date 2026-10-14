# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TweetCreateParams"]


class TweetCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    community_id: str
    """The Community to post into, from 1 to 19 digits.

    The account must be a member. Xquik picks the Community in X's composer, checks
    the post request names it & reads the post after. A post X puts outside the
    Community is deleted & fails uncharged. Not with `reply_to_tweet_id`, since X
    keeps replies public.
    """

    is_note_tweet: bool

    media: SequenceNotStr[str]
    """Publicly reachable URLs of up to 4 images or exactly 1 MP4 video up to 100 MB.

    Media adds 2 credits per started MB across all files.
    """

    reply_to_tweet_id: str
    """The post to reply to. Any X post ID works, from 1 to 19 digits."""

    text: str
    """Tweet text (optional when media is provided)"""
