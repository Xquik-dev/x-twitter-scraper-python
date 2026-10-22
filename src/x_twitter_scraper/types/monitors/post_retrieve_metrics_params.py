# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostRetrieveMetricsParams"]


class PostRetrieveMetricsParams(TypedDict, total=False):
    hours: int
    """Hours to return, from 1 to 720."""
