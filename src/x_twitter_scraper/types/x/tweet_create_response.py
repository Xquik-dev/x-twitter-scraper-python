# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetCreateResponse"]


class TweetCreateResponse(BaseModel):
    success: Literal[True]

    tweet_id: str = FieldInfo(alias="tweetId")
