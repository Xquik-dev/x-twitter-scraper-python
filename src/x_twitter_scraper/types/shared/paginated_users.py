# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_profile import UserProfile

__all__ = ["PaginatedUsers"]


class PaginatedUsers(BaseModel):
    """Paginated user profiles.

    The item count can be lower than pageSize when the source returns fewer profiles or remaining credits cover fewer results. Follow next_cursor while has_next_page is true. A relationship can naturally contain fewer profiles than requested. Zero affordable results returns 402 insufficient_credits.
    """

    has_next_page: bool

    next_cursor: str

    users: List[UserProfile]
