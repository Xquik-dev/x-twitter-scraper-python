# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from pydantic import Field as FieldInfo

from .search_tweet import SearchTweet
from .paginated_tweets import PaginatedTweets
from .topic_filter_summary import TopicFilterSummary

__all__ = ["TopicFilteredTweets", "TopicScoredTweet"]


class TopicScoredTweet(SearchTweet):
    topic_score: float = FieldInfo(alias="topicScore")
    """How likely the post is about the topic."""


class TopicFilteredTweets(PaginatedTweets):
    """Posts kept by the topic filter.

    Each kept post carries its topicScore. Follow next_cursor to check the next posts.
    """

    topic_filter: TopicFilterSummary = FieldInfo(alias="topicFilter")
    """What the topic filter asked & how many posts it kept."""

    tweets: List[TopicScoredTweet]  # type: ignore
