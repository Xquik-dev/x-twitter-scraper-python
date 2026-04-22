# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .follow import (
    FollowResource,
    AsyncFollowResource,
    FollowResourceWithRawResponse,
    AsyncFollowResourceWithRawResponse,
    FollowResourceWithStreamingResponse,
    AsyncFollowResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.x import (
    user_retrieve_batch_params,
    user_retrieve_likes_params,
    user_retrieve_media_params,
    user_retrieve_search_params,
    user_retrieve_tweets_params,
    user_retrieve_mentions_params,
    user_retrieve_followers_params,
    user_retrieve_following_params,
    user_retrieve_followers_you_know_params,
    user_retrieve_verified_followers_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.user_profile import UserProfile
from ....types.shared.paginated_users import PaginatedUsers
from ....types.shared.paginated_tweets import PaginatedTweets

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """Look up, search, and explore user profiles and relationships"""

    @cached_property
    def follow(self) -> FollowResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Get user profile with follower counts & verification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfile,
        )

    def retrieve_batch(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Look up multiple users by IDs in one call

        Args:
          ids: Comma-separated user IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/users/batch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List followers of a user

        Args:
          cursor: Pagination cursor for followers list

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    user_retrieve_followers_params.UserRetrieveFollowersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_followers_you_know(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List mutual followers between you and a user

        Args:
          cursor: Pagination cursor for followers-you-know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/followers-you-know", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor}, user_retrieve_followers_you_know_params.UserRetrieveFollowersYouKnowParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_following(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List accounts a user follows

        Args:
          cursor: Pagination cursor for following list

          page_size: Results per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/following", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    user_retrieve_following_params.UserRetrieveFollowingParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_likes(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets liked by a user

        Args:
          cursor: Pagination cursor for liked tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/likes", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, user_retrieve_likes_params.UserRetrieveLikesParams),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_media(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List media tweets posted by a user

        Args:
          cursor: Pagination cursor for media tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/media", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, user_retrieve_media_params.UserRetrieveMediaParams),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_mentions(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        since_time: str | Omit = omit,
        until_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets mentioning a user

        Args:
          cursor: Pagination cursor for mentions

          since_time: Unix timestamp - return mentions after this time

          until_time: Unix timestamp - return mentions before this time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/mentions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Search users by name or username

        Args:
          q: User search query

          cursor: Pagination cursor for user search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/users/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                    },
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_tweets(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        include_parent_tweet: bool | Omit = omit,
        include_replies: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List recent tweets posted by a user

        Args:
          cursor: Pagination cursor for user tweets

          include_parent_tweet: Include parent tweet for replies

          include_replies: Include reply tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_parent_tweet": include_parent_tweet,
                        "include_replies": include_replies,
                    },
                    user_retrieve_tweets_params.UserRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_verified_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List verified followers of a user

        Args:
          cursor: Pagination cursor for verified followers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/verified-followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor}, user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )


class AsyncUsersResource(AsyncAPIResource):
    """Look up, search, and explore user profiles and relationships"""

    @cached_property
    def follow(self) -> AsyncFollowResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Get user profile with follower counts & verification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfile,
        )

    async def retrieve_batch(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Look up multiple users by IDs in one call

        Args:
          ids: Comma-separated user IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/users/batch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List followers of a user

        Args:
          cursor: Pagination cursor for followers list

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    user_retrieve_followers_params.UserRetrieveFollowersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_followers_you_know(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List mutual followers between you and a user

        Args:
          cursor: Pagination cursor for followers-you-know

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/followers-you-know", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, user_retrieve_followers_you_know_params.UserRetrieveFollowersYouKnowParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_following(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List accounts a user follows

        Args:
          cursor: Pagination cursor for following list

          page_size: Results per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/following", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    user_retrieve_following_params.UserRetrieveFollowingParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_likes(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets liked by a user

        Args:
          cursor: Pagination cursor for liked tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/likes", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, user_retrieve_likes_params.UserRetrieveLikesParams
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_media(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List media tweets posted by a user

        Args:
          cursor: Pagination cursor for media tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/media", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, user_retrieve_media_params.UserRetrieveMediaParams
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_mentions(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        since_time: str | Omit = omit,
        until_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets mentioning a user

        Args:
          cursor: Pagination cursor for mentions

          since_time: Unix timestamp - return mentions after this time

          until_time: Unix timestamp - return mentions before this time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/mentions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Search users by name or username

        Args:
          q: User search query

          cursor: Pagination cursor for user search

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/users/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                    },
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_tweets(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        include_parent_tweet: bool | Omit = omit,
        include_replies: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List recent tweets posted by a user

        Args:
          cursor: Pagination cursor for user tweets

          include_parent_tweet: Include parent tweet for replies

          include_replies: Include reply tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_parent_tweet": include_parent_tweet,
                        "include_replies": include_replies,
                    },
                    user_retrieve_tweets_params.UserRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_verified_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List verified followers of a user

        Args:
          cursor: Pagination cursor for verified followers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/verified-followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.retrieve_batch = to_raw_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_followers = to_raw_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = to_raw_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = to_raw_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_likes = to_raw_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_media = to_raw_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = to_raw_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_search = to_raw_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_tweets = to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_raw_response_wrapper(
            users.retrieve_verified_followers,
        )

    @cached_property
    def follow(self) -> FollowResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResourceWithRawResponse(self._users.follow)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.retrieve_batch = async_to_raw_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_followers = async_to_raw_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = async_to_raw_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = async_to_raw_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_likes = async_to_raw_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_media = async_to_raw_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = async_to_raw_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_search = async_to_raw_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_tweets = async_to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_raw_response_wrapper(
            users.retrieve_verified_followers,
        )

    @cached_property
    def follow(self) -> AsyncFollowResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResourceWithRawResponse(self._users.follow)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.retrieve_batch = to_streamed_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_followers = to_streamed_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = to_streamed_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = to_streamed_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_likes = to_streamed_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_media = to_streamed_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = to_streamed_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_search = to_streamed_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_tweets = to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_streamed_response_wrapper(
            users.retrieve_verified_followers,
        )

    @cached_property
    def follow(self) -> FollowResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResourceWithStreamingResponse(self._users.follow)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.retrieve_batch = async_to_streamed_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_followers = async_to_streamed_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = async_to_streamed_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = async_to_streamed_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_likes = async_to_streamed_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_media = async_to_streamed_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = async_to_streamed_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_search = async_to_streamed_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_tweets = async_to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_streamed_response_wrapper(
            users.retrieve_verified_followers,
        )

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResourceWithStreamingResponse(self._users.follow)
