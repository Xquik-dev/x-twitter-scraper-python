# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TweetListParams"]


class TweetListParams(TypedDict, total=False):
    ids: Required[str]
    """1 to 100 posts, separated by commas.

    Each is a tweet ID or a tweet URL, such as x.com/nasa/status/20. A post named
    twice is read once. Any other entry is skipped & listed under `skipped` with
    why. A batch without 1 post gets 400 `invalid_tweet_id`.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """
