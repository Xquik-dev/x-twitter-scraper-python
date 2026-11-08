# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Union
from typing_extensions import TypeAlias

from ..shared.paginated_tweets import PaginatedTweets
from ..shared.image_filtered_tweets import ImageFilteredTweets
from ..shared.topic_filtered_tweets import TopicFilteredTweets

__all__ = ["UserRetrieveTweetsResponse"]

UserRetrieveTweetsResponse: TypeAlias = Union[TopicFilteredTweets, ImageFilteredTweets, PaginatedTweets]
