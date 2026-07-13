# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetCreateResponse"]


class TweetCreateResponse(BaseModel):
    charged: bool

    charged_credits: str = FieldInfo(alias="chargedCredits")
    """Credits charged for this tweet.

    Text-only tweets and replies cost 30 credits; attached media adds 2 credits per
    started MB.
    """

    success: Literal[True]

    tweet_id: str = FieldInfo(alias="tweetId")

    write_action_id: Optional[str] = FieldInfo(alias="writeActionId", default=None)
