# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .x_account_connection_link import XAccountConnectionLink

__all__ = ["AccountConnectionLinkListResponse"]


class AccountConnectionLinkListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    links: List[XAccountConnectionLink]
    """Your connect links, newest first."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Pass unchanged as cursor when has_more is true."""
