# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SoftIntervention", "Text", "TextEntity", "TextEntityRef", "URL"]


class TextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class TextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[TextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class Text(BaseModel):
    entities: Optional[List[TextEntity]] = None
    """Links inside the label, by character range."""

    rtl: Optional[bool] = None
    """Whether the label reads right to left."""

    text: Optional[str] = None
    """The label's text."""


class URL(BaseModel):
    """The page that explains the label."""

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class SoftIntervention(BaseModel):
    """The label X shows under a post whose reach it limits.

    It links to the page that explains it.
    """

    display_type: Optional[str] = FieldInfo(alias="displayType", default=None)
    """The label's kind. `Fosnr` marks a post X keeps up but shows to fewer people."""

    engagement_nudge: Optional[bool] = FieldInfo(alias="engagementNudge", default=None)
    """Whether X prompts readers before they engage with the post."""

    text: Optional[Text] = None

    url: Optional[URL] = None
    """The page that explains the label."""
