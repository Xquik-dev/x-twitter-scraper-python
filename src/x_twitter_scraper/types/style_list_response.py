# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .style_profile_summary import StyleProfileSummary

__all__ = ["StyleListResponse"]


class StyleListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    styles: List[StyleProfileSummary]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
