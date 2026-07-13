# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.write_action_retrieve_response import WriteActionRetrieveResponse

__all__ = ["WriteActionsResource", "AsyncWriteActionsResource"]


class WriteActionsResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> WriteActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return WriteActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WriteActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return WriteActionsResourceWithStreamingResponse(self)

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
    ) -> WriteActionRetrieveResponse:
        """
        Get write action status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/write-actions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WriteActionRetrieveResponse,
        )


class AsyncWriteActionsResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncWriteActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWriteActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWriteActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncWriteActionsResourceWithStreamingResponse(self)

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
    ) -> WriteActionRetrieveResponse:
        """
        Get write action status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/write-actions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WriteActionRetrieveResponse,
        )


class WriteActionsResourceWithRawResponse:
    def __init__(self, write_actions: WriteActionsResource) -> None:
        self._write_actions = write_actions

        self.retrieve = to_raw_response_wrapper(
            write_actions.retrieve,
        )


class AsyncWriteActionsResourceWithRawResponse:
    def __init__(self, write_actions: AsyncWriteActionsResource) -> None:
        self._write_actions = write_actions

        self.retrieve = async_to_raw_response_wrapper(
            write_actions.retrieve,
        )


class WriteActionsResourceWithStreamingResponse:
    def __init__(self, write_actions: WriteActionsResource) -> None:
        self._write_actions = write_actions

        self.retrieve = to_streamed_response_wrapper(
            write_actions.retrieve,
        )


class AsyncWriteActionsResourceWithStreamingResponse:
    def __init__(self, write_actions: AsyncWriteActionsResource) -> None:
        self._write_actions = write_actions

        self.retrieve = async_to_streamed_response_wrapper(
            write_actions.retrieve,
        )
