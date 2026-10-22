# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .post_monitor import PostMonitor

__all__ = ["PostListResponse"]


class PostListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    monitors: List[PostMonitor]

    total: int
    """Post monitors on this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
