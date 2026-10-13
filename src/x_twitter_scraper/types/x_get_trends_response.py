# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetTrendsResponse", "Trend", "Location"]


class Trend(BaseModel):
    name: str

    description: Optional[str] = None

    promoted_content: Optional[str] = FieldInfo(alias="promotedContent", default=None)
    """Promotion identifier from X. Null for organic trends."""

    query: Optional[str] = None

    rank: Optional[int] = None

    tweet_volume: Optional[int] = FieldInfo(alias="tweetVolume", default=None)
    """Approximate public post volume when X supplies it."""

    url: Optional[str] = None
    """X search URL for the trend."""


class Location(BaseModel):
    """The place country or location named.

    Absent when woeid picked the place or the request named none.
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


class XGetTrendsResponse(BaseModel):
    count: int

    trends: List[Trend]

    woeid: int

    location: Optional[Location] = None
    """The place country or location named.

    Absent when woeid picked the place or the request named none.
    """
