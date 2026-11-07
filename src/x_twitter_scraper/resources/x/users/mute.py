# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.x.users import mute_create_params, mute_delete_params
from ....types.x.users.mute_create_response import MuteCreateResponse
from ....types.x.users.mute_delete_response import MuteDeleteResponse

__all__ = ["MuteResource", "AsyncMuteResource"]


class MuteResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> MuteResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return MuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return MuteResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MuteCreateResponse:
        """
        Mutes a user through a connected X account. The user's posts leave that
        account's timelines, and X doesn't tell the user.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._post(
            path_template("/x/users/{id}/mute", id=id),
            body=maybe_transform({"account": account}, mute_create_params.MuteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MuteCreateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MuteDeleteResponse:
        """
        Unmutes a user through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._delete(
            path_template("/x/users/{id}/mute", id=id),
            body=maybe_transform({"account": account}, mute_delete_params.MuteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MuteDeleteResponse,
        )


class AsyncMuteResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncMuteResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncMuteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMuteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncMuteResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MuteCreateResponse:
        """
        Mutes a user through a connected X account. The user's posts leave that
        account's timelines, and X doesn't tell the user.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._post(
            path_template("/x/users/{id}/mute", id=id),
            body=await async_maybe_transform({"account": account}, mute_create_params.MuteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MuteCreateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MuteDeleteResponse:
        """
        Unmutes a user through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._delete(
            path_template("/x/users/{id}/mute", id=id),
            body=await async_maybe_transform({"account": account}, mute_delete_params.MuteDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MuteDeleteResponse,
        )


class MuteResourceWithRawResponse:
    def __init__(self, mute: MuteResource) -> None:
        self._mute = mute

        self.create = to_raw_response_wrapper(
            mute.create,
        )
        self.delete = to_raw_response_wrapper(
            mute.delete,
        )


class AsyncMuteResourceWithRawResponse:
    def __init__(self, mute: AsyncMuteResource) -> None:
        self._mute = mute

        self.create = async_to_raw_response_wrapper(
            mute.create,
        )
        self.delete = async_to_raw_response_wrapper(
            mute.delete,
        )


class MuteResourceWithStreamingResponse:
    def __init__(self, mute: MuteResource) -> None:
        self._mute = mute

        self.create = to_streamed_response_wrapper(
            mute.create,
        )
        self.delete = to_streamed_response_wrapper(
            mute.delete,
        )


class AsyncMuteResourceWithStreamingResponse:
    def __init__(self, mute: AsyncMuteResource) -> None:
        self._mute = mute

        self.create = async_to_streamed_response_wrapper(
            mute.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            mute.delete,
        )
