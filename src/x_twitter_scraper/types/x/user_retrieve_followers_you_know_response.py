# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["UserRetrieveFollowersYouKnowResponse"]


class UserRetrieveFollowersYouKnowResponse(BaseModel):
    has_next_page: bool

    next_cursor: str

    users: List[object]
