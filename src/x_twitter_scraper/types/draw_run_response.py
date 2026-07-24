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
    """Candidate entries inspected for this draw after the credit-derived cap.

    This may be lower than the source tweet's full reply count.
    """

    tweet_id: str = FieldInfo(alias="tweetId")

    valid_entries: int = FieldInfo(alias="validEntries")
    """Entries from the inspected candidate set that passed all filters.

    This is not necessarily every valid reply on the source tweet when credits cap
    inspection.
    """

    winners: List[Winner]
