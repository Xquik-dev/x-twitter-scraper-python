# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DmRetrieveHistoryParams"]


class DmRetrieveHistoryParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for DM history"""

    max_id: Annotated[str, PropertyInfo(alias="maxId")]
    """Legacy pagination cursor (backward compat)"""
