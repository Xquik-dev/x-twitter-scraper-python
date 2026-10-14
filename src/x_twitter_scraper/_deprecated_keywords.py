# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import warnings

from ._types import Omit

__all__ = ["min_likes_or_min_faves"]


def min_likes_or_min_faves(min_likes: int | Omit, min_faves: int | Omit) -> int | Omit:
    if isinstance(min_faves, Omit):
        return min_likes
    warnings.warn(
        "min_faves is deprecated & goes away in a later minor version. Use min_likes.",
        DeprecationWarning,
        stacklevel=3,
    )
    return min_faves if isinstance(min_likes, Omit) else min_likes
