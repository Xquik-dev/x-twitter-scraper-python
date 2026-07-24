# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ComposeCreateResponse",
    "ComposePrepareResult",
    "ComposePrepareResultContentRule",
    "ComposePrepareResultEngagementMultiplier",
    "ComposePrepareResultScorerWeight",
    "ComposePrepareResultSavedStyle",
    "ComposeRefineResult",
    "ComposeRefineResultExamplePattern",
    "ComposeScoreResult",
    "ComposeScoreResultChecklist",
]


class ComposePrepareResultContentRule(BaseModel):
    rule: str


class ComposePrepareResultEngagementMultiplier(BaseModel):
    action: str
    """Human-readable published signal name."""

    multiplier: Literal["Production weight not published by X"]


class ComposePrepareResultScorerWeight(BaseModel):
    context: str
    """Signal direction and publication limit."""

    signal: str
    """Signal name from X's public ranking repository."""

    weight: None = None
    """X does not publish the production weight."""


class ComposePrepareResultSavedStyle(BaseModel):
    tweet_count: int = FieldInfo(alias="tweetCount")

    username: str


class ComposePrepareResult(BaseModel):
    content_rules: List[ComposePrepareResultContentRule] = FieldInfo(alias="contentRules")
    """Xquik editorial heuristics, ordered for the goal."""

    engagement_multipliers: List[ComposePrepareResultEngagementMultiplier] = FieldInfo(alias="engagementMultipliers")
    """Published engagement signal names. Production multipliers are not published."""

    engagement_velocity: str = FieldInfo(alias="engagementVelocity")
    """Publication limit for timing and decay claims."""

    follow_up_questions: List[str] = FieldInfo(alias="followUpQuestions")

    intent_url: str = FieldInfo(alias="intentUrl")
    """X post intent seeded with the topic."""

    next_step: str = FieldInfo(alias="nextStep")

    scorer_weights: List[ComposePrepareResultScorerWeight] = FieldInfo(alias="scorerWeights")
    """Published signal names with unpublished weights as null."""

    source: str
    """Signal source and evidence limits."""

    top_penalties: List[str] = FieldInfo(alias="topPenalties")
    """Negative engagement predictions in the public model."""

    saved_styles: Optional[List[ComposePrepareResultSavedStyle]] = FieldInfo(alias="savedStyles", default=None)
    """Style analyses saved to the account."""

    style_note: Optional[str] = FieldInfo(alias="styleNote", default=None)
    """Next action when no cached style is available."""

    style_tweets: Optional[List[str]] = FieldInfo(alias="styleTweets", default=None)
    """Cached examples for the requested style username."""


class ComposeRefineResultExamplePattern(BaseModel):
    description: str

    pattern: str


class ComposeRefineResult(BaseModel):
    composition_guidance: List[str] = FieldInfo(alias="compositionGuidance")
    """Goal, tone, media, and editorial guidance."""

    example_patterns: List[ComposeRefineResultExamplePattern] = FieldInfo(alias="examplePatterns")

    intent_url: str = FieldInfo(alias="intentUrl")
    """X post intent seeded with the topic."""

    next_step: str = FieldInfo(alias="nextStep")


class ComposeScoreResultChecklist(BaseModel):
    factor: str

    passed: bool

    suggestion: Optional[str] = None
    """Present only when the check fails."""


class ComposeScoreResult(BaseModel):
    checklist: List[ComposeScoreResultChecklist]
    """Deterministic editorial checks. Not a reach prediction."""

    next_step: str = FieldInfo(alias="nextStep")

    passed: bool

    passed_count: int = FieldInfo(alias="passedCount")

    top_suggestion: str = FieldInfo(alias="topSuggestion")

    total_checks: Literal[9] = FieldInfo(alias="totalChecks")

    intent_url: Optional[str] = FieldInfo(alias="intentUrl", default=None)
    """Present only when every check passes."""


ComposeCreateResponse: TypeAlias = Union[ComposePrepareResult, ComposeRefineResult, ComposeScoreResult]
