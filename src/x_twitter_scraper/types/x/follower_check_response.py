# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FollowerCheckResponse"]


class FollowerCheckResponse(BaseModel):
    is_followed_by: bool = FieldInfo(alias="isFollowedBy")

    is_following: bool = FieldInfo(alias="isFollowing")

    source_username: str = FieldInfo(alias="sourceUsername")

    target_username: str = FieldInfo(alias="targetUsername")
    """The target account's username, in lower case."""

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)
    """The source account's user ID, as X gives it."""

    target_id: Optional[str] = FieldInfo(alias="targetId", default=None)
    """The target account's user ID, as X gives it."""
