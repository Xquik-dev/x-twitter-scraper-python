# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from ..._models import BaseModel

__all__ = ["TopicFilterSummary", "TopicFilterSummaryUnchecked"]


class TopicFilterSummaryUnchecked(BaseModel):
    id: str

    reason: str


class TopicFilterSummary(BaseModel):
    """What the topic filter asked & how many posts it kept."""

    checked: int
    """Posts checked.

    Only kept posts are billed.
    """

    cutoff: float
    """The lowest topicScore a kept post has."""

    kept: int
    """Posts about the topic, all returned & billed at 2 credits each."""

    question: str
    """The question asked of each post."""

    topic: str
    """The topic you sent."""

    unchecked: List[TopicFilterSummaryUnchecked]
    """Posts the check couldn't answer.

    They aren't billed or returned.
    """
