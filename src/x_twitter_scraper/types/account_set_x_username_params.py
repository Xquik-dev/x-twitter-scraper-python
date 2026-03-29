# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountSetXUsernameParams"]


class AccountSetXUsernameParams(TypedDict, total=False):
    username: Required[str]
    """X username without @"""
