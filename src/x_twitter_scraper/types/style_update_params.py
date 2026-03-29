# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["StyleUpdateParams", "Tweet"]


class StyleUpdateParams(TypedDict, total=False):
    label: Required[str]
    """Display label for the style"""

    tweets: Required[Iterable[Tweet]]
    """Array of tweet objects"""


class Tweet(TypedDict, total=False):
    text: Required[str]
