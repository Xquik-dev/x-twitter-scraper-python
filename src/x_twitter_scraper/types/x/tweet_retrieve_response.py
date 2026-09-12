# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from .tweet_detail import TweetDetail

__all__ = ["TweetRetrieveResponse"]


class TweetRetrieveResponse(BaseModel):
    tweet: TweetDetail
    """Full tweet with text, engagement metrics, media, and metadata.

    A zero metric can mean X did not report the count.
    """

    author: Optional[TweetAuthor] = None
    """Tweet author profile.

    The lookup route always includes follower count and verification state. Other
    profile fields appear when available.
    """
