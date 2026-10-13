# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..shared.user_profile import UserProfile

__all__ = ["TweetAuthor"]


class TweetAuthor(UserProfile):
    """Author profile.

    Lookups always include follower count & verification. Other fields depend on availability.
    """

    followers: int  # type: ignore

    verified: bool  # type: ignore
