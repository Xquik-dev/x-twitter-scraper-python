# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .x_account import XAccount

__all__ = ["AccountListResponse"]


class AccountListResponse(BaseModel):
    accounts: List[XAccount]

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Present on cursor-paginated responses."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Pass unchanged as cursor when hasMore is true."""
