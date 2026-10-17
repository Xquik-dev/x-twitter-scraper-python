# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommunityNotesRatingOutcome"]


class CommunityNotesRatingOutcome(BaseModel):
    """A group of a contributor's ratings, by what each one said."""

    helpful_count: Optional[int] = FieldInfo(alias="helpfulCount", default=None)
    """Ratings that called a note helpful."""

    not_helpful_count: Optional[int] = FieldInfo(alias="notHelpfulCount", default=None)
    """Ratings that called a note not helpful."""

    total: Optional[int] = None
    """All ratings in the group, when X sends the sum."""
