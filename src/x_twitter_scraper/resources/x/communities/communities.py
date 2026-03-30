# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .join import (
    JoinResource,
    AsyncJoinResource,
    JoinResourceWithRawResponse,
    AsyncJoinResourceWithRawResponse,
    JoinResourceWithStreamingResponse,
    AsyncJoinResourceWithStreamingResponse,
)
from .tweets import (
    TweetsResource,
    AsyncTweetsResource,
    TweetsResourceWithRawResponse,
    AsyncTweetsResourceWithRawResponse,
    TweetsResourceWithStreamingResponse,
    AsyncTweetsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.x import (
    community_create_params,
    community_delete_params,
    community_retrieve_search_params,
    community_retrieve_members_params,
    community_retrieve_moderators_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.x.community_create_response import CommunityCreateResponse
from ....types.x.community_delete_response import CommunityDeleteResponse
from ....types.x.community_retrieve_info_response import CommunityRetrieveInfoResponse

__all__ = ["CommunitiesResource", "AsyncCommunitiesResource"]


class CommunitiesResource(SyncAPIResource):
    @cached_property
    def join(self) -> JoinResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResource(self._client)

    @cached_property
    def tweets(self) -> TweetsResource:
        """X data lookups (subscription required)"""
        return TweetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return CommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return CommunitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account: str,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityCreateResponse:
        """
        Create community

        Args:
          account: X account (@username or account ID)

          name: Community name

          description: Community description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/communities",
            body=maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "description": description,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityCreateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        community_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityDeleteResponse:
        """
        Delete community

        Args:
          account: X account (@username or account ID)

          community_name: Community name for confirmation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/x/communities/{id}", id=id),
            body=maybe_transform(
                {
                    "account": account,
                    "community_name": community_name,
                },
                community_delete_params.CommunityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityDeleteResponse,
        )

    def retrieve_info(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityRetrieveInfoResponse:
        """
        Get community details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/communities/{id}/info", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityRetrieveInfoResponse,
        )

    def retrieve_members(
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
        Get community members

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
            path_template("/x/communities/{id}/members", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor}, community_retrieve_members_params.CommunityRetrieveMembersParams
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_moderators(
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
        Get community moderators

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
            path_template("/x/communities/{id}/moderators", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"cursor": cursor}, community_retrieve_moderators_params.CommunityRetrieveModeratorsParams
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        query_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Search tweets across communities

        Args:
          q: Search query

          cursor: Pagination cursor

          query_type: Sort order (Latest or Top)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/x/communities/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "query_type": query_type,
                    },
                    community_retrieve_search_params.CommunityRetrieveSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncCommunitiesResource(AsyncAPIResource):
    @cached_property
    def join(self) -> AsyncJoinResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResource(self._client)

    @cached_property
    def tweets(self) -> AsyncTweetsResource:
        """X data lookups (subscription required)"""
        return AsyncTweetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommunitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncCommunitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account: str,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityCreateResponse:
        """
        Create community

        Args:
          account: X account (@username or account ID)

          name: Community name

          description: Community description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/communities",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "description": description,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityCreateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        community_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityDeleteResponse:
        """
        Delete community

        Args:
          account: X account (@username or account ID)

          community_name: Community name for confirmation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/x/communities/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "account": account,
                    "community_name": community_name,
                },
                community_delete_params.CommunityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityDeleteResponse,
        )

    async def retrieve_info(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityRetrieveInfoResponse:
        """
        Get community details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/communities/{id}/info", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityRetrieveInfoResponse,
        )

    async def retrieve_members(
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
        Get community members

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
            path_template("/x/communities/{id}/members", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, community_retrieve_members_params.CommunityRetrieveMembersParams
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_moderators(
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
        Get community moderators

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
            path_template("/x/communities/{id}/moderators", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, community_retrieve_moderators_params.CommunityRetrieveModeratorsParams
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        query_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Search tweets across communities

        Args:
          q: Search query

          cursor: Pagination cursor

          query_type: Sort order (Latest or Top)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/x/communities/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "query_type": query_type,
                    },
                    community_retrieve_search_params.CommunityRetrieveSearchParams,
                ),
            ),
            cast_to=NoneType,
        )


class CommunitiesResourceWithRawResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_raw_response_wrapper(
            communities.create,
        )
        self.delete = to_raw_response_wrapper(
            communities.delete,
        )
        self.retrieve_info = to_raw_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = to_raw_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = to_raw_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = to_raw_response_wrapper(
            communities.retrieve_search,
        )

    @cached_property
    def join(self) -> JoinResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResourceWithRawResponse(self._communities.join)

    @cached_property
    def tweets(self) -> TweetsResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return TweetsResourceWithRawResponse(self._communities.tweets)


class AsyncCommunitiesResourceWithRawResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_raw_response_wrapper(
            communities.create,
        )
        self.delete = async_to_raw_response_wrapper(
            communities.delete,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = async_to_raw_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = async_to_raw_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = async_to_raw_response_wrapper(
            communities.retrieve_search,
        )

    @cached_property
    def join(self) -> AsyncJoinResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResourceWithRawResponse(self._communities.join)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithRawResponse:
        """X data lookups (subscription required)"""
        return AsyncTweetsResourceWithRawResponse(self._communities.tweets)


class CommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_streamed_response_wrapper(
            communities.create,
        )
        self.delete = to_streamed_response_wrapper(
            communities.delete,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = to_streamed_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = to_streamed_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = to_streamed_response_wrapper(
            communities.retrieve_search,
        )

    @cached_property
    def join(self) -> JoinResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResourceWithStreamingResponse(self._communities.join)

    @cached_property
    def tweets(self) -> TweetsResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return TweetsResourceWithStreamingResponse(self._communities.tweets)


class AsyncCommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_streamed_response_wrapper(
            communities.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            communities.delete,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = async_to_streamed_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = async_to_streamed_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = async_to_streamed_response_wrapper(
            communities.retrieve_search,
        )

    @cached_property
    def join(self) -> AsyncJoinResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResourceWithStreamingResponse(self._communities.join)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithStreamingResponse:
        """X data lookups (subscription required)"""
        return AsyncTweetsResourceWithStreamingResponse(self._communities.tweets)
