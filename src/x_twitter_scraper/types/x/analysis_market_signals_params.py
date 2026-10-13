# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "AnalysisMarketSignalsParams",
    "Analysis",
    "AnalysisQuestion",
    "AnalysisQuestionCriteria",
    "AnalysisTarget",
    "Baseline",
    "BaselineMonitor",
    "BaselineTweet",
]


class AnalysisMarketSignalsParams(TypedDict, total=False):
    analysis: Analysis
    """Analysis settings, the same as the analysis input of Xquik's AI Actors.

    Leave it out for the route's own questions.
    """

    baseline: Iterable[Baseline]
    """Rows of an earlier answer to compare with, such as its results.

    Each needs the post's id, or tweet.id, & its answers. Send monitor too, so other
    settings show as not_comparable. Each result's monitor says whether the post is
    new, changed or unchanged. The comparison costs nothing extra.
    """

    cursor: str
    """The next_cursor of the page before. Send the same search with it."""

    limit: int
    """Maximum posts to analyze from the search. Credits can return fewer."""

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Analyze a public List's posts. Send its ID or URL."""

    query: str
    """
    X search to analyze, with the operators of /x/tweets/search, such as from:nasa
    or lang:en. X searches up to 512 characters, counted with the other search
    fields, as /x/tweets/search counts q.
    """

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Search order. Default Latest."""

    quotes_of: Annotated[str, PropertyInfo(alias="quotesOf")]
    """Analyze the quotes of 1 post. Send its ID or URL."""

    replies_to: Annotated[str, PropertyInfo(alias="repliesTo")]
    """Analyze the replies in 1 post's conversation. Send its ID or URL."""

    since_time: Annotated[Union[str, int], PropertyInfo(alias="sinceTime")]
    """Inclusive start of the search, such as 2026-09-25T00:00:00Z.

    Unix seconds also work. A time without an offset is UTC.
    """

    texts: SequenceNotStr[str]
    """Your own texts to analyze, such as drafts.

    Reads nothing from X. Each text costs the same as 1 analyzed post.
    """

    tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tweetIds")]
    """Post IDs or post URLs to analyze, up to 100."""

    until_time: Annotated[Union[str, int], PropertyInfo(alias="untilTime")]
    """Exclusive end of the search, such as 2026-09-26T00:00:00Z.

    Unix seconds also work. A time without an offset is UTC.
    """

    username: str
    """Analyze 1 account's posts. Send a handle, with or without @, or a profile URL."""


class AnalysisQuestionCriteria(TypedDict, total=False):
    """For a probability. What counts as yes & as no."""

    no: Required[str]

    yes: Required[str]


class AnalysisQuestion(TypedDict, total=False):
    """A question the AI answers for each post.

    A choice picks 1 of 2 to 255 categories, a score picks 1 of 2 or more ordered levels & a probability answers yes or no.
    """

    id: Required[str]
    """Name of the answer, such as request.

    A name the response renames or drops gets a 400, such as created_at,
    favorite_count, muting or blocking.
    """

    instructions: Required[str]
    """The question, as the AI reads it."""

    type: Required[Literal["choice", "score", "probability"]]

    version: Required[str]
    """Your version of the question, such as 1."""

    categories: Dict[str, str]
    """For a choice. Each category name with its description, or null."""

    criteria: AnalysisQuestionCriteria
    """For a probability. What counts as yes & as no."""

    levels: SequenceNotStr[str]
    """For a score. Each level's description, lowest first."""


class AnalysisTarget(TypedDict, total=False):
    name: Required[str]

    aliases: SequenceNotStr[str]


class Analysis(TypedDict, total=False):
    """Analysis settings, the same as the analysis input of Xquik's AI Actors.

    Leave it out for the route's own questions.
    """

    concurrency: int
    """Posts analyzed at the same time."""

    context: str
    """Background the AI reads with every post."""

    max_context_bytes: Annotated[int, PropertyInfo(alias="maxContextBytes")]
    """Bytes of post, quote & settings the AI reads.

    Longer posts are cut to fit. Empty settings take 219 bytes, so a smaller value
    gets a 400.
    """

    preset: Literal[
        "brand",
        "complaints",
        "competitors",
        "purchase_intent",
        "product_feedback",
        "news",
        "sentiment",
        "market",
        "viral_lite",
    ]
    """A ready set of questions, used when questions is left out.

    complaints, competitors, purchase_intent & product_feedback need targets.
    viral_lite scores how viral the wording reads.
    """

    questions: Iterable[AnalysisQuestion]
    """Your own questions, which replace the route's questions.

    Write question IDs & category names in lower case without hyphens.
    """

    targets: Iterable[AnalysisTarget]
    """
    Brands, people, assets or topics the questions are about, each with its aliases.
    """


class BaselineMonitor(TypedDict, total=False):
    """The earlier row's monitor, with its fingerprint."""

    configuration_fingerprint: Annotated[str, PropertyInfo(alias="configurationFingerprint")]


class BaselineTweet(TypedDict, total=False):
    id: Required[str]


class Baseline(TypedDict, total=False):
    answers: Required[Dict[str, Union[str, float]]]
    """The earlier answers by question ID."""

    id: str
    """Post ID, or text:1 & so on. Else tweet.id counts."""

    monitor: BaselineMonitor
    """The earlier row's monitor, with its fingerprint."""

    tweet: BaselineTweet
