# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Dict

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper

LINK_ID = "xlink_AAAAAAAAAAAAAAAA"
ATTEMPT_ID = "xatt_0123456789abcdef0123456789abcdef"
RETURN_URL = "https://example.com/connected"
LINK: Dict[str, object] = {
    "object": "x_account_connection_link",
    "id": LINK_ID,
    "purpose": "connect",
    "status": "pending",
    "reference": "user-42",
    "returnUrl": RETURN_URL,
    "accountId": None,
    "xUserId": None,
    "xUsername": None,
    "health": None,
    "failure": None,
    "createdAt": "2025-01-15T12:00:00Z",
    "expiresAt": "2025-01-15T12:30:00Z",
    "completedAt": None,
}
PENDING: Dict[str, object] = {
    "object": "x_account_connection_attempt",
    "id": ATTEMPT_ID,
    "status": "pending",
    "pollAfterMs": 1000,
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_create_posts_the_options_and_reads_the_url(asynchronous: bool) -> None:
    request, link = await send_with_mock_transport(
        lambda client: client.x.account_connection_links.create(
            account_id="42", reference="user-42", return_url=RETURN_URL
        ),
        lambda client: client.x.account_connection_links.create(
            account_id="42", reference="user-42", return_url=RETURN_URL
        ),
        {**LINK, "url": "https://example.com/connect#token"},
        asynchronous,
        "POST",
    )

    assert request.method == "POST"
    assert request.url.path.endswith("/x/account-connection-links")
    assert json.loads(request.content) == {"accountId": "42", "reference": "user-42", "returnUrl": RETURN_URL}
    assert link.url == "https://example.com/connect#token"
    assert link.status == "pending"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_reads_the_link_by_its_id(asynchronous: bool) -> None:
    request, link = await send_with_mock_transport(
        lambda client: client.x.account_connection_links.retrieve(LINK_ID),
        lambda client: client.x.account_connection_links.retrieve(LINK_ID),
        LINK,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path.endswith(f"/x/account-connection-links/{LINK_ID}")
    assert link.reference == "user-42"
    assert link.url is None


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_delete_revokes_the_link_by_its_id(asynchronous: bool) -> None:
    request, result = await send_with_mock_transport(
        lambda client: client.x.account_connection_links.delete(LINK_ID),
        lambda client: client.x.account_connection_links.delete(LINK_ID),
        {"success": True},
        asynchronous,
        "DELETE",
    )

    assert request.method == "DELETE"
    assert request.url.path.endswith(f"/x/account-connection-links/{LINK_ID}")
    assert result.success is True


def test_the_links_refuse_an_empty_id() -> None:
    client = XTwitterScraper(api_key="isolated-test")
    with pytest.raises(ValueError, match="id"):
        client.x.account_connection_links.retrieve("")
    with pytest.raises(ValueError, match="id"):
        client.x.account_connection_links.delete("")


async def test_the_async_links_refuse_an_empty_id() -> None:
    client = AsyncXTwitterScraper(api_key="isolated-test")
    with pytest.raises(ValueError, match="id"):
        await client.x.account_connection_links.retrieve("")
    with pytest.raises(ValueError, match="id"):
        await client.x.account_connection_links.delete("")


def test_the_raw_and_streaming_wrappers_expose_the_links() -> None:
    client = XTwitterScraper(api_key="isolated-test")
    asynchronous = AsyncXTwitterScraper(api_key="isolated-test")
    for links in (
        client.x.account_connection_links.with_raw_response,
        client.x.account_connection_links.with_streaming_response,
        client.x.with_raw_response.account_connection_links,
        client.x.with_streaming_response.account_connection_links,
        asynchronous.x.account_connection_links.with_raw_response,
        asynchronous.x.account_connection_links.with_streaming_response,
        asynchronous.x.with_raw_response.account_connection_links,
        asynchronous.x.with_streaming_response.account_connection_links,
    ):
        assert callable(links.create)
        assert callable(links.retrieve)
        assert callable(links.delete)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_accounts_send_the_attempt_id_and_read_a_pending_answer(asynchronous: bool) -> None:
    request, created = await send_with_mock_transport(
        lambda client: client.x.accounts.create(
            email="account@example.invalid",
            password="<ACCOUNT_PASSWORD>",
            totp_secret="<TOTP_SECRET>",
            username="your_x_username",
            connection_attempt_id=ATTEMPT_ID,
        ),
        lambda client: client.x.accounts.create(
            email="account@example.invalid",
            password="<ACCOUNT_PASSWORD>",
            totp_secret="<TOTP_SECRET>",
            username="your_x_username",
            connection_attempt_id=ATTEMPT_ID,
        ),
        PENDING,
        asynchronous,
        "POST",
    )

    assert json.loads(request.content)["connection_attempt_id"] == ATTEMPT_ID
    assert created.status == "pending"

    request, reauth = await send_with_mock_transport(
        lambda client: client.x.accounts.reauth("42", password="<ACCOUNT_PASSWORD>", connection_attempt_id=ATTEMPT_ID),
        lambda client: client.x.accounts.reauth("42", password="<ACCOUNT_PASSWORD>", connection_attempt_id=ATTEMPT_ID),
        PENDING,
        asynchronous,
        "POST",
    )

    assert json.loads(request.content) == {"password": "<ACCOUNT_PASSWORD>", "connection_attempt_id": ATTEMPT_ID}
    assert reauth.status == "pending"
    assert reauth.id == ATTEMPT_ID


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_a_finished_attempt_names_the_connected_account(asynchronous: bool) -> None:
    _, attempt = await send_with_mock_transport(
        lambda client: client.x.account_connection_attempts.retrieve(ATTEMPT_ID),
        lambda client: client.x.account_connection_attempts.retrieve(ATTEMPT_ID),
        {"object": "x_account_connection_attempt", "id": ATTEMPT_ID, "status": "success", "accountId": "42"},
        asynchronous,
    )

    assert attempt.status == "success"
    assert attempt.account_id == "42"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_tweets_create_sends_media_ids(asynchronous: bool) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: client.x.tweets.create(
            account="@elonmusk", idempotency_key="write-1", media_ids=["2104371968258560001"]
        ),
        lambda client: client.x.tweets.create(
            account="@elonmusk", idempotency_key="write-1", media_ids=["2104371968258560001"]
        ),
        {},
        asynchronous,
        "POST",
        strict_response_validation=False,
    )

    assert json.loads(request.content) == {"account": "@elonmusk", "media_ids": ["2104371968258560001"]}
