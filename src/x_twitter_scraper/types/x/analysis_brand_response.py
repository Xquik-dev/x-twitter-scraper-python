# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet

__all__ = [
    "AnalysisBrandResponse",
    "AnalysisSummary",
    "AnalysisSummaryCashtag",
    "AnalysisSummaryCashtagSignal",
    "AnalysisSummaryMonitor",
    "AnalysisSummaryMonitorChangedRow",
    "AnalysisSummaryMonitorChangedRowChange",
    "AnalysisSummaryRows",
    "AnalysisSummarySourceDomain",
    "AnalysisSummaryTarget",
    "Result",
    "ResultAnalysis",
    "ResultAnalysisAnswer",
    "ResultAnalysisContextAvailability",
    "ResultAnalysisQuestion",
    "ResultMonitor",
    "ResultMonitorChange",
    "Unanalyzed",
]


class AnalysisSummaryCashtagSignal(BaseModel):
    bearish: int

    bullish: int

    score: float
    """Bullish minus bearish posts, over all posts."""


class AnalysisSummaryCashtag(BaseModel):
    cashtag: str

    choices: Dict[str, object]
    """Category counts of the cashtag's posts by question ID."""

    rows: int

    signal: Optional[AnalysisSummaryCashtagSignal] = None


class AnalysisSummaryMonitorChangedRowChange(BaseModel):
    current: str

    previous: str

    question_id: str = FieldInfo(alias="questionId")


class AnalysisSummaryMonitorChangedRow(BaseModel):
    changes: List[AnalysisSummaryMonitorChangedRowChange]

    tweet_id: str = FieldInfo(alias="tweetId")


class AnalysisSummaryMonitor(BaseModel):
    """Posts per comparison status, & up to 50 changed posts with their changes.

    Null when the answer holds no post.
    """

    changed_rows: List[AnalysisSummaryMonitorChangedRow] = FieldInfo(alias="changedRows")

    statuses: Dict[str, int]
    """Posts per monitor status."""


class AnalysisSummaryRows(BaseModel):
    """Posts by analysis outcome."""

    analyzed: int

    failed: int

    skipped: int


class AnalysisSummarySourceDomain(BaseModel):
    domain: str

    posts: int


class AnalysisSummaryTarget(BaseModel):
    choices: Dict[str, object]
    """Category counts by question ID."""

    engagement: int

    mentions: int

    name: str

    share: float

    top: Dict[str, object]
    """The most engaged posts per question ID & category."""


class AnalysisSummary(BaseModel):
    """Totals of the answers across the analyzed posts."""

    cashtags: List[AnalysisSummaryCashtag]
    """Posts & answers per cashtag, most posts first, up to 20.

    signal is present for the market questions.
    """

    engagement: int
    """Likes, reposts, replies & quotes of the analyzed posts."""

    monitor: Optional[AnalysisSummaryMonitor] = None
    """Posts per comparison status, & up to 50 changed posts with their changes.

    Null when the answer holds no post.
    """

    questions: Dict[str, Dict[str, object]]
    """Totals by question ID.

    A choice has counts, shares, engagementShares & top posts per category. A score
    has mean, engagementWeightedMean & levels. A probability has mean, yes & no.
    """

    rows: AnalysisSummaryRows
    """Posts by analysis outcome."""

    schema_version: int = FieldInfo(alias="schemaVersion")

    source_domains: List[AnalysisSummarySourceDomain] = FieldInfo(alias="sourceDomains")
    """Posts per linked hostname, most posts first, up to 20."""

    targets: List[AnalysisSummaryTarget]
    """Mentions & answers per target in analysis.targets."""

    viral: Optional[Dict[str, object]] = None
    """Only from /x/analysis/viral-score.

    Scored posts, the average score, verdict counts, the scores against actual
    engagement, a report per author & the leaderboards.
    """


class ResultAnalysisAnswer(BaseModel):
    """1 question's answer.

    A probability has probability. A choice or score has value, confidence & the probability of each category or level.
    """

    question_id: str = FieldInfo(alias="questionId")

    question_version: str = FieldInfo(alias="questionVersion")

    type: Literal["choice", "score", "probability"]

    confidence: Optional[float] = None

    levels: Optional[List[str]] = None
    """For a score. The levels the question named, from 0."""

    probabilities: Optional[Dict[str, float]] = None
    """Probability of each category, or of each level by index."""

    probability: Optional[float] = None
    """For a probability. The chance the answer is yes."""

    value: Union[str, float, None] = None
    """
    The chosen category, or the level from 0, which can have decimals, such as 1.4
    between levels 1 & 2.
    """


class ResultAnalysisContextAvailability(BaseModel):
    """What the AI read beside the post's text."""

    article: Literal["text_blocks", "summary", "not_supplied"]

    author: Literal["available", "missing"]

    media: Literal["text_descriptions_only", "not_supplied"]

    post_text: Literal["full", "truncated"] = FieldInfo(alias="postText")
    """truncated when the post was cut to fit."""

    quote: Literal["available", "missing", "not_applicable"]

    reply: Literal["available", "missing", "not_applicable"]


