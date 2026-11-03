# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from typing import Any

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import ShadowbanReport

ACTIVE: dict[str, Any] = {
    "username": "NASA",
    "userId": "11348282",
    "account": "active",
    "checkedAt": "2026-11-03T02:15:00.000Z",
    "overall": "clear",
    "checks": {
        "account": {"verdict": "pass", "reason": "active", "evidence": {"profileUrl": "https://x.com/NASA"}},
        "search": {
            "verdict": "pass",
            "reason": "listed",
            "evidence": {
                "query": "from:NASA",
                "searchUrl": "https://x.com/search?q=from%3ANASA&f=live",
                "recentPostIds": ["2103610284464316469", "2103583087540003274"],
                "foundPostIds": ["2103610284464316469", "2103583087540003274"],
            },
        },
        "suggestion": {
            "verdict": "pass",
            "reason": "suggested",
            "evidence": {"query": "NASA", "suggestedUsernames": ["NASA", "NASAHubble", "NASAEarth"]},
        },
        "replies": {
            "verdict": "unknown",
            "reason": "more_replies",
            "evidence": {
                "replies": [
                    {
                        "replyId": "2103589735449141451",
                        "replyUrl": "https://x.com/i/status/2103589735449141451",
                        "parentId": "2102883223948628205",
                        "parentUrl": "https://x.com/i/status/2102883223948628205",
                        "placement": "more_replies",
                    },
                    {
                        "replyId": "2103215186870239252",
                        "replyUrl": "https://x.com/i/status/2103215186870239252",
                        "parentId": "2102924351171670302",
                        "parentUrl": "https://x.com/i/status/2102924351171670302",
                        "placement": "thread",
                    },
                ]
            },
        },
        "replyLock": {
            "verdict": "pass",
            "reason": "replies_show",
            "evidence": {"checkedReplies": 2, "shownReplies": 2},
        },
        "timeline": {"verdict": "pass", "reason": "visible", "evidence": {"postCount": 74486, "timelinePosts": 20}},
        "engagement": {
            "verdict": "pass",
            "reason": "typical",
            "evidence": {"newestMedian": 4268, "newestPosts": 5, "earlierMedian": 2773.5, "earlierPosts": 7},
        },
        "sensitive": {"verdict": "pass", "reason": "not_flagged", "evidence": None},
        "withheld": {"verdict": "pass", "reason": "none", "evidence": {"countries": []}},
    },
}

SUSPENDED = {
    "username": None,
    "userId": "11348282",
    "account": "suspended",
    "checkedAt": "2026-11-03T02:16:00.000Z",
    "overall": "suspended",
    "checks": {
        "account": {
            "verdict": "fail",
            "reason": "suspended",
            "evidence": {"profileUrl": "https://x.com/i/user/11348282"},
        },
        "search": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "suggestion": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "replies": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "replyLock": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "timeline": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "engagement": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "sensitive": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "withheld": {"verdict": "unknown", "reason": "suspended", "evidence": None},
    },
}

