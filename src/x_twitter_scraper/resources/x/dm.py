# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import dm_send_params, dm_retrieve_history_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.dm_send_response import DmSendResponse
from ...types.x.dm_retrieve_history_response import DmRetrieveHistoryResponse

__all__ = ["DmResource", "AsyncDmResource"]


class DmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return DmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return DmResourceWithStreamingResponse(self)

    def retrieve_history(
        self,
        user_id: str,
        *,
        cursor: str | Omit = omit,
        max_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmRetrieveHistoryResponse:
        """
        Get DM conversation history

        Args:
          cursor: Pagination cursor from previous response

          max_id: Legacy pagination cursor (backward compat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/x/dm/{user_id}/history", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "max_id": max_id,
                    },
                    dm_retrieve_history_params.DmRetrieveHistoryParams,
                ),
            ),
            cast_to=DmRetrieveHistoryResponse,
        )

    def send(
        self,
        user_id: str,
        *,
        account: str,
        text: str,
        media_ids: SequenceNotStr[str] | Omit = omit,
        reply_to_message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmSendResponse:
        """
        Send direct message

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/x/dm/{user_id}", user_id=user_id),
            body=maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "media_ids": media_ids,
                    "reply_to_message_id": reply_to_message_id,
                },
                dm_send_params.DmSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmSendResponse,
        )


class AsyncDmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncDmResourceWithStreamingResponse(self)

    async def retrieve_history(
        self,
        user_id: str,
        *,
        cursor: str | Omit = omit,
        max_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmRetrieveHistoryResponse:
        """
        Get DM conversation history

        Args:
          cursor: Pagination cursor from previous response

          max_id: Legacy pagination cursor (backward compat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/x/dm/{user_id}/history", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "max_id": max_id,
                    },
                    dm_retrieve_history_params.DmRetrieveHistoryParams,
                ),
            ),
            cast_to=DmRetrieveHistoryResponse,
        )

    async def send(
        self,
        user_id: str,
        *,
        account: str,
        text: str,
        media_ids: SequenceNotStr[str] | Omit = omit,
        reply_to_message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmSendResponse:
        """
        Send direct message

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/x/dm/{user_id}", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "media_ids": media_ids,
                    "reply_to_message_id": reply_to_message_id,
                },
                dm_send_params.DmSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DmSendResponse,
        )


class DmResourceWithRawResponse:
    def __init__(self, dm: DmResource) -> None:
        self._dm = dm

        self.retrieve_history = to_raw_response_wrapper(
            dm.retrieve_history,
        )
        self.send = to_raw_response_wrapper(
            dm.send,
        )


class AsyncDmResourceWithRawResponse:
    def __init__(self, dm: AsyncDmResource) -> None:
        self._dm = dm

        self.retrieve_history = async_to_raw_response_wrapper(
            dm.retrieve_history,
        )
        self.send = async_to_raw_response_wrapper(
            dm.send,
        )


class DmResourceWithStreamingResponse:
    def __init__(self, dm: DmResource) -> None:
        self._dm = dm

        self.retrieve_history = to_streamed_response_wrapper(
            dm.retrieve_history,
        )
        self.send = to_streamed_response_wrapper(
            dm.send,
        )


class AsyncDmResourceWithStreamingResponse:
    def __init__(self, dm: AsyncDmResource) -> None:
        self._dm = dm

        self.retrieve_history = async_to_streamed_response_wrapper(
            dm.retrieve_history,
        )
        self.send = async_to_streamed_response_wrapper(
            dm.send,
        )
