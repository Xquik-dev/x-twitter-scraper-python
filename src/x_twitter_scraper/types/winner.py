# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Winner"]


class Winner(BaseModel):
    author_username: str = FieldInfo(alias="authorUsername")

    is_backup: bool = FieldInfo(alias="isBackup")

    position: int

    tweet_id: str = FieldInfo(alias="tweetId")
