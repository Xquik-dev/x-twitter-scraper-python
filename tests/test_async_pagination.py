# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Iterable
from contextlib import nullcontext
from typing_extensions import override

import httpx
import pytest

from x_twitter_scraper import InternalServerError, AsyncXTwitterScraper
from x_twitter_scraper._models import FinalRequestOptions
from x_twitter_scraper._base_client import PageInfo, BaseAsyncPage, AsyncPaginator


class NumberPage(BaseAsyncPage[int]):
    items: list[int]
    cursor: str | None = None

    @override
    def _get_page_items(self) -> Iterable[int]:
        return self.items

    @override
    def next_page_info(self) -> PageInfo | None:
        return PageInfo(params={"cursor": self.cursor}) if self.cursor else None


@pytest.mark.parametrize("fail", [False, True])
async def test_async_paginator_retains_items_and_propagates_page_failure(fail: bool) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(200, json={"items": [1, 2], "cursor": "next-page"})
        return httpx.Response(503, json={"error": "unavailable"}) if fail else httpx.Response(200, json={"items": [3]})

    collected: list[int] = []
    async with AsyncXTwitterScraper(
        api_key="isolated-test",
        max_retries=0,
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond)),
    ) as client:
        paginator = AsyncPaginator(
            client=client,
            options=FinalRequestOptions.construct(method="get", url="/pages"),
            page_cls=NumberPage,
            model=int,
        )
        with pytest.raises(InternalServerError) if fail else nullcontext():
            async for item in paginator:
                collected.append(item)
    assert collected == ([1, 2] if fail else [1, 2, 3])
    assert len(requests) == 2
    assert requests[0].url.params.get("cursor") is None
    assert requests[1].url.params["cursor"] == "next-page"
