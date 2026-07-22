# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserRetrieveBatchParams"]


class UserRetrieveBatchParams(TypedDict, total=False):
    ids: Required[str]
    """Comma-separated numeric user IDs (1-100 values).

    Duplicate IDs are ignored while preserving first-seen order.
    """
