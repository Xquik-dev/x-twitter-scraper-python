# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Dict

import pytest

from tests.utils import send_with_mock_transport

ACCOUNT: Dict[str, object] = {
    "userId": "11348282",
    "userName": "NASA",
    "followers": 92376187,
    "following": 180,
    "posts": 73919,
    "accountAgeDays": 6449,
    "postsPrivate": False,
    "sample": {"posts": 20, "oldestAt": "2026-10-28T13:15:28.000Z", "newestAt": "2026-11-02T22:12:05.000Z"},
    "averages": {
        "likes": 3684.2,
        "replies": 142.7,
        "reposts": 459.8,
        "quotes": 45,
        "bookmarks": 209.7,
        "views": 785247.8,
        "engagements": 4331.7,
    },
    "medianViews": 512330,
    "engagementRate": 0.0047,
    "engagementPerView": 0.55,
    "postsPerDay": 3.8,
    "topPostId": "1852301447063109847",
}
FOLLOWER: Dict[str, object] = {
    "id": "1852412278803021824",
    "userName": "orbit_watcher",
    "name": "Orbit Watcher",
    "class": "likelyReal",
    "score": 1,
    "signals": ["noBanner"],
    "followers": 312,
    "following": 410,
    "likes": 2840,
    "posts": 1290,
    "position": 1,
    "joinedAtMs": 1561939200000,
    "pictureUrl": "https://pbs.twimg.com/profile_images/1/photo.jpg",
}
AUDIT: Dict[str, object] = {
    "account": ACCOUNT,
    "coverage": {"percent": 0.0002, "read": 200, "total": 92376187},
    "quality": {"grade": "B", "score": 71},
    "classes": [{"class": "likelyReal", "count": 122, "percent": 61}],
    "signals": [{"count": 36, "id": "defaultPicture", "percent": 18, "points": 2}],
    "arrivalBands": [{"count": 13, "from": 1, "percent": 13, "read": 100, "to": 100}],
    "cohorts": [{"count": 7, "likelyFake": 6, "percent": 3.5, "weekStartMs": 1761523200000}],
    "languages": [{"count": 141, "percent": 70.5, "value": "en"}],
    "places": [{"count": 22, "percent": 11, "value": "United States"}],
    "verified": {"count": 9, "percent": 4.5},
    "followers": [FOLLOWER],
    "topFollowers": [FOLLOWER],
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_a_follower_audit_reads_the_newest_followers(asynchronous: bool) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_follower_audit("11348282", limit=50),
        lambda client: client.x.users.retrieve_follower_audit("11348282", limit=50),
        {"audit": AUDIT},
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/users/11348282/follower-audit"
    assert dict(request.url.params) == {"limit": "50"}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_a_follower_audit_reads_its_report_into_typed_fields(asynchronous: bool) -> None:
    _, report = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_follower_audit("11348282"),
        lambda client: client.x.users.retrieve_follower_audit("11348282"),
        {"audit": AUDIT},
        asynchronous,
    )

    audit = report.audit
    assert audit.quality.grade == "B"
    assert audit.classes[0].class_ == "likelyReal"
    assert audit.arrival_bands[0].from_ == 1
    assert audit.cohorts[0].week_start_ms == 1761523200000
    assert audit.top_followers[0].user_name == "orbit_watcher"
    assert audit.top_followers[0].joined_at_ms == 1561939200000
    assert audit.account.engagement_rate == 0.0047
