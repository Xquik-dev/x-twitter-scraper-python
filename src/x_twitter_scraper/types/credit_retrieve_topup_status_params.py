# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditRetrieveTopupStatusParams"]


class CreditRetrieveTopupStatusParams(TypedDict, total=False):
    session_id: Required[str]
    """Top-up session ID to inspect."""
