# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.x.tweets import retweet_create_params, retweet_delete_params
from ....types.x.tweets.retweet_create_response import RetweetCreateResponse
from ....types.x.tweets.retweet_delete_response import RetweetDeleteResponse

__all__ = ["RetweetResource", "AsyncRetweetResource"]


class RetweetResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> RetweetResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return RetweetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetweetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return RetweetResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetweetCreateResponse:
        """
        Reposts a tweet through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return self._post(
            path_template("/x/tweets/{id}/retweet", id=id),
            body=maybe_transform({"account": account}, retweet_create_params.RetweetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetCreateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetweetDeleteResponse:
        """
        Removes a repost through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return self._delete(
            path_template("/x/tweets/{id}/retweet", id=id),
            body=maybe_transform({"account": account}, retweet_delete_params.RetweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetDeleteResponse,
        )


class AsyncRetweetResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncRetweetResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncRetweetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetweetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncRetweetResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetweetCreateResponse:
        """
        Reposts a tweet through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return await self._post(
            path_template("/x/tweets/{id}/retweet", id=id),
            body=await async_maybe_transform({"account": account}, retweet_create_params.RetweetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetCreateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetweetDeleteResponse:
        """
        Removes a repost through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return await self._delete(
            path_template("/x/tweets/{id}/retweet", id=id),
            body=await async_maybe_transform({"account": account}, retweet_delete_params.RetweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetweetDeleteResponse,
        )


class RetweetResourceWithRawResponse:
    def __init__(self, retweet: RetweetResource) -> None:
        self._retweet = retweet

        self.create = to_raw_response_wrapper(
            retweet.create,
        )
        self.delete = to_raw_response_wrapper(
            retweet.delete,
        )


class AsyncRetweetResourceWithRawResponse:
    def __init__(self, retweet: AsyncRetweetResource) -> None:
        self._retweet = retweet

        self.create = async_to_raw_response_wrapper(
            retweet.create,
        )
        self.delete = async_to_raw_response_wrapper(
            retweet.delete,
        )


class RetweetResourceWithStreamingResponse:
    def __init__(self, retweet: RetweetResource) -> None:
        self._retweet = retweet

        self.create = to_streamed_response_wrapper(
            retweet.create,
        )
        self.delete = to_streamed_response_wrapper(
            retweet.delete,
        )


class AsyncRetweetResourceWithStreamingResponse:
    def __init__(self, retweet: AsyncRetweetResource) -> None:
        self._retweet = retweet

        self.create = async_to_streamed_response_wrapper(
            retweet.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            retweet.delete,
        )
