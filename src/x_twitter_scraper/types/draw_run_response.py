# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .winner import Winner
from .._models import BaseModel

__all__ = ["DrawRunResponse"]


class DrawRunResponse(BaseModel):
    id: str

    total_entries: int = FieldInfo(alias="totalEntries")
    """
    Entries inspected after the credit cap, which can be fewer than the post's
    replies.
    """

    tweet_id: str = FieldInfo(alias="tweetId")

    valid_entries: int = FieldInfo(alias="validEntries")
    """Inspected entries that passed every filter.

    A credit cap can leave valid replies uninspected.
    """

    winners: List[Winner]
