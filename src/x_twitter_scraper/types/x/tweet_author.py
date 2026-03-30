# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetAuthor"]


class TweetAuthor(BaseModel):
    id: str

    followers: int

    username: str

    verified: bool

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
