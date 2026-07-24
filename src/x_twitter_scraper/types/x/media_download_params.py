# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MediaDownloadParams"]


class MediaDownloadParams(TypedDict, total=False):
    tweet_id: Annotated[str, PropertyInfo(alias="tweetId")]
    """Numeric tweet ID alias for tweetInput"""

    tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tweetIds")]
    """Array of tweet URLs or IDs (bulk, max 50 string items)"""

    tweet_input: Annotated[str, PropertyInfo(alias="tweetInput")]
    """Tweet URL or ID (single tweet)"""

    tweet_url: Annotated[str, PropertyInfo(alias="tweetUrl")]
    """Tweet URL alias for tweetInput"""
