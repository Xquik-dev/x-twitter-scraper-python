# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["XGetTrendsParams"]


class XGetTrendsParams(TypedDict, total=False):
    count: int
    """Number of trending topics to return (1-50, default 30)"""

    country: str
    """Country to read trends for, by name or 2-letter code, such as Turkey or TR.

    Case insensitive.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    location: str
    """Town or country to read trends for, by name, such as Istanbul.

    Case insensitive. Add country when 2 towns share a name. /x/trends/locations
    lists every name.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    woeid: int
    """Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey).

    Wins over country & location.
    """
