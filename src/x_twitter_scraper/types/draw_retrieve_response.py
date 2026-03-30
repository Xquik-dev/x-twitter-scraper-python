# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .winner import Winner
from .._models import BaseModel
from .draw_detail import DrawDetail

__all__ = ["DrawRetrieveResponse"]


class DrawRetrieveResponse(BaseModel):
    draw: DrawDetail

    winners: List[Winner]
