# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetEmbedParams"]


class TweetEmbedParams(TypedDict, total=False):
    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    hide_media: Annotated[bool, PropertyInfo(alias="hideMedia")]
    """Set `true` to leave photos, videos, and link cards out."""

    hide_thread: Annotated[bool, PropertyInfo(alias="hideThread")]
    """Set `true` to leave the tweet this one replies to out."""

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    omit_script: Annotated[bool, PropertyInfo(alias="omitScript")]
    """
    Set `true` to leave the widget script tag out, for pages that load it once
    themselves.
    """

    theme: Literal["light", "dark"]
    """Color theme of the embed. X uses light when left out."""
