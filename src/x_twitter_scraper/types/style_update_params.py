# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["StyleUpdateParams", "Tweet"]


class StyleUpdateParams(TypedDict, total=False):
    tweets: Required[Iterable[Tweet]]
    """Array of tweet objects"""

    label: str
    """Optional display label of up to 50 characters.

    When sent, it must match the path ID, ignoring case and a leading @. When it is
    left out, the path ID names the style and must fit the same limit.
    """


class Tweet(TypedDict, total=False):
    text: Required[str]
