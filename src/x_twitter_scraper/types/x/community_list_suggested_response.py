# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from ..._models import BaseModel
from ..shared.community import Community

__all__ = ["CommunityListSuggestedResponse"]


class CommunityListSuggestedResponse(BaseModel):
    communities: List[Community]
    """Suggested communities in X's order"""

    count: int
    """Communities returned & charged"""

    message: Optional[str] = None
    """What to do next. Present only when X suggests none."""
