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
from ....types.x.tweets import bookmark_create_params, bookmark_delete_params
from ....types.x.tweets.bookmark_create_response import BookmarkCreateResponse
from ....types.x.tweets.bookmark_delete_response import BookmarkDeleteResponse

__all__ = ["BookmarkResource", "AsyncBookmarkResource"]


class BookmarkResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> BookmarkResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return BookmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return BookmarkResourceWithStreamingResponse(self)

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
    ) -> BookmarkCreateResponse:
        """
        Bookmarks a post through a connected X account. Only that account sees its
        bookmarks, and GET /x/bookmarks lists them.

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
            path_template("/x/tweets/{id}/bookmark", id=id),
            body=maybe_transform({"account": account}, bookmark_create_params.BookmarkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
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
    ) -> BookmarkDeleteResponse:
        """
        Removes a bookmark through a connected X account.

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
            path_template("/x/tweets/{id}/bookmark", id=id),
            body=maybe_transform({"account": account}, bookmark_delete_params.BookmarkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkDeleteResponse,
        )


class AsyncBookmarkResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncBookmarkResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncBookmarkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncBookmarkResourceWithStreamingResponse(self)

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
    ) -> BookmarkCreateResponse:
        """
        Bookmarks a post through a connected X account. Only that account sees its
        bookmarks, and GET /x/bookmarks lists them.

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
            path_template("/x/tweets/{id}/bookmark", id=id),
            body=await async_maybe_transform({"account": account}, bookmark_create_params.BookmarkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkCreateResponse,
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
    ) -> BookmarkDeleteResponse:
        """
        Removes a bookmark through a connected X account.

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
            path_template("/x/tweets/{id}/bookmark", id=id),
            body=await async_maybe_transform({"account": account}, bookmark_delete_params.BookmarkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkDeleteResponse,
        )


class BookmarkResourceWithRawResponse:
    def __init__(self, bookmark: BookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = to_raw_response_wrapper(
            bookmark.create,
        )
        self.delete = to_raw_response_wrapper(
            bookmark.delete,
        )


class AsyncBookmarkResourceWithRawResponse:
    def __init__(self, bookmark: AsyncBookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = async_to_raw_response_wrapper(
            bookmark.create,
        )
        self.delete = async_to_raw_response_wrapper(
            bookmark.delete,
        )


class BookmarkResourceWithStreamingResponse:
    def __init__(self, bookmark: BookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = to_streamed_response_wrapper(
            bookmark.create,
        )
        self.delete = to_streamed_response_wrapper(
            bookmark.delete,
        )


class AsyncBookmarkResourceWithStreamingResponse:
    def __init__(self, bookmark: AsyncBookmarkResource) -> None:
        self._bookmark = bookmark

        self.create = async_to_streamed_response_wrapper(
            bookmark.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            bookmark.delete,
        )
