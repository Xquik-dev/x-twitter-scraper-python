# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContentDisclosure", "Advertising", "AIGenerated"]


class Advertising(BaseModel):
    is_paid_promotion: Optional[bool] = FieldInfo(alias="isPaidPromotion", default=None)
    """True when X labels the tweet as paid promotion content."""


class AIGenerated(BaseModel):
    can_edit: Optional[bool] = FieldInfo(alias="canEdit", default=None)
    """Whether the disclosure can be edited on X."""

    detection_source: Optional[str] = FieldInfo(alias="detectionSource", default=None)
    """Source of the AI-generated media disclosure."""

    has_ai_generated_media: Optional[bool] = FieldInfo(alias="hasAiGeneratedMedia", default=None)
    """True when X labels the tweet as containing AI-generated media."""


class ContentDisclosure(BaseModel):
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid partnership content or AI-generated media.
    """

    advertising: Optional[Advertising] = None

    ai_generated: Optional[AIGenerated] = FieldInfo(alias="aiGenerated", default=None)
