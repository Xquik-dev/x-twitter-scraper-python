# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FollowerCheckParams"]


class FollowerCheckParams(TypedDict, total=False):
    source: Required[str]
    """Source username, @username, or X or Twitter profile URL"""

    target: Required[str]
    """Target username, @username, or X or Twitter profile URL"""
