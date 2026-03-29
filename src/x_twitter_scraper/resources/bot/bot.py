# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import bot_track_usage_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .platform_links import (
    PlatformLinksResource,
    AsyncPlatformLinksResource,
    PlatformLinksResourceWithRawResponse,
    AsyncPlatformLinksResourceWithRawResponse,
    PlatformLinksResourceWithStreamingResponse,
    AsyncPlatformLinksResourceWithStreamingResponse,
)
from ...types.bot_track_usage_response import BotTrackUsageResponse

__all__ = ["BotResource", "AsyncBotResource"]


class BotResource(SyncAPIResource):
    """Telegram bot service endpoints"""

    @cached_property
    def platform_links(self) -> PlatformLinksResource:
        """Telegram bot service endpoints"""
        return PlatformLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> BotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return BotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return BotResourceWithStreamingResponse(self)

    def track_usage(
        self,
        *,
        input_tokens: int,
        output_tokens: int,
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTrackUsageResponse:
        """
        Track bot token usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bot/usage",
            body=maybe_transform(
                {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "platform_user_id": platform_user_id,
                },
                bot_track_usage_params.BotTrackUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotTrackUsageResponse,
        )


class AsyncBotResource(AsyncAPIResource):
    """Telegram bot service endpoints"""

    @cached_property
    def platform_links(self) -> AsyncPlatformLinksResource:
        """Telegram bot service endpoints"""
        return AsyncPlatformLinksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncBotResourceWithStreamingResponse(self)

    async def track_usage(
        self,
        *,
        input_tokens: int,
        output_tokens: int,
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BotTrackUsageResponse:
        """
        Track bot token usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bot/usage",
            body=await async_maybe_transform(
                {
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "platform_user_id": platform_user_id,
                },
                bot_track_usage_params.BotTrackUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BotTrackUsageResponse,
        )


class BotResourceWithRawResponse:
    def __init__(self, bot: BotResource) -> None:
        self._bot = bot

        self.track_usage = to_raw_response_wrapper(
            bot.track_usage,
        )

    @cached_property
    def platform_links(self) -> PlatformLinksResourceWithRawResponse:
        """Telegram bot service endpoints"""
        return PlatformLinksResourceWithRawResponse(self._bot.platform_links)


class AsyncBotResourceWithRawResponse:
    def __init__(self, bot: AsyncBotResource) -> None:
        self._bot = bot

        self.track_usage = async_to_raw_response_wrapper(
            bot.track_usage,
        )

    @cached_property
    def platform_links(self) -> AsyncPlatformLinksResourceWithRawResponse:
        """Telegram bot service endpoints"""
        return AsyncPlatformLinksResourceWithRawResponse(self._bot.platform_links)


class BotResourceWithStreamingResponse:
    def __init__(self, bot: BotResource) -> None:
        self._bot = bot

        self.track_usage = to_streamed_response_wrapper(
            bot.track_usage,
        )

    @cached_property
    def platform_links(self) -> PlatformLinksResourceWithStreamingResponse:
        """Telegram bot service endpoints"""
        return PlatformLinksResourceWithStreamingResponse(self._bot.platform_links)


class AsyncBotResourceWithStreamingResponse:
    def __init__(self, bot: AsyncBotResource) -> None:
        self._bot = bot

        self.track_usage = async_to_streamed_response_wrapper(
            bot.track_usage,
        )

    @cached_property
    def platform_links(self) -> AsyncPlatformLinksResourceWithStreamingResponse:
        """Telegram bot service endpoints"""
        return AsyncPlatformLinksResourceWithStreamingResponse(self._bot.platform_links)
