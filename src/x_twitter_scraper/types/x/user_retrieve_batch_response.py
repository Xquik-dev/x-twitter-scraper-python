# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.user_profile import UserProfile

__all__ = ["UserRetrieveBatchResponse"]


class UserRetrieveBatchResponse(BaseModel):
    """Batch user lookup results.

    Duplicate requested IDs are ignored while preserving first-seen order. unavailable_ids identifies processed IDs with no returned profile. unprocessed_ids identifies IDs skipped when available credits limit processing.
    """

    has_next_page: Literal[False]
    """Batch lookups never paginate."""

    next_cursor: str
    """Empty because batch lookups never paginate."""

    processed_count: int
    """Number of requested IDs included in the lookup."""

    requested_count: int
    """Number of unique IDs requested."""

    returned_count: int
    """Number of user profiles returned and charged."""

    unavailable_ids: List[str]
    """Processed IDs with no returned profile, in first-seen request order."""

    unprocessed_ids: List[str]
    """Requested IDs skipped because available credits limited processing.

    Retry these IDs after adding credits.
    """

    users: List[UserProfile]
