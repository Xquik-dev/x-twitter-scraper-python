# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import subscribe_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.subscribe_create_response import SubscribeCreateResponse

__all__ = ["SubscribeResource", "AsyncSubscribeResource"]


class SubscribeResource(SyncAPIResource):
    """Subscription, billing, and credits"""

    @cached_property
    def with_raw_response(self) -> SubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return SubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return SubscribeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        tier: Literal["starter", "pro", "business"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscribeCreateResponse:
        """
        Create a subscription checkout or billing-management URL only after the user
        confirms. The request never completes payment by itself.

        Args:
          tier: Subscription tier to pre-select.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/subscribe",
            body=maybe_transform({"tier": tier}, subscribe_create_params.SubscribeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeCreateResponse,
        )


class AsyncSubscribeResource(AsyncAPIResource):
    """Subscription, billing, and credits"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncSubscribeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        tier: Literal["starter", "pro", "business"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscribeCreateResponse:
        """
        Create a subscription checkout or billing-management URL only after the user
        confirms. The request never completes payment by itself.

        Args:
          tier: Subscription tier to pre-select.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/subscribe",
            body=await async_maybe_transform({"tier": tier}, subscribe_create_params.SubscribeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeCreateResponse,
        )


class SubscribeResourceWithRawResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = to_raw_response_wrapper(
            subscribe.create,
        )


class AsyncSubscribeResourceWithRawResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = async_to_raw_response_wrapper(
            subscribe.create,
        )


class SubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = to_streamed_response_wrapper(
            subscribe.create,
        )


class AsyncSubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = async_to_streamed_response_wrapper(
            subscribe.create,
        )
