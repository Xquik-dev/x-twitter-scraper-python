# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SpaceRetrieveReplayResponse", "Replay"]


class Replay(BaseModel):
    """Recording of an ended Space"""

    url: str
    """HLS playlist of the recording"""

    status: Optional[str] = None
    """Stream status, as X names it"""

    stream_type: Optional[str] = FieldInfo(alias="streamType", default=None)
    """Stream format, as X names it"""


class SpaceRetrieveReplayResponse(BaseModel):
    replay: Replay
    """Recording of an ended Space"""
