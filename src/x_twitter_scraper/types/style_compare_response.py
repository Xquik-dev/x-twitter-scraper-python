# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .style_profile import StyleProfile

__all__ = ["StyleCompareResponse"]


class StyleCompareResponse(BaseModel):
    style1: StyleProfile

    style2: StyleProfile
