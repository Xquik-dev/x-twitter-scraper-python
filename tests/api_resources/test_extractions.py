# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    ExtractionRunResponse,
    ExtractionListResponse,
    ExtractionCancelResponse,
    ExtractionRetrieveResponse,
    ExtractionEstimateCostResponse,
)
from x_twitter_scraper._utils import parse_date, parse_datetime
from x_twitter_scraper._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)


class TestExtractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.retrieve(
            id="id",
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.retrieve(
            id="id",
            cursor="cursor",
            field_style="source",
            include_raw=True,
            limit=1,
            output_mode="compact",
            output_preset="nested",
            wait=0,
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.extractions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.list()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.list(
            cursor="cursor",
            limit=1,
            status="pending",
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionListResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.cancel(
            "id",
        )
        assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.extractions.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_cost(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.estimate_cost(
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_cost_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.estimate_cost(
            tool_type="follower_explorer",
            advanced_query="advancedQuery",
            any_words="anyWords",
            bio_contains="bioContains",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            collection_strategy="auto",
            conversation_id="conversationId",
            dedupe_across_targets=True,
            dedupe_mode="none",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_location=True,
            has_media_only=True,
            has_website=True,
            include_original_post=True,
            include_search_terms=True,
            include_target_metadata=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            list_id="listId",
            location_contains="locationContains",
            max_depth=1,
            max_followers=0,
            max_following=0,
            max_id="maxId",
            max_items_per_target=1,
            max_likes=0,
            max_pages_per_target=1,
            max_posts=0,
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_account_age_days=0,
            min_bookmarks=0,
            min_faves=0,
            min_followers=0,
            min_following=0,
            min_posts=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            native_retweets=True,
            near="near",
            news=True,
            overlap_mode=True,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            relation_targets=[
                {
                    "relation": "community_members",
                    "value": "x",
                }
            ],
            replies="include",
            results_limit=1,
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            search_queries=["string"],
            search_query="searchQuery",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="relevance",
            source="source",
            start_cursor="x",
            target_community_id="targetCommunityId",
            target_community_ids=["string"],
            target_list_id="targetListId",
            target_list_ids=["string"],
            targets=["string"],
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_tweet_ids=["string"],
            target_username="elonmusk",
            target_usernames=["string"],
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
            within="within",
            within_time="withinTime",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_estimate_cost(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.estimate_cost(
            tool_type="follower_explorer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_estimate_cost(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.estimate_cost(
            tool_type="follower_explorer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export_results(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.export_results(
            id="id",
            format="csv",
        )
        assert extraction.http_request.url.path == "/extractions/id/export"
        assert extraction.is_closed
        assert extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    def test_method_export_results_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.export_results(
            id="id",
            format="csv",
            has_description=True,
            has_location=True,
            has_media=True,
            lang="lang",
            max_followers=0,
            max_following=0,
            max_posts=0,
            min_followers=0,
            min_following=0,
            min_likes=0,
            min_posts=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            search="search",
            since_date=parse_date("2019-12-27"),
            until_date=parse_date("2019-12-27"),
            verified=True,
        )
        assert extraction.http_request.url.path == "/extractions/id/export"
        assert extraction.is_closed
        assert extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    def test_raw_response_export_results(self, client: XTwitterScraper) -> None:

        extraction = client.extractions.with_raw_response.export_results(
            id="id",
            format="csv",
        )
        assert extraction.http_request.url.path == "/extractions/id/export"

        assert extraction.is_closed is True
        assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert extraction.json() == {"foo": "bar"}
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    def test_streaming_response_export_results(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.export_results(
            id="id",
            format="csv",
        ) as extraction:
            assert extraction.http_request.url.path == "/extractions/id/export"
            assert not extraction.is_closed
            assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert extraction.json() == {"foo": "bar"}
            assert cast(Any, extraction.is_closed) is True
            assert isinstance(extraction, StreamedBinaryAPIResponse)

        assert cast(Any, extraction.is_closed) is True

    @parametrize
    def test_path_params_export_results(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.extractions.with_raw_response.export_results(
                id="",
                format="csv",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.run(
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.run(
            tool_type="follower_explorer",
            dry_run=True,
            advanced_query="advancedQuery",
            any_words="anyWords",
            bio_contains="bioContains",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            collection_strategy="auto",
            conversation_id="conversationId",
            dedupe_across_targets=True,
            dedupe_mode="none",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_location=True,
            has_media_only=True,
            has_website=True,
            include_original_post=True,
            include_search_terms=True,
            include_target_metadata=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            list_id="listId",
            location_contains="locationContains",
            max_depth=1,
            max_followers=0,
            max_following=0,
            max_id="maxId",
            max_items_per_target=1,
            max_likes=0,
            max_pages_per_target=1,
            max_posts=0,
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_account_age_days=0,
            min_bookmarks=0,
            min_faves=0,
            min_followers=0,
            min_following=0,
            min_posts=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            native_retweets=True,
            near="near",
            news=True,
            overlap_mode=True,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            relation_targets=[
                {
                    "relation": "community_members",
                    "value": "x",
                }
            ],
            replies="include",
            results_limit=1,
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            search_queries=["string"],
            search_query="searchQuery",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="relevance",
            source="source",
            start_cursor="x",
            target_community_id="targetCommunityId",
            target_community_ids=["string"],
            target_list_id="targetListId",
            target_list_ids=["string"],
            targets=["string"],
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_tweet_ids=["string"],
            target_username="elonmusk",
            target_usernames=["string"],
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
            within="within",
            within_time="withinTime",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.run(
            tool_type="follower_explorer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.run(
            tool_type="follower_explorer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.retrieve(
            id="id",
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.retrieve(
            id="id",
            cursor="cursor",
            field_style="source",
            include_raw=True,
            limit=1,
            output_mode="compact",
            output_preset="nested",
            wait=0,
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.extractions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.list()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.list(
            cursor="cursor",
            limit=1,
            status="pending",
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionListResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.cancel(
            "id",
        )
        assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionCancelResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.extractions.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.estimate_cost(
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_cost_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.estimate_cost(
            tool_type="follower_explorer",
            advanced_query="advancedQuery",
            any_words="anyWords",
            bio_contains="bioContains",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            collection_strategy="auto",
            conversation_id="conversationId",
            dedupe_across_targets=True,
            dedupe_mode="none",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_location=True,
            has_media_only=True,
            has_website=True,
            include_original_post=True,
            include_search_terms=True,
            include_target_metadata=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            list_id="listId",
            location_contains="locationContains",
            max_depth=1,
            max_followers=0,
            max_following=0,
            max_id="maxId",
            max_items_per_target=1,
            max_likes=0,
            max_pages_per_target=1,
            max_posts=0,
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_account_age_days=0,
            min_bookmarks=0,
            min_faves=0,
            min_followers=0,
            min_following=0,
            min_posts=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            native_retweets=True,
            near="near",
            news=True,
            overlap_mode=True,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            relation_targets=[
                {
                    "relation": "community_members",
                    "value": "x",
                }
            ],
            replies="include",
            results_limit=1,
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            search_queries=["string"],
            search_query="searchQuery",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="relevance",
            source="source",
            start_cursor="x",
            target_community_id="targetCommunityId",
            target_community_ids=["string"],
            target_list_id="targetListId",
            target_list_ids=["string"],
            targets=["string"],
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_tweet_ids=["string"],
            target_username="elonmusk",
            target_usernames=["string"],
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
            within="within",
            within_time="withinTime",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.estimate_cost(
            tool_type="follower_explorer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.estimate_cost(
            tool_type="follower_explorer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export_results(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.export_results(
            id="id",
            format="csv",
        )
        assert extraction.http_request.url.path == "/extractions/id/export"
        assert extraction.is_closed
        assert await extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    async def test_method_export_results_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.export_results(
            id="id",
            format="csv",
            has_description=True,
            has_location=True,
            has_media=True,
            lang="lang",
            max_followers=0,
            max_following=0,
            max_posts=0,
            min_followers=0,
            min_following=0,
            min_likes=0,
            min_posts=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            search="search",
            since_date=parse_date("2019-12-27"),
            until_date=parse_date("2019-12-27"),
            verified=True,
        )
        assert extraction.http_request.url.path == "/extractions/id/export"
        assert extraction.is_closed
        assert await extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    async def test_raw_response_export_results(self, async_client: AsyncXTwitterScraper) -> None:

        extraction = await async_client.extractions.with_raw_response.export_results(
            id="id",
            format="csv",
        )
        assert extraction.http_request.url.path == "/extractions/id/export"

        assert extraction.is_closed is True
        assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await extraction.json() == {"foo": "bar"}
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    async def test_streaming_response_export_results(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.export_results(
            id="id",
            format="csv",
        ) as extraction:
            assert extraction.http_request.url.path == "/extractions/id/export"
            assert not extraction.is_closed
            assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await extraction.json() == {"foo": "bar"}
            assert cast(Any, extraction.is_closed) is True
            assert isinstance(extraction, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, extraction.is_closed) is True

    @parametrize
    async def test_path_params_export_results(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.extractions.with_raw_response.export_results(
                id="",
                format="csv",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.run(
            tool_type="follower_explorer",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.run(
            tool_type="follower_explorer",
            dry_run=True,
            advanced_query="advancedQuery",
            any_words="anyWords",
            bio_contains="bioContains",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            collection_strategy="auto",
            conversation_id="conversationId",
            dedupe_across_targets=True,
            dedupe_mode="none",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_location=True,
            has_media_only=True,
            has_website=True,
            include_original_post=True,
            include_search_terms=True,
            include_target_metadata=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            list_id="listId",
            location_contains="locationContains",
            max_depth=1,
            max_followers=0,
            max_following=0,
            max_id="maxId",
            max_items_per_target=1,
            max_likes=0,
            max_pages_per_target=1,
            max_posts=0,
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_account_age_days=0,
            min_bookmarks=0,
            min_faves=0,
            min_followers=0,
            min_following=0,
            min_posts=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            native_retweets=True,
            near="near",
            news=True,
            overlap_mode=True,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            relation_targets=[
                {
                    "relation": "community_members",
                    "value": "x",
                }
            ],
            replies="include",
            results_limit=1,
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            search_queries=["string"],
            search_query="searchQuery",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort="relevance",
            source="source",
            start_cursor="x",
            target_community_id="targetCommunityId",
            target_community_ids=["string"],
            target_list_id="targetListId",
            target_list_ids=["string"],
            targets=["string"],
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_tweet_ids=["string"],
            target_username="elonmusk",
            target_usernames=["string"],
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
            within="within",
            within_time="withinTime",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.run(
            tool_type="follower_explorer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.run(
            tool_type="follower_explorer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True
