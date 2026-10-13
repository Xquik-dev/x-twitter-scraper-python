# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.community import (
    Rule as CommunityRule,
    Community,
    PrimaryTopic as CommunityPrimaryTopic,
    CreatorUnionMember1 as CommunityCreator,
)

__all__ = ["CommunityRetrieveInfoResponse", "Community", "CommunityCreator", "CommunityPrimaryTopic", "CommunityRule"]


class CommunityRetrieveInfoResponse(BaseModel):
    community: Community
    """Public X Community, as every Community read returns it."""
