# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .dm import (
    DmResource,
    AsyncDmResource,
    DmResourceWithRawResponse,
    AsyncDmResourceWithRawResponse,
    DmResourceWithStreamingResponse,
    AsyncDmResourceWithStreamingResponse,
)
from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from ...types import x_get_home_timeline_params, x_get_notifications_params
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .bookmarks import (
    BookmarksResource,
    AsyncBookmarksResource,
    BookmarksResourceWithRawResponse,
    AsyncBookmarksResourceWithRawResponse,
    BookmarksResourceWithStreamingResponse,
    AsyncBookmarksResourceWithStreamingResponse,
)
from .followers import (
    FollowersResource,
    AsyncFollowersResource,
    FollowersResourceWithRawResponse,
    AsyncFollowersResourceWithRawResponse,
    FollowersResourceWithStreamingResponse,
    AsyncFollowersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .tweets.tweets import (
    TweetsResource,
    AsyncTweetsResource,
    TweetsResourceWithRawResponse,
    AsyncTweetsResourceWithRawResponse,
    TweetsResourceWithStreamingResponse,
    AsyncTweetsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .communities.communities import (
    CommunitiesResource,
    AsyncCommunitiesResource,
    CommunitiesResourceWithRawResponse,
    AsyncCommunitiesResourceWithRawResponse,
    CommunitiesResourceWithStreamingResponse,
    AsyncCommunitiesResourceWithStreamingResponse,
)
from ...types.x_get_trends_response import XGetTrendsResponse
from ...types.x_get_article_response import XGetArticleResponse
from ...types.shared.paginated_tweets import PaginatedTweets
from ...types.x_get_notifications_response import XGetNotificationsResponse

__all__ = ["XResource", "AsyncXResource"]


class XResource(SyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def tweets(self) -> TweetsResource:
        return TweetsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        """X data lookups (subscription required)"""
        return UsersResource(self._client)

    @cached_property
    def followers(self) -> FollowersResource:
        """X data lookups (subscription required)"""
        return FollowersResource(self._client)

    @cached_property
    def dm(self) -> DmResource:
        return DmResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        """Media upload & download"""
        return MediaResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResource(self._client)

    @cached_property
    def communities(self) -> CommunitiesResource:
        return CommunitiesResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        """Connected X account management"""
        return AccountsResource(self._client)

    @cached_property
    def bookmarks(self) -> BookmarksResource:
        """X data lookups (subscription required)"""
        return BookmarksResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        """X data lookups (subscription required)"""
        return ListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> XResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return XResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return XResourceWithStreamingResponse(self)

    def get_article(
        self,
        tweet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetArticleResponse:
        """
        Retrieve the full content of an X Article (long-form post) by tweet ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return self._get(
            path_template("/x/articles/{tweet_id}", tweet_id=tweet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XGetArticleResponse,
        )

    def get_home_timeline(
        self,
        *,
        cursor: str | Omit = omit,
        seen_tweet_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get home timeline

        Args:
          cursor: Pagination cursor for timeline

          seen_tweet_ids: Comma-separated tweet IDs to exclude from results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "seen_tweet_ids": seen_tweet_ids,
                    },
                    x_get_home_timeline_params.XGetHomeTimelineParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_notifications(
        self,
        *,
        cursor: str | Omit = omit,
        type: Literal["All", "Verified", "Mentions"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetNotificationsResponse:
        """
        Get notifications

        Args:
          cursor: Pagination cursor for notifications

          type: Notification type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    x_get_notifications_params.XGetNotificationsParams,
                ),
            ),
            cast_to=XGetNotificationsResponse,
        )

    def get_trends(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendsResponse:
        """Get trending topics"""
        return self._get(
            "/x/trends",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XGetTrendsResponse,
        )


class AsyncXResource(AsyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def tweets(self) -> AsyncTweetsResource:
        return AsyncTweetsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """X data lookups (subscription required)"""
        return AsyncUsersResource(self._client)

    @cached_property
    def followers(self) -> AsyncFollowersResource:
        """X data lookups (subscription required)"""
        return AsyncFollowersResource(self._client)

    @cached_property
    def dm(self) -> AsyncDmResource:
        return AsyncDmResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        """Media upload & download"""
        return AsyncMediaResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResource(self._client)

    @cached_property
    def communities(self) -> AsyncCommunitiesResource:
        return AsyncCommunitiesResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Connected X account management"""
        return AsyncAccountsResource(self._client)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResource:
        """X data lookups (subscription required)"""
        return AsyncBookmarksResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        """X data lookups (subscription required)"""
        return AsyncListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncXResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncXResourceWithStreamingResponse(self)

    async def get_article(
        self,
        tweet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetArticleResponse:
        """
        Retrieve the full content of an X Article (long-form post) by tweet ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return await self._get(
            path_template("/x/articles/{tweet_id}", tweet_id=tweet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XGetArticleResponse,
        )

    async def get_home_timeline(
        self,
        *,
        cursor: str | Omit = omit,
        seen_tweet_ids: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get home timeline

        Args:
          cursor: Pagination cursor for timeline

          seen_tweet_ids: Comma-separated tweet IDs to exclude from results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "seen_tweet_ids": seen_tweet_ids,
                    },
                    x_get_home_timeline_params.XGetHomeTimelineParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_notifications(
        self,
        *,
        cursor: str | Omit = omit,
        type: Literal["All", "Verified", "Mentions"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetNotificationsResponse:
        """
        Get notifications

        Args:
          cursor: Pagination cursor for notifications

          type: Notification type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    x_get_notifications_params.XGetNotificationsParams,
                ),
            ),
            cast_to=XGetNotificationsResponse,
        )

    async def get_trends(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendsResponse:
        """Get trending topics"""
        return await self._get(
            "/x/trends",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XGetTrendsResponse,
        )


class XResourceWithRawResponse:
    def __init__(self, x: XResource) -> None:
        self._x = x

        self.get_article = to_raw_response_wrapper(
            x.get_article,
        )
        self.get_home_timeline = to_raw_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = to_raw_response_wrapper(
            x.get_notifications,
        )
        self.get_trends = to_raw_response_wrapper(
            x.get_trends,
        )

    @cached_property
    def tweets(self) -> TweetsResourceWithRawResponse:
        return TweetsResourceWithRawResponse(self._x.tweets)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return UsersResourceWithRawResponse(self._x.users)

    @cached_property
    def followers(self) -> FollowersResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return FollowersResourceWithRawResponse(self._x.followers)

    @cached_property
    def dm(self) -> DmResourceWithRawResponse:
        return DmResourceWithRawResponse(self._x.dm)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        """Media upload & download"""
        return MediaResourceWithRawResponse(self._x.media)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResourceWithRawResponse(self._x.profile)

    @cached_property
    def communities(self) -> CommunitiesResourceWithRawResponse:
        return CommunitiesResourceWithRawResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Connected X account management"""
        return AccountsResourceWithRawResponse(self._x.accounts)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return BookmarksResourceWithRawResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return ListsResourceWithRawResponse(self._x.lists)


class AsyncXResourceWithRawResponse:
    def __init__(self, x: AsyncXResource) -> None:
        self._x = x

        self.get_article = async_to_raw_response_wrapper(
            x.get_article,
        )
        self.get_home_timeline = async_to_raw_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = async_to_raw_response_wrapper(
            x.get_notifications,
        )
        self.get_trends = async_to_raw_response_wrapper(
            x.get_trends,
        )

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithRawResponse:
        return AsyncTweetsResourceWithRawResponse(self._x.tweets)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return AsyncUsersResourceWithRawResponse(self._x.users)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return AsyncFollowersResourceWithRawResponse(self._x.followers)

    @cached_property
    def dm(self) -> AsyncDmResourceWithRawResponse:
        return AsyncDmResourceWithRawResponse(self._x.dm)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        """Media upload & download"""
        return AsyncMediaResourceWithRawResponse(self._x.media)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResourceWithRawResponse(self._x.profile)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithRawResponse:
        return AsyncCommunitiesResourceWithRawResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Connected X account management"""
        return AsyncAccountsResourceWithRawResponse(self._x.accounts)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return AsyncBookmarksResourceWithRawResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return AsyncListsResourceWithRawResponse(self._x.lists)


class XResourceWithStreamingResponse:
    def __init__(self, x: XResource) -> None:
        self._x = x

        self.get_article = to_streamed_response_wrapper(
            x.get_article,
        )
        self.get_home_timeline = to_streamed_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = to_streamed_response_wrapper(
            x.get_notifications,
        )
        self.get_trends = to_streamed_response_wrapper(
            x.get_trends,
        )

    @cached_property
    def tweets(self) -> TweetsResourceWithStreamingResponse:
        return TweetsResourceWithStreamingResponse(self._x.tweets)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return UsersResourceWithStreamingResponse(self._x.users)

    @cached_property
    def followers(self) -> FollowersResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return FollowersResourceWithStreamingResponse(self._x.followers)

    @cached_property
    def dm(self) -> DmResourceWithStreamingResponse:
        return DmResourceWithStreamingResponse(self._x.dm)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        """Media upload & download"""
        return MediaResourceWithStreamingResponse(self._x.media)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResourceWithStreamingResponse(self._x.profile)

    @cached_property
    def communities(self) -> CommunitiesResourceWithStreamingResponse:
        return CommunitiesResourceWithStreamingResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Connected X account management"""
        return AccountsResourceWithStreamingResponse(self._x.accounts)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return BookmarksResourceWithStreamingResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return ListsResourceWithStreamingResponse(self._x.lists)


class AsyncXResourceWithStreamingResponse:
    def __init__(self, x: AsyncXResource) -> None:
        self._x = x

        self.get_article = async_to_streamed_response_wrapper(
            x.get_article,
        )
        self.get_home_timeline = async_to_streamed_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = async_to_streamed_response_wrapper(
            x.get_notifications,
        )
        self.get_trends = async_to_streamed_response_wrapper(
            x.get_trends,
        )

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithStreamingResponse:
        return AsyncTweetsResourceWithStreamingResponse(self._x.tweets)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return AsyncUsersResourceWithStreamingResponse(self._x.users)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return AsyncFollowersResourceWithStreamingResponse(self._x.followers)

    @cached_property
    def dm(self) -> AsyncDmResourceWithStreamingResponse:
        return AsyncDmResourceWithStreamingResponse(self._x.dm)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        """Media upload & download"""
        return AsyncMediaResourceWithStreamingResponse(self._x.media)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResourceWithStreamingResponse(self._x.profile)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        return AsyncCommunitiesResourceWithStreamingResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Connected X account management"""
        return AsyncAccountsResourceWithStreamingResponse(self._x.accounts)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return AsyncBookmarksResourceWithStreamingResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return AsyncListsResourceWithStreamingResponse(self._x.lists)
