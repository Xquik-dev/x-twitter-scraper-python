# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractionRetrieveParams"]


class ExtractionRetrieveParams(TypedDict, total=False):
    after: str
    """Cursor for pagination"""

    limit: int
