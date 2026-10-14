# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XGetHomeTimelineParams"]


class XGetHomeTimelineParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    seen_tweet_ids: Annotated[str, PropertyInfo(alias="seenTweetIds")]
    """Comma-separated tweet IDs to exclude from results. Empty entries are ignored."""
