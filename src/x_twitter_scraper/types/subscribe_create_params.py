# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SubscribeCreateParams"]


class SubscribeCreateParams(TypedDict, total=False):
    tier: Literal["starter", "pro", "business"]
    """Subscription tier to pre-select."""
