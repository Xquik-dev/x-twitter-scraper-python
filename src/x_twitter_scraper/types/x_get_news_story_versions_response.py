# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetNewsStoryVersionsResponse", "Version"]


class Version(BaseModel):
    """1 version X wrote of a news story."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When X wrote the version, in UTC, from its ID."""

    headline: str
    """The story's headline in this version."""

    id: str
    """The version's ID."""

    text: str
    """
    The story's text in this version, without the time line X writes above it in the
    reader's time zone.
    """


class XGetNewsStoryVersionsResponse(BaseModel):
    count: int
    """Versions returned."""

    id: str
    """The story's ID, as the request named it."""

    versions: List[Version]
