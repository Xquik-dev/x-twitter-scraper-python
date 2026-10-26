# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    AnalysisNewsResponse,
    AnalysisBrandResponse,
    AnalysisClassifyResponse,
    AnalysisSentimentResponse,
    AnalysisViralScoreResponse,
    AnalysisMarketSignalsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_brand(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.brand()
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_brand_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.brand(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_brand(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.brand()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_brand(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.brand() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_classify(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.classify()
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_classify_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.classify(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_classify(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.classify()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_classify(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.classify() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_market_signals(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.market_signals()
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_market_signals_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.market_signals(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_market_signals(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.market_signals()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_market_signals(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.market_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_news(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.news()
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_news_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.news(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_news(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.news()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_news(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.news() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.sentiment()
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sentiment_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.sentiment(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sentiment(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.sentiment()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sentiment(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.sentiment() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_viral_score(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.viral_score()
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_viral_score_with_all_params(self, client: XTwitterScraper) -> None:
        analysis = client.x.analysis.viral_score(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_viral_score(self, client: XTwitterScraper) -> None:
        response = client.x.analysis.with_raw_response.viral_score()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = response.parse()
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_viral_score(self, client: XTwitterScraper) -> None:
        with client.x.analysis.with_streaming_response.viral_score() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = response.parse()
            assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

        assert response.is_closed is True


class TestAsyncAnalysis:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_brand(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.brand()
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_brand_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.brand(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_brand(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.brand()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_brand(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.brand() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisBrandResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_classify(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.classify()
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.classify(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.classify()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.classify() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisClassifyResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_market_signals(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.market_signals()
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_market_signals_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.market_signals(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_market_signals(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.market_signals()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_market_signals(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.market_signals() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisMarketSignalsResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_news(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.news()
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_news_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.news(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_news(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.news()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_news(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.news() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisNewsResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.sentiment()
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sentiment_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.sentiment(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sentiment(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.sentiment()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sentiment(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.sentiment() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisSentimentResponse, analysis, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_viral_score(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.viral_score()
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_viral_score_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        analysis = await async_client.x.analysis.viral_score(
            analysis={
                "concurrency": 1,
                "context": "context",
                "max_context_bytes": 219,
                "preset": "brand",
                "questions": [
                    {
                        "id": "request",
                        "instructions": "What does the author ask for?",
                        "type": "choice",
                        "version": "1",
                        "categories": {},
                        "criteria": {"no": "Asks for no refund.", "yes": "Asks for a refund."},
                        "levels": ["string", "string"],
                    }
                ],
                "targets": [{"name": "Sony", "aliases": ["WH-1000XM6"]}],
            },
            baseline=[
                {
                    "answers": {},
                    "id": "1893456789012345678",
                    "monitor": {"configuration_fingerprint": "configurationFingerprint"},
                    "tweet": {"id": "x"},
                }
            ],
            cursor="DAACCgACGRElMJcAAA",
            limit=20,
            list_id="1234567890",
            query="Sony WH-1000XM6 lang:en",
            query_type="Latest",
            quotes_of="1893456789012345678",
            replies_to="1893456789012345678",
            since_time="2026-09-25T00:00:00Z",
            texts=["We shipped dark mode today. Tell us what breaks."],
            tweet_ids=["1893456789012345678"],
            until_time="2026-09-26T00:00:00Z",
            username="@NASA",
        )
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_viral_score(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.analysis.with_raw_response.viral_score()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        analysis = await response.parse()
        assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_viral_score(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.analysis.with_streaming_response.viral_score() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            analysis = await response.parse()
            assert_matches_type(AnalysisViralScoreResponse, analysis, path=["response"])

        assert response.is_closed is True
