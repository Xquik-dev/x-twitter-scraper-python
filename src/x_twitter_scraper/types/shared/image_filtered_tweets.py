# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from pydantic import Field as FieldInfo

from .search_tweet import SearchTweet
from .paginated_tweets import PaginatedTweets
from .image_filter_summary import ImageFilterSummary

__all__ = ["ImageFilteredTweets", "ImageScoredTweet"]


class ImageScoredTweet(SearchTweet):
    image_score: float = FieldInfo(alias="imageScore")
    """How likely a photo shows what you asked for."""


class ImageFilteredTweets(PaginatedTweets):
    """Posts kept by the image filter.

    Each kept post carries its imageScore. Follow next_cursor to check the next posts.
    """

    image_filter: ImageFilterSummary = FieldInfo(alias="imageFilter")
    """What the image filter asked & how many posts it kept."""

    tweets: List[ImageScoredTweet]  # type: ignore
