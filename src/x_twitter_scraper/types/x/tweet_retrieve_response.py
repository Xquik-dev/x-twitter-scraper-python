# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from .tweet_detail import TweetDetail

__all__ = ["TweetRetrieveResponse"]


class TweetRetrieveResponse(BaseModel):
    tweet: TweetDetail

    author: Optional[TweetAuthor] = None
