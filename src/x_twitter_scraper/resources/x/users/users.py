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
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.x.user_retrieve_response import UserRetrieveResponse
from ....types.x.user_retrieve_likes_response import UserRetrieveLikesResponse
from ....types.x.user_retrieve_media_response import UserRetrieveMediaResponse
from ....types.x.user_retrieve_tweets_response import UserRetrieveTweetsResponse
from ....types.x.user_retrieve_followers_you_know_response import UserRetrieveFollowersYouKnowResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """X data lookups (subscription required)"""

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
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Look up X user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/x/users/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
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
    ) -> None:
        """
        Get multiple users by IDs

        Args:
          ids: Comma-separated user IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/x/users/batch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Get user followers

        Args:
          cursor: Pagination cursor

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveFollowersYouKnowResponse:
        """
        Get followers you know for a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveFollowersYouKnowResponse,
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
    ) -> None:
        """
        Get users this user follows

        Args:
          cursor: Pagination cursor

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveLikesResponse:
        """
        Get tweets liked by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveLikesResponse,
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
    ) -> UserRetrieveMediaResponse:
        """
        Get media tweets by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveMediaResponse,
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
    ) -> None:
        """
        Get tweets mentioning a user

        Args:
          cursor: Pagination cursor

          since_time: Unix timestamp - filter after

          until_time: Unix timestamp - filter before

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> None:
        """
        Search users by name or username

        Args:
          q: Search query

          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveTweetsResponse:
        """
        Get recent tweets by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveTweetsResponse,
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
    ) -> None:
        """
        Get verified followers

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
        )


class AsyncUsersResource(AsyncAPIResource):
    """X data lookups (subscription required)"""

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
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Look up X user

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/x/users/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
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
    ) -> None:
        """
        Get multiple users by IDs

        Args:
          ids: Comma-separated user IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/x/users/batch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=NoneType,
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
    ) -> None:
        """
        Get user followers

        Args:
          cursor: Pagination cursor

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveFollowersYouKnowResponse:
        """
        Get followers you know for a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveFollowersYouKnowResponse,
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
    ) -> None:
        """
        Get users this user follows

        Args:
          cursor: Pagination cursor

          page_size: Items per page (20-200, default 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveLikesResponse:
        """
        Get tweets liked by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveLikesResponse,
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
    ) -> UserRetrieveMediaResponse:
        """
        Get media tweets by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveMediaResponse,
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
    ) -> None:
        """
        Get tweets mentioning a user

        Args:
          cursor: Pagination cursor

          since_time: Unix timestamp - filter after

          until_time: Unix timestamp - filter before

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> None:
        """
        Search users by name or username

        Args:
          q: Search query

          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
    ) -> UserRetrieveTweetsResponse:
        """
        Get recent tweets by a user

        Args:
          cursor: Pagination cursor from previous response

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
            cast_to=UserRetrieveTweetsResponse,
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
    ) -> None:
        """
        Get verified followers

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            cast_to=NoneType,
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
