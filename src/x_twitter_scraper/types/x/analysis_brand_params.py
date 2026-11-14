# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "AnalysisBrandParams",
    "Analysis",
    "AnalysisQuestion",
    "AnalysisQuestionCriteria",
    "AnalysisTarget",
    "Baseline",
    "BaselineMonitor",
    "BaselineTweet",
]


class AnalysisBrandParams(TypedDict, total=False):
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
    """The next_cursor of the page before. Send the same search or page with it."""

    image_shows: Annotated[str, PropertyInfo(alias="imageShows")]
    """Keep only posts whose photos show this, the same as the Actors' imageShows input.

    Send charts, screenshots, product_photos, memes or people, or describe it in
    words, such as a rocket. AI-powered analysis checks posts with photos X doesn't
    mark sensitive & keeps scores of 0.5 or more. Only kept posts are analyzed &
    cost 2 credits each. imageFilter states the cutoff & counts. Send topic or
    imageShows, not both.
    """

    liked_by: Annotated[str, PropertyInfo(alias="likedBy")]
    """Analyze the posts 1 account liked, as /x/users/{id}/likes reads them.

    Send a handle, with or without @, a user ID or a profile URL. Send no other
    posts or search with it.
    """

    limit: int
    """Maximum posts to analyze from the search or page. Credits can return fewer."""

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Analyze a public List's posts. Send its ID or URL."""

    list_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="listIds")]
    """Analyze the posts of several public Lists in 1 search.

    Send their IDs or URLs. listId, when sent, joins them.
    """

    media_by: Annotated[str, PropertyInfo(alias="mediaBy")]
    """Analyze 1 account's posts with photos or videos, as its Media tab shows them.

    /x/users/{id}/media reads the same posts. Send a handle, with or without @, a
    user ID or a profile URL. Send no other posts or search with it.
    """

    queries: SequenceNotStr[str]
    """X searches to analyze as 1 search.

    A post matching any of them counts. Each takes the operators of query. query,
    when sent, joins them. X searches up to 512 characters, counted with the other
    search fields.
    """

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

    replies_by: Annotated[str, PropertyInfo(alias="repliesBy")]
    """Analyze 1 account's posts & replies, as its Replies tab shows them.

    /x/users/{id}/replies reads the same posts. Send a handle, with or without @, a
    user ID or a profile URL. Send no other posts or search with it.
    """

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

    thread_of: Annotated[str, PropertyInfo(alias="threadOf")]
    """Analyze 1 post's thread, as /x/tweets/{id}/thread reads it.

    Send the post's ID or URL. Send no other posts or search with it.
    """

    topic: str
    """Keep only posts about this topic, the same as the Actors' topic input.

    AI-powered analysis asks "Is this post about <topic>?" of each post & keeps
    scores of 0.5 or more. Only kept posts are analyzed & cost 2 credits each, & a
    post the filter drops costs nothing. topicFilter states the cutoff & counts.
    Send topic or imageShows, not both.
    """

    tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="tweetIds")]
    """Post IDs or post URLs to analyze, up to 100."""

    until_time: Annotated[Union[str, int], PropertyInfo(alias="untilTime")]
    """Exclusive end of the search, such as 2026-09-26T00:00:00Z.

    Unix seconds also work. A time without an offset is UTC.
    """

    username: str
    """Analyze 1 account's posts. Send a handle, with or without @, or a profile URL."""

    usernames: SequenceNotStr[str]
    """Analyze the posts of several accounts in 1 search.

    Send handles, with or without @, or profile URLs. username, when sent, joins
    them.
    """


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

    images: bool
    """Reads up to 4 images per post with its text, at no extra cost.

    Images of posts X marks sensitive stay unread. Send false to analyze the text
    alone.
    """

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
