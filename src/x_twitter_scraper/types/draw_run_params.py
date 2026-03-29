# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DrawRunParams"]


class DrawRunParams(TypedDict, total=False):
    tweet_url: Required[Annotated[str, PropertyInfo(alias="tweetUrl")]]

    backup_count: Annotated[int, PropertyInfo(alias="backupCount")]

    filter_account_age_days: Annotated[int, PropertyInfo(alias="filterAccountAgeDays")]

    filter_language: Annotated[str, PropertyInfo(alias="filterLanguage")]

    filter_min_followers: Annotated[int, PropertyInfo(alias="filterMinFollowers")]

    must_follow_username: Annotated[str, PropertyInfo(alias="mustFollowUsername")]

    must_retweet: Annotated[bool, PropertyInfo(alias="mustRetweet")]

    required_hashtags: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredHashtags")]

    required_keywords: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredKeywords")]

    required_mentions: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredMentions")]

    unique_authors_only: Annotated[bool, PropertyInfo(alias="uniqueAuthorsOnly")]

    winner_count: Annotated[int, PropertyInfo(alias="winnerCount")]
