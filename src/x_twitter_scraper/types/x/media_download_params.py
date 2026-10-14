# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MediaDownloadParams"]


class MediaDownloadParams(TypedDict, total=False):
    tweet_id: Annotated[str, PropertyInfo(alias="tweetId")]
    """Numeric tweet ID alias for tweetInput"""

    tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tweetIds")]
    """Up to 50 tweet URLs or IDs.

    An item that names no post gets 400 `invalid_tweet_id`, which says which item.
    """

    tweet_input: Annotated[str, PropertyInfo(alias="tweetInput")]
    """Tweet URL or ID (single tweet)"""

    tweet_url: Annotated[str, PropertyInfo(alias="tweetUrl")]
    """Tweet URL alias for tweetInput"""
