# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CommunityRetrieveAnalyticsParams"]


class CommunityRetrieveAnalyticsParams(TypedDict, total=False):
    fields: str
    """Keep named fields using comma-separated names and dots for nested fields.

    Field names ignore case and underscores. Unknown names return an error before any read.
    The price stays the same.
    """

    omit: str
    """Drop named fields using comma-separated names and dots for nested fields.

    Omit drops fields after fields selects them.
    """
