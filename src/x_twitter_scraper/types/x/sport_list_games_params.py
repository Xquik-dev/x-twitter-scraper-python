# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SportListGamesParams"]


class SportListGamesParams(TypedDict, total=False):
    fields: str
    """Fields to keep in each row, comma-separated. Use dots for nested fields, such
    as author.username. A list keeps the field in each item. Case & underscores do
    not matter. A row that lacks a field leaves it out. Cursors, counts &
    diagnostics always stay. An unknown name answers 400 unknown_field with the
    valid names, before any read. The price stays the same. SDK row types then
    hold only the named fields.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Start of the window. Takes an ISO 8601 date or time, such as 2026-10-01, or
    Unix seconds. A time without a zone reads as UTC. Defaults to 7 days before
    to. Alias sinceTime.
    """

    omit: str
    """Fields to drop from each row, comma-separated. It takes the same names as
    fields. With fields, it drops from the kept fields.
    """

    team: str
    """Keeps only 1 team's games, by team ID. Each game lists its teamIds. Aliases
    teamId & team_id.
    """

    to: str
    """End of the window. Takes the forms of from. Defaults to 7 days after from.
    Alias untilTime.
    """
