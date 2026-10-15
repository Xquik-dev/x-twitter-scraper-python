# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["XGetTrendsParams"]


class XGetTrendsParams(TypedDict, total=False):
    at: str
    """A past time, to read what was trending on Twitter then.

    Takes an ISO 8601 time, a date such as 2026-10-13, or Unix seconds. A time
    without a zone reads as UTC. It also takes a span back from now, as a number &
    s, m, h or d. So at=24h reads what was trending on Twitter yesterday at this
    hour, on every run of a schedule. The answer is the stored list nearest that
    time, with its own time in capturedAt. History starts 2026-10-13 02:20 UTC. A
    time over 24 hours from every stored list answers 400 at no charge.
    """

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
