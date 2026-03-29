# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.bot import platform_link_create_params, platform_link_delete_params, platform_link_lookup_params
from ..._base_client import make_request_options
from ...types.bot.platform_link_create_response import PlatformLinkCreateResponse
from ...types.bot.platform_link_delete_response import PlatformLinkDeleteResponse
from ...types.bot.platform_link_lookup_response import PlatformLinkLookupResponse

__all__ = ["PlatformLinksResource", "AsyncPlatformLinksResource"]


class PlatformLinksResource(SyncAPIResource):
    """Telegram bot service endpoints"""

    @cached_property
    def with_raw_response(self) -> PlatformLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return PlatformLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlatformLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return PlatformLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: Literal["telegram"],
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkCreateResponse:
        """
        Link a platform user to an Xquik account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/bot/platform-links",
            body=maybe_transform(
                {
                    "platform": platform,
                    "platform_user_id": platform_user_id,
                },
                platform_link_create_params.PlatformLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformLinkCreateResponse,
        )

    def delete(
        self,
        *,
        platform: Literal["telegram"],
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkDeleteResponse:
        """
        Unlink a platform user from an Xquik account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/bot/platform-links",
            body=maybe_transform(
                {
                    "platform": platform,
                    "platform_user_id": platform_user_id,
                },
                platform_link_delete_params.PlatformLinkDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformLinkDeleteResponse,
        )

    def lookup(
        self,
        *,
        platform: str,
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkLookupResponse:
        """
        Look up an Xquik user by platform identity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/bot/platform-links/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "platform": platform,
                        "platform_user_id": platform_user_id,
                    },
                    platform_link_lookup_params.PlatformLinkLookupParams,
                ),
            ),
            cast_to=PlatformLinkLookupResponse,
        )


class AsyncPlatformLinksResource(AsyncAPIResource):
    """Telegram bot service endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncPlatformLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlatformLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlatformLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncPlatformLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        platform: Literal["telegram"],
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkCreateResponse:
        """
        Link a platform user to an Xquik account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/bot/platform-links",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "platform_user_id": platform_user_id,
                },
                platform_link_create_params.PlatformLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformLinkCreateResponse,
        )

    async def delete(
        self,
        *,
        platform: Literal["telegram"],
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkDeleteResponse:
        """
        Unlink a platform user from an Xquik account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/bot/platform-links",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "platform_user_id": platform_user_id,
                },
                platform_link_delete_params.PlatformLinkDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlatformLinkDeleteResponse,
        )

    async def lookup(
        self,
        *,
        platform: str,
        platform_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlatformLinkLookupResponse:
        """
        Look up an Xquik user by platform identity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/bot/platform-links/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "platform": platform,
                        "platform_user_id": platform_user_id,
                    },
                    platform_link_lookup_params.PlatformLinkLookupParams,
                ),
            ),
            cast_to=PlatformLinkLookupResponse,
        )


class PlatformLinksResourceWithRawResponse:
    def __init__(self, platform_links: PlatformLinksResource) -> None:
        self._platform_links = platform_links

        self.create = to_raw_response_wrapper(
            platform_links.create,
        )
        self.delete = to_raw_response_wrapper(
            platform_links.delete,
        )
        self.lookup = to_raw_response_wrapper(
            platform_links.lookup,
        )


class AsyncPlatformLinksResourceWithRawResponse:
    def __init__(self, platform_links: AsyncPlatformLinksResource) -> None:
        self._platform_links = platform_links

        self.create = async_to_raw_response_wrapper(
            platform_links.create,
        )
        self.delete = async_to_raw_response_wrapper(
            platform_links.delete,
        )
        self.lookup = async_to_raw_response_wrapper(
            platform_links.lookup,
        )


class PlatformLinksResourceWithStreamingResponse:
    def __init__(self, platform_links: PlatformLinksResource) -> None:
        self._platform_links = platform_links

        self.create = to_streamed_response_wrapper(
            platform_links.create,
        )
        self.delete = to_streamed_response_wrapper(
            platform_links.delete,
        )
        self.lookup = to_streamed_response_wrapper(
            platform_links.lookup,
        )


class AsyncPlatformLinksResourceWithStreamingResponse:
    def __init__(self, platform_links: AsyncPlatformLinksResource) -> None:
        self._platform_links = platform_links

        self.create = async_to_streamed_response_wrapper(
            platform_links.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            platform_links.delete,
        )
        self.lookup = async_to_streamed_response_wrapper(
            platform_links.lookup,
        )
