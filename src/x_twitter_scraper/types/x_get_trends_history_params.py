# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XGetTrendsHistoryParams"]


class XGetTrendsHistoryParams(TypedDict, total=False):
    count: int
    """Trends to return in each list, from 1 to 50."""

    country: str
    """
    Country to read trends history for, by name or 2-letter code, such as Turkey or
    TR. Case insensitive.
    """

    cursor: str
    """The next_cursor of the page before, for the next lists.

    It keeps the time of the first request, so a range of spans stays the same on
    every page.
    """

    every: str
    """Step between 2 returned lists, as a number & m, h or d, such as 15m, 1h or 1d.

    A step under 5m returns every stored list.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Start of the range.

    Takes an ISO 8601 time, a date such as 2026-10-13, or Unix seconds. A time
    without a zone reads as UTC. It also takes a span back from now, as a number &
    s, m, h or d, so from=7d reads the last 7 days. Defaults to 24 hours before to.
    History starts 2026-10-13 02:20 UTC, and a range that begins earlier returns the
    stored part. Alias sinceTime.
    """

    limit: int
    """Maximum lists 1 request returns & charges.

    A wider range gives a next_cursor for the next lists. A low credit balance can
    return fewer.
    """

    location: str
    """Town or country to read trends history for, by name, such as Istanbul.

    Case insensitive. Add country when 2 towns share a name. /x/trends/locations
    lists every name.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    to: str
    """End of the range, which it leaves out.

    Takes the forms of from, so from=2d with to=1d reads the day before the last 24
    hours. Defaults to now. Alias untilTime.
    """

    woeid: int
    """WOEID of the place, such as 1 for Worldwide or 23424969 for Turkey.

    It wins over country & location. /x/trends/locations lists every WOEID.
    """
