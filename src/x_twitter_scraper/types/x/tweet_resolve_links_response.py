# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetResolveLinksResponse", "Link"]


class Link(BaseModel):
    """Pairs one t.co link with the URL it leads to."""

    url: str
    """The t.co link, as `https://t.co/<code>`."""

    resolved_url: Optional[str] = FieldInfo(alias="resolvedUrl", default=None)
    """Target URL, as the link's author set it.

    Xquik does not check it. Absent for a link t.co does not have.
    """


class TweetResolveLinksResponse(BaseModel):
    links: List[Link]

    unprocessed_urls: List[str] = FieldInfo(alias="unprocessedUrls")
    """Links not read, in the order sent.

    X did not answer for them in time, or available credits ran out. Send them
    again.
    """
