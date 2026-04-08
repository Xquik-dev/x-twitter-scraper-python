# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractionRetrieveParams"]


class ExtractionRetrieveParams(TypedDict, total=False):
    after: str
    """Cursor for keyset pagination"""

    limit: int
    """Maximum number of results to return (1-1000, default 100)"""
