# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from .._models import BaseModel
from .style_profile import StyleProfile

__all__ = ["StyleCompareResponse"]


class StyleCompareResponse(BaseModel):
    style1: StyleProfile
    """Full style profile with sampled tweets used for tone analysis."""

    style2: StyleProfile
    """Full style profile with sampled tweets used for tone analysis."""
