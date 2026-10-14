# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XGetHashflagsParams"]


class XGetHashflagsParams(TypedDict, total=False):
    active_only: Annotated[bool, PropertyInfo(alias="activeOnly")]
    """Keeps hashflags that run now. Send false to add ended & upcoming ones."""

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    limit: int
    """Maximum hashflags to return.

    Omit it for every match. Credits can return fewer. Aliases pageSize, count,
    max_results, maxItems, max_items & per_page.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    q: str
    """Text the hashtag contains, such as football.

    Case insensitive. A leading hash sign is ignored. Alias query.
    """
