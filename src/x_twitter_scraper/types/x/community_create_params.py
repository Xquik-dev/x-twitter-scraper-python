# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunityCreateParams"]


class CommunityCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) creating the community"""

    name: Required[str]
    """Community name"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    description: str
    """Community description"""
