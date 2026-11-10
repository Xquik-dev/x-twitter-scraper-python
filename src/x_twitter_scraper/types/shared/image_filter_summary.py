# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ImageFilterSummary", "ImageFilterSummaryUnchecked"]


class ImageFilterSummaryUnchecked(BaseModel):
    id: str

    reason: str


class ImageFilterSummary(BaseModel):
    """What the image filter asked & how many posts it kept."""

    checked: int
    """Posts whose photos were checked.

    Only kept posts are billed.
    """

    cutoff: float
    """The lowest imageScore a kept post has."""

    image_shows: str = FieldInfo(alias="imageShows")
    """What you asked the photos to show."""

    kept: int
    """Posts whose photos show it, all returned & billed at 2 credits each."""

    question: str
    """The question asked of each post's photos."""

    unchecked: List[ImageFilterSummaryUnchecked]
    """Posts without a safe photo & posts the check couldn't answer.

    They aren't billed or returned.
    """
