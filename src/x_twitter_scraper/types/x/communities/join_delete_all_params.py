# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JoinDeleteAllParams"]


class JoinDeleteAllParams(TypedDict, total=False):
    account: Required[str]
    """X account identifier (@username or account ID)"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