class ResultAnalysisQuestion(BaseModel):
    id: str

    version: str


class ResultAnalysis(BaseModel):
    """The answers in full, with their probabilities."""

    answers: List[ResultAnalysisAnswer]
    """1 answer per question, in question order."""

    context_availability: ResultAnalysisContextAvailability = FieldInfo(alias="contextAvailability")
    """What the AI read beside the post's text."""

    context_bytes: int = FieldInfo(alias="contextBytes")
    """Bytes of post & settings the AI read."""

    questions: List[ResultAnalysisQuestion]
    """The ID & version of each question asked."""

    status: Literal["succeeded"]


class ResultMonitorChange(BaseModel):
    current: str

    previous: str

    question_id: str = FieldInfo(alias="questionId")


class ResultMonitor(BaseModel):
    """
    How the post's answers compare with its row in baseline, as the AI Actors compare a run with an earlier dataset.
    """

    baseline_dataset_id: None = None
    """Always null. The baseline is the rows you sent."""

    changed_question_ids: List[str] = FieldInfo(alias="changedQuestionIds")
    """IDs of the questions whose decision changed."""

    changes: List[ResultMonitorChange]
    """Each changed decision, earlier & now."""

    configuration_fingerprint: str = FieldInfo(alias="configurationFingerprint")
    """Hash of the questions, targets & context.

    Rows with another hash are not_comparable.
    """

    status: Literal["first_run", "new_to_baseline", "unchanged", "changed", "not_comparable", "analysis_unavailable"]
    """first_run without baseline.

    new_to_baseline for a post baseline lacks. changed when an answer clearly left
    its earlier decision. not_comparable when other settings made the earlier row or
    it answers none of these questions.
    """


class Result(BaseModel):
    """1 analyzed post with its answers."""

    analysis: ResultAnalysis
    """The answers in full, with their probabilities."""

    answers: Dict[str, Union[str, float]]
    """Each question's decision by question ID.

    A choice gives its category, a score its level from 0, which can have decimals,
    & a probability its value from 0 to 1.
    """

    cashtags: List[str]
    """Cashtags in the post's text, in upper case."""

    monitor: ResultMonitor
    """
    How the post's answers compare with its row in baseline, as the AI Actors
    compare a run with an earlier dataset.
    """

    source_domains: List[str] = FieldInfo(alias="sourceDomains")
    """Hostnames the post links to, without t.co."""

    tweet: SearchTweet
    """The post, as /x/tweets/search returns it.

    Your own texts have the IDs text:1, text:2 & so on.
    """

    viral: Optional[Dict[str, object]] = None
    """Only from /x/analysis/viral-score.

    The score with its weights version, the caps that applied & the engagement
    comparison.
    """

    viral_actual_engagement_rate: Optional[float] = FieldInfo(alias="viralActualEngagementRate", default=None)
    """Only from /x/analysis/viral-score.

    log10 of 1 plus the weighted engagement per 1,000 followers. Null without a
    follower count.
    """

    viral_algorithm_score: Optional[float] = FieldInfo(alias="viralAlgorithmScore", default=None)
    """Only from /x/analysis/viral-score.

    The post's public counts under X's published ranking weights, per 1,000 views or
    followers.
    """

    viral_score: Optional[int] = FieldInfo(alias="viralScore", default=None)
    """Only from /x/analysis/viral-score.

    How viral the wording reads, or null when a trait has no answer.
    """

    viral_verdict: Optional[Literal["send_it", "edit_first", "sleep_on_it"]] = FieldInfo(
        alias="viralVerdict", default=None
    )
    """Only from /x/analysis/viral-score.

    send_it from 70, edit_first from 40, else sleep_on_it.
    """


class Unanalyzed(BaseModel):
    """A post without an analysis. It costs nothing."""

    id: str
    """Post ID. Your own texts have the IDs text:1, text:2 & so on."""

    reason: str
    """post_unavailable when X returns no such post.

    missing_text for a post without text. insufficient_credits when credits ran out.
    context_limit when the settings leave the post no room. The other reasons mean
    the analysis failed. Send the post again.
    """

    status: Literal["failed", "skipped"]


class AnalysisBrandResponse(BaseModel):
    """Analyzed posts, the posts without an analysis & the totals of the answers.

    Each row in results costs 2 credits.
    """

    analysis_summary: AnalysisSummary = FieldInfo(alias="analysisSummary")
    """Totals of the answers across the analyzed posts."""

    has_next_page: bool
    """Whether the search has more posts. Send next_cursor as cursor."""

    next_cursor: str
    """Cursor of the search's next page, else empty."""

    results: List[Result]
    """Each analyzed post with its answers."""

    unanalyzed: List[Unanalyzed]
    """Each post without an analysis, by ID & reason. These cost nothing."""
