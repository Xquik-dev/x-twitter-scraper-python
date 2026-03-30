# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import bookmark_list_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.paginated_tweets import PaginatedTweets
from ...types.x.bookmark_retrieve_folders_response import BookmarkRetrieveFoldersResponse

__all__ = ["BookmarksResource", "AsyncBookmarksResource"]


class BookmarksResource(SyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> BookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return BookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return BookmarksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get bookmarked tweets

        Args:
          cursor: Pagination cursor from previous response

          folder_id: Optional bookmark folder ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/bookmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "folder_id": folder_id,
                    },
                    bookmark_list_params.BookmarkListParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_folders(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkRetrieveFoldersResponse:
        """Get bookmark folders"""
        return self._get(
            "/x/bookmarks/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkRetrieveFoldersResponse,
        )


class AsyncBookmarksResource(AsyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> AsyncBookmarksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookmarksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookmarksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncBookmarksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        folder_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get bookmarked tweets

        Args:
          cursor: Pagination cursor from previous response

          folder_id: Optional bookmark folder ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/bookmarks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "folder_id": folder_id,
                    },
                    bookmark_list_params.BookmarkListParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_folders(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BookmarkRetrieveFoldersResponse:
        """Get bookmark folders"""
        return await self._get(
            "/x/bookmarks/folders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookmarkRetrieveFoldersResponse,
        )


class BookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.list = to_raw_response_wrapper(
            bookmarks.list,
        )
        self.retrieve_folders = to_raw_response_wrapper(
            bookmarks.retrieve_folders,
        )


class AsyncBookmarksResourceWithRawResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.list = async_to_raw_response_wrapper(
            bookmarks.list,
        )
        self.retrieve_folders = async_to_raw_response_wrapper(
            bookmarks.retrieve_folders,
        )


class BookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: BookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.list = to_streamed_response_wrapper(
            bookmarks.list,
        )
        self.retrieve_folders = to_streamed_response_wrapper(
            bookmarks.retrieve_folders,
        )


class AsyncBookmarksResourceWithStreamingResponse:
    def __init__(self, bookmarks: AsyncBookmarksResource) -> None:
        self._bookmarks = bookmarks

        self.list = async_to_streamed_response_wrapper(
            bookmarks.list,
        )
        self.retrieve_folders = async_to_streamed_response_wrapper(
            bookmarks.retrieve_folders,
        )
