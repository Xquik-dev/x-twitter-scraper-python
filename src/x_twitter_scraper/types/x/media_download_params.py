# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MediaDownloadParams"]


class MediaDownloadParams(TypedDict, total=False):
    image_shows: Annotated[str, PropertyInfo(alias="imageShows")]
    """Save only posts whose photos show this.

    Send charts, screenshots, product_photos, memes or people, or describe it in words,
    such as a rocket. AI-powered analysis checks posts with photos X doesn't mark
    sensitive & keeps scores of 0.5 or more. Each post saved costs 2 credits, the AI
    analysis price, on top of its save price, & a post the filter drops costs nothing.
    imageFilter states the cutoff & counts.
    """

    tweet_id: Annotated[str, PropertyInfo(alias="tweetId")]
    """Numeric tweet ID alias for tweetInput"""

    tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tweetIds")]
    """Tweet URLs or IDs.

    An item that names no post gets 400 `invalid_tweet_id`, which says which item.
    Posts Xquik had no time to read come back in `unprocessedTweetIds`, with no
    charge. Send them again.
    """

    tweet_input: Annotated[str, PropertyInfo(alias="tweetInput")]
    """Tweet URL or ID (single tweet)"""

    tweet_url: Annotated[str, PropertyInfo(alias="tweetUrl")]
    """Tweet URL alias for tweetInput"""
