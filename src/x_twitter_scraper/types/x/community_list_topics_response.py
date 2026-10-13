# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.community_topic import CommunityTopic

__all__ = ["CommunityListTopicsResponse"]


class CommunityListTopicsResponse(BaseModel):
    count: int
    """Top-level topics returned & charged"""

    topics: List[CommunityTopic]
    """Topics in X's order"""

    message: Optional[str] = None
    """What to do next. Present only when X lists no topic."""
