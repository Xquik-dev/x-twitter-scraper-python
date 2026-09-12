# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveBatchParams"]


class UserRetrieveBatchParams(TypedDict, total=False):
    ids: Required[str]
    """Comma-separated numeric user IDs (1-100 values).

    Duplicate IDs are ignored while preserving first-seen order.
    """

    max_followers: Annotated[int, PropertyInfo(alias="maxFollowers")]
    """Maximum follower count. Missing counts pass this maximum."""

    min_account_age_days: Annotated[int, PropertyInfo(alias="minAccountAgeDays")]
    """Minimum account age in whole days."""

    min_followers: Annotated[int, PropertyInfo(alias="minFollowers")]
    """Minimum follower count. Filtering happens before billing."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return verified profiles."""
