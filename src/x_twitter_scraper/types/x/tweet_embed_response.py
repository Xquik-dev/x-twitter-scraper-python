# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetEmbedResponse", "Embed"]


class Embed(BaseModel):
    """Holds the HTML that embeds one tweet on a website."""

    author_name: str = FieldInfo(alias="authorName")
    """Display name of the tweet's author."""

    author_url: str = FieldInfo(alias="authorUrl")
    """Link to the author's profile."""

    html: str
    """Markup to place on a page.

    It loads X's widget script unless `omitScript` is `true`.
    """

    tweet_id: str = FieldInfo(alias="tweetId")
    """ID of the embedded tweet."""

    url: str
    """Link to the tweet with its author's username."""

    height: Optional[int] = None
    """Height in pixels, when X fixes it."""

    width: Optional[int] = None
    """Width of the embed in pixels."""


class TweetEmbedResponse(BaseModel):
    embed: Embed
    """Holds the HTML that embeds one tweet on a website."""
