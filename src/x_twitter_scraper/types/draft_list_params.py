# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DraftListParams"]


class DraftListParams(TypedDict, total=False):
    after_cursor: Annotated[str, PropertyInfo(alias="afterCursor")]
    """Cursor for pagination"""

    limit: int
    """Maximum number of items to return (1-100, default 50).

    For paid per-result endpoints, the returned count may be lower when remaining
    credits cannot cover the requested page. If zero paid results are affordable,
    the endpoint returns 402 insufficient_credits.
    """
