# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest

from tests.utils import send_with_mock_transport

CHECKOUT = "https://xquik.com/api/v1/credits/topup/redirect?session=cs_test"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_topup_sends_the_currency_and_return_page(asynchronous: bool) -> None:
    request, checkout = await send_with_mock_transport(
        lambda client: client.credits.topup_balance(dollars=25, currency="EUR", return_path="/en/x-article-reader"),
        lambda client: client.credits.topup_balance(dollars=25, currency="EUR", return_path="/en/x-article-reader"),
        {"url": CHECKOUT, "redirect_url": CHECKOUT, "chargedCurrency": "EUR", "chargedMinorUnits": 2231},
        asynchronous,
        method="POST",
    )

    assert request.url.path == "/api/v1/credits/topup"
    assert json.loads(request.content) == {"dollars": 25, "currency": "EUR", "returnPath": "/en/x-article-reader"}
    assert (checkout.charged_currency, checkout.charged_minor_units) == ("EUR", 2231)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_topup_status_says_what_the_checkout_charged(asynchronous: bool) -> None:
    _, status = await send_with_mock_transport(
        lambda client: client.credits.retrieve_topup_status(session_id="cs_test"),
        lambda client: client.credits.retrieve_topup_status(session_id="cs_test"),
        {"status": "paid", "amount_dollars": 10, "chargedCurrency": "JPY", "chargedMinorUnits": 1580},
        asynchronous,
    )

    assert (status.charged_currency, status.charged_minor_units) == ("JPY", 1580)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_subscribe_sends_the_currency_and_reads_the_one_charged(asynchronous: bool) -> None:
    request, checkout = await send_with_mock_transport(
        lambda client: client.subscribe.create(currency="GBP", tier="pro"),
        lambda client: client.subscribe.create(currency="GBP", tier="pro"),
        {"url": CHECKOUT, "status": "checkout_created", "message": "Checkout created.", "chargedCurrency": "GBP"},
        asynchronous,
        method="POST",
    )

    assert request.url.path == "/api/v1/subscribe"
    assert json.loads(request.content) == {"currency": "GBP", "tier": "pro"}
    assert checkout.charged_currency == "GBP"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_subscribe_without_a_checkout_has_no_currency(asynchronous: bool) -> None:
    _, answer = await send_with_mock_transport(
        lambda client: client.subscribe.create(),
        lambda client: client.subscribe.create(),
        {"url": CHECKOUT, "status": "already_subscribed", "message": "Already subscribed."},
        asynchronous,
        method="POST",
    )

    assert answer.charged_currency is None
