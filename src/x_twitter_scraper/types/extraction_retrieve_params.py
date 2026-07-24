# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractionRetrieveParams"]


class ExtractionRetrieveParams(TypedDict, total=False):
    cursor: str
    """Cursor for keyset pagination from prior response next_cursor"""

    limit: int
    """Maximum number of results to return (1-1000, default 100)"""