LIMITED: dict[str, object] = {
    **ACTIVE,
    "overall": "limited",
    "checks": {
        **ACTIVE["checks"],
        "replyLock": {
            "verdict": "unknown",
            "reason": "replies_missing",
            "evidence": {"checkedReplies": 3, "shownReplies": 0},
        },
        "timeline": {"verdict": "fail", "reason": "hidden", "evidence": {"postCount": None, "timelinePosts": 0}},
        "engagement": {
            "verdict": "unknown",
            "reason": "low",
            "evidence": {"newestMedian": 0, "newestPosts": 5, "earlierMedian": 12, "earlierPosts": 20},
        },
        "sensitive": {"verdict": "fail", "reason": "flagged", "evidence": None},
        "withheld": {"verdict": "fail", "reason": "countries", "evidence": {"countries": ["DE", "TR"]}},
    },
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_shadowban_reads_each_check_and_its_evidence(asynchronous: bool) -> None:
    request, report = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_shadowban("NASA", fields="username,userId,account,checks"),
        lambda client: client.x.users.retrieve_shadowban("NASA", fields="username,userId,account,checks"),
        ACTIVE,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/x/users/NASA/shadowban"
    assert dict(request.url.params) == {"fields": "username,userId,account,checks"}
    assert isinstance(report, ShadowbanReport)
    assert (report.username, report.user_id, report.account) == ("NASA", "11348282", "active")
    checks = report.checks
    assert checks.account.evidence.profile_url == "https://x.com/NASA"
    assert (checks.search.verdict, checks.search.reason) == ("pass", "listed")
    assert checks.search.evidence is not None
    assert checks.search.evidence.found_post_ids == ["2103610284464316469", "2103583087540003274"]
    assert checks.suggestion.evidence is not None
    assert checks.suggestion.evidence.suggested_usernames == ["NASA", "NASAHubble", "NASAEarth"]
    assert (checks.replies.verdict, checks.replies.reason) == ("unknown", "more_replies")
    assert checks.replies.evidence is not None
    assert [reply.placement for reply in checks.replies.evidence.replies] == ["more_replies", "thread"]
    assert checks.replies.evidence.replies[0].parent_id == "2102883223948628205"
    assert report.checked_at == datetime.datetime(2026, 11, 3, 2, 15, tzinfo=datetime.timezone.utc)
    assert report.overall == "clear"
    assert (checks.reply_lock.verdict, checks.reply_lock.reason) == ("pass", "replies_show")
    assert checks.reply_lock.evidence is not None
    assert (checks.reply_lock.evidence.checked_replies, checks.reply_lock.evidence.shown_replies) == (2, 2)
    assert (checks.timeline.verdict, checks.timeline.reason) == ("pass", "visible")
    assert checks.timeline.evidence is not None
    assert (checks.timeline.evidence.post_count, checks.timeline.evidence.timeline_posts) == (74486, 20)
    assert (checks.engagement.verdict, checks.engagement.reason) == ("pass", "typical")
    assert checks.engagement.evidence is not None
    assert (checks.engagement.evidence.newest_median, checks.engagement.evidence.newest_posts) == (4268, 5)
    assert (checks.engagement.evidence.earlier_median, checks.engagement.evidence.earlier_posts) == (2773.5, 7)
    assert (checks.sensitive.verdict, checks.sensitive.reason, checks.sensitive.evidence) == (
        "pass",
        "not_flagged",
        None,
    )
    assert (checks.withheld.verdict, checks.withheld.reason) == ("pass", "none")
    assert checks.withheld.evidence is not None
    assert checks.withheld.evidence.countries == []


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_shadowban_reads_the_failing_checks_of_a_limited_account(asynchronous: bool) -> None:
    _, report = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_shadowban("NASA"),
        lambda client: client.x.users.retrieve_shadowban("NASA"),
        LIMITED,
        asynchronous,
    )

    checks = report.checks
    assert report.overall == "limited"
    assert (checks.reply_lock.verdict, checks.reply_lock.reason) == ("unknown", "replies_missing")
    assert checks.reply_lock.evidence is not None
    assert checks.reply_lock.evidence.shown_replies == 0
    assert (checks.timeline.verdict, checks.timeline.reason) == ("fail", "hidden")
    assert checks.timeline.evidence is not None
    assert (checks.timeline.evidence.post_count, checks.timeline.evidence.timeline_posts) == (None, 0)
    assert (checks.engagement.verdict, checks.engagement.reason) == ("unknown", "low")
    assert (checks.sensitive.verdict, checks.sensitive.reason) == ("fail", "flagged")
    assert (checks.withheld.verdict, checks.withheld.reason) == ("fail", "countries")
    assert checks.withheld.evidence is not None
    assert checks.withheld.evidence.countries == ["DE", "TR"]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_shadowban_reads_a_suspended_account_without_evidence(asynchronous: bool) -> None:
    request, report = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_shadowban("11348282"),
        lambda client: client.x.users.retrieve_shadowban("11348282"),
        SUSPENDED,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/users/11348282/shadowban"
    assert dict(request.url.params) == {}
    assert (report.username, report.account) == (None, "suspended")
    assert (report.checks.account.verdict, report.checks.account.reason) == ("fail", "suspended")
    assert report.checks.search.evidence is None
    assert report.checks.suggestion.evidence is None
    assert report.checks.replies.evidence is None
    assert report.overall == "suspended"
    assert [
        (check.verdict, check.reason, check.evidence)
        for check in (
            report.checks.reply_lock,
            report.checks.timeline,
            report.checks.engagement,
            report.checks.sensitive,
            report.checks.withheld,
        )
    ] == [("unknown", "suspended", None)] * 5


def test_an_empty_id_raises_before_any_request(client: XTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        client.x.users.retrieve_shadowban("")


async def test_an_async_empty_id_raises_before_any_request(async_client: AsyncXTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        await async_client.x.users.retrieve_shadowban("")
