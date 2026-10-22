# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor. The after alias also works. Offset pagination is not
    supported.
    """

    limit: int
    """Maximum items per page, from 1 to 200. Default 200. Pass nextCursor as cursor
    for the next page.
    """
