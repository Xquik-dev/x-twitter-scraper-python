# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_profile import UserProfile

__all__ = ["PaginatedUsers"]


class PaginatedUsers(BaseModel):
    """Paginated user profiles.

    No-mode follower, following, and verified follower requests merge independent views automatically. Response fields, page size, aliases, filters, and per-returned-profile billing stay unchanged. Existing unprefixed cursors retain legacy behavior. Follow next_cursor while has_next_page is true.
    """

    has_next_page: bool

    next_cursor: str

    users: List[UserProfile]
