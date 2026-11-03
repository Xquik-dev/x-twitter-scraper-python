# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import ShadowbanReport

ACTIVE = {
    "username": "NASA",
    "userId": "11348282",
    "account": "active",
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
    },
}

SUSPENDED = {
    "username": None,
    "userId": "11348282",
    "account": "suspended",
    "checks": {
        "account": {
            "verdict": "fail",
            "reason": "suspended",
            "evidence": {"profileUrl": "https://x.com/i/user/11348282"},
        },
        "search": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "suggestion": {"verdict": "unknown", "reason": "suspended", "evidence": None},
        "replies": {"verdict": "unknown", "reason": "suspended", "evidence": None},
    },
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_shadowban_reads_each_check_and_its_evidence(asynchronous: bool) -> None:
    request, report = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_shadowban("NASA", omit="checks.account"),
        lambda client: client.x.users.retrieve_shadowban("NASA", omit="checks.account"),
        ACTIVE,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/x/users/NASA/shadowban"
    assert dict(request.url.params) == {"omit": "checks.account"}
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


def test_an_empty_id_raises_before_any_request(client: XTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        client.x.users.retrieve_shadowban("")


async def test_an_async_empty_id_raises_before_any_request(async_client: AsyncXTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        await async_client.x.users.retrieve_shadowban("")
