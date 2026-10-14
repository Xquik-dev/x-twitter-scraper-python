# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StyleProfileSummary"]


class StyleProfileSummary(BaseModel):
    """Style profile summary with tweet count and ownership flag."""

    fetched_at: datetime = FieldInfo(alias="fetchedAt")

    is_own_account: bool = FieldInfo(alias="isOwnAccount")

    tweet_count: int = FieldInfo(alias="tweetCount")

    x_username: str = FieldInfo(alias="xUsername")
