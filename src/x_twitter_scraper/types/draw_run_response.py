# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DrawRunResponse", "Winner"]


class Winner(BaseModel):
    author_username: str = FieldInfo(alias="authorUsername")

    is_backup: bool = FieldInfo(alias="isBackup")

    position: int

    tweet_id: str = FieldInfo(alias="tweetId")


class DrawRunResponse(BaseModel):
    id: str

    total_entries: int = FieldInfo(alias="totalEntries")

    tweet_id: str = FieldInfo(alias="tweetId")

    valid_entries: int = FieldInfo(alias="validEntries")

    winners: List[Winner]
