# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types.x import CommunityRetrieveAnalyticsParams
from x_twitter_scraper.types.shared import CommunityAnalytics, CommunityAnalyticsMetric
from x_twitter_scraper.types.shared.community_analytics import Metrics

COMMUNITY_ANALYTICS = {
    "id": "1493446837214187523",
    "periodEndsAt": "2026-10-16T23:59:59.999Z",
    "metrics": {
        "likes": {"count": 15298, "changePercent": -1.2076202776880853},
        "newMembers": {"count": 557, "changePercent": -1.5901060070671376},
        "posts": {"count": 5108, "changePercent": 0.5907837731390311},
        "replies": {"count": 6851, "changePercent": -0.8251302837290099},
        "uniquePosters": {"count": 1800, "changePercent": -0.33222591362126247},
    },
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_community_analytics_sends_filters_and_reads_every_metric(asynchronous: bool) -> None:
    arguments: CommunityRetrieveAnalyticsParams = {
        "fields": "id,periodEndsAt,metrics",
        "omit": "metrics.likes.changePercent",
    }
    request, analytics = await send_with_mock_transport(
        lambda client: client.x.communities.retrieve_analytics("1493446837214187523", **arguments),
        lambda client: client.x.communities.retrieve_analytics("1493446837214187523", **arguments),
        COMMUNITY_ANALYTICS,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/x/communities/1493446837214187523/analytics"
    assert dict(request.url.params) == {
        "fields": "id,periodEndsAt,metrics",
        "omit": "metrics.likes.changePercent",
    }
    assert isinstance(analytics, CommunityAnalytics)
    assert analytics.id == "1493446837214187523"
    assert analytics.period_ends_at == datetime(2026, 10, 16, 23, 59, 59, 999000, tzinfo=timezone.utc)
    metrics = analytics.metrics
    assert isinstance(metrics, Metrics)
    for metric, count, change_percent in (
        (metrics.likes, 15298, -1.2076202776880853),
        (metrics.new_members, 557, -1.5901060070671376),
        (metrics.posts, 5108, 0.5907837731390311),
        (metrics.replies, 6851, -0.8251302837290099),
        (metrics.unique_posters, 1800, -0.33222591362126247),
    ):
        assert isinstance(metric, CommunityAnalyticsMetric)
        assert metric.count == count
        assert metric.change_percent == change_percent


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_community_analytics_without_filters_sends_no_query(asynchronous: bool) -> None:
    request, analytics = await send_with_mock_transport(
        lambda client: client.x.communities.retrieve_analytics("1493446837214187523"),
        lambda client: client.x.communities.retrieve_analytics("1493446837214187523"),
        COMMUNITY_ANALYTICS,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/communities/1493446837214187523/analytics"
    assert request.url.query == b""
    assert analytics.metrics.likes.count == 15298
