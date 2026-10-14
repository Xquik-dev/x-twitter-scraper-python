# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from ..._models import BaseModel

__all__ = ["CommunityTopic", "Subtopic"]


class Subtopic(BaseModel):
    id: str
    """Subtopic ID, which topicId also takes"""

    name: str
    """Subtopic name, which topic also takes"""


class CommunityTopic(BaseModel):
    """A topic X groups communities under, with its subtopics."""

    id: str
    """Topic ID. Pass it as topicId to /x/communities/popular."""

    name: str
    """Topic name, which topic on /x/communities/popular takes"""

    subtopics: List[Subtopic]
    """Narrower topics inside this topic"""
