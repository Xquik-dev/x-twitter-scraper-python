# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StyleCompareParams"]


class StyleCompareParams(TypedDict, total=False):
    username1: Required[str]
    """First username to compare"""

    username2: Required[str]
    """Second username to compare"""
