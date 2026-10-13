# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XGetTrendLocationsParams"]


class XGetTrendLocationsParams(TypedDict, total=False):
    country: str
    """Country name or 2-letter code, such as Turkey or TR.

    Case insensitive. Returns the country & its towns.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    limit: int
    """Maximum locations to return.

    Omit it for every match. Credits can return fewer. Aliases pageSize, count,
    max_results, maxItems, max_items & per_page.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    place_type: Annotated[Literal["country", "town", "worldwide", "unknown"], PropertyInfo(alias="placeType")]
    """Kind of place. Case insensitive. X labels a few towns unknown."""

    q: str
    """Text the location name contains, such as york. Case insensitive. Alias query."""
