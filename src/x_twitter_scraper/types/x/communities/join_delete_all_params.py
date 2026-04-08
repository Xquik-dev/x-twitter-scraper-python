# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JoinDeleteAllParams"]


class JoinDeleteAllParams(TypedDict, total=False):
    account: Required[str]
    """X account identifier (@username or account ID)"""
