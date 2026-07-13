# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.user_profile import UserProfile

__all__ = ["TweetAuthor"]


class TweetAuthor(UserProfile):
    """Tweet author profile.

    The lookup route always includes follower count and verification state. Other profile fields appear when available.
    """

    pass
