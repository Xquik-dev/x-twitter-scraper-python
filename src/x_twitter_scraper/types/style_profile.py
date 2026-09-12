# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .style_profile_summary import StyleProfileSummary

__all__ = ["StyleProfile", "StyleProfileTweet"]


class StyleProfileTweet(BaseModel):
    id: str

    text: str

    author_username: Optional[str] = FieldInfo(alias="authorUsername", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)


class StyleProfile(StyleProfileSummary):
    """Full style profile with sampled tweets used for tone analysis."""

    tweets: List[StyleProfileTweet]
