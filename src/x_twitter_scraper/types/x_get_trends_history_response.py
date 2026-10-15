# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetTrendsHistoryResponse", "Snapshot", "SnapshotTrend", "Location"]


class SnapshotTrend(BaseModel):
    name: str

    description: Optional[str] = None

    promoted_content: Optional[str] = FieldInfo(alias="promotedContent", default=None)
    """X's promotion ID of a promoted trend. Null for the others."""

    query: Optional[str] = None

    rank: Optional[int] = None
    """The trend's place in X's list at that time."""

    tweet_volume: Optional[int] = FieldInfo(alias="tweetVolume", default=None)
    """X's post count for the trend at that time, when X showed one."""

    url: Optional[str] = None
    """The trend's search link on X."""


class Snapshot(BaseModel):
    captured_at: datetime = FieldInfo(alias="capturedAt")
    """When Xquik read this stored list from X. Xquik never estimates it."""

    count: int
    """Trends in this list."""

    trends: List[SnapshotTrend]


class Location(BaseModel):
    """The place the request named by country or location.

    Absent when it sent a woeid or named no place.
    """

    country: Optional[str] = None
    """Country name. Null for Worldwide."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """2-letter country code. Null for Worldwide."""

    name: str

    parent_woeid: Optional[int] = FieldInfo(alias="parentWoeid", default=None)
    """WOEID of the country or region above it. Null for Worldwide."""

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)
    """X's kind of place. Town, Country, Supername for Worldwide, or Unknown."""

    place_type_code: Optional[int] = FieldInfo(alias="placeTypeCode", default=None)
    """X's numeric code for the kind of place."""

    url: Optional[str] = None
    """X's legacy Yahoo GeoPlanet reference. It may not resolve."""

    woeid: int
    """Location ID. Pass it as woeid to /x/trends."""


class XGetTrendsHistoryResponse(BaseModel):
    count: int
    """Lists returned & charged."""

    from_time: datetime = FieldInfo(alias="fromTime")
    """Start of the range as Xquik read it.

    A span such as 7d shows here as the time it counted back to.
    """

    has_next_page: bool
    """Whether the range holds more lists."""

    next_cursor: str
    """Send it as cursor for the next lists. Empty on the last page."""

    snapshots: List[Snapshot]
    """1 stored list per step, oldest first. A step with no stored list is left out."""

    to_time: datetime = FieldInfo(alias="toTime")
    """End of the range as Xquik read it, which the range leaves out.

    Without to, it is the time of the first request.
    """

    woeid: int

    location: Optional[Location] = None
    """The place the request named by country or location.

    Absent when it sent a woeid or named no place.
    """
