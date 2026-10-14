# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from .winner import Winner
from .._models import BaseModel
from .draw_detail import DrawDetail

__all__ = ["DrawRetrieveResponse"]


class DrawRetrieveResponse(BaseModel):
    draw: DrawDetail
    """Full giveaway draw with tweet metrics, entries, and timing."""

    winners: List[Winner]
