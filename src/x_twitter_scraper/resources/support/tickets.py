# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.support import ticket_reply_params, ticket_create_params, ticket_update_params
from ...types.support.ticket_list_response import TicketListResponse
from ...types.support.ticket_reply_response import TicketReplyResponse
from ...types.support.ticket_create_response import TicketCreateResponse
from ...types.support.ticket_update_response import TicketUpdateResponse
from ...types.support.ticket_retrieve_response import TicketRetrieveResponse

__all__ = ["TicketsResource", "AsyncTicketsResource"]


class TicketsResource(SyncAPIResource):
    """Support ticket management"""

    @cached_property
    def with_raw_response(self) -> TicketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return TicketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TicketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return TicketsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        subject: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketCreateResponse:
        """
        Create a support ticket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "content": content,
                "subject": subject,
            },
            [["attachments", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["attachments", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/support/tickets",
            body=maybe_transform(body, ticket_create_params.TicketCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketCreateResponse,
        )

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
    ) -> TicketRetrieveResponse:
        """
        Get ticket with all messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/support/tickets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["open", "resolved", "closed"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketUpdateResponse:
        """
        Update ticket status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/support/tickets/{id}", id=id),
            body=maybe_transform({"status": status}, ticket_update_params.TicketUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketListResponse:
        """List user's support tickets"""
        return self._get(
            "/support/tickets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketListResponse,
        )

    def reply(
        self,
        id: str,
        *,
        content: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketReplyResponse:
        """
        Reply to a support ticket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths({"content": content}, [["attachments", "<array>"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["attachments", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/support/tickets/{id}/messages", id=id),
            body=maybe_transform(body, ticket_reply_params.TicketReplyParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketReplyResponse,
        )


class AsyncTicketsResource(AsyncAPIResource):
    """Support ticket management"""

    @cached_property
    def with_raw_response(self) -> AsyncTicketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTicketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTicketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncTicketsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        subject: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketCreateResponse:
        """
        Create a support ticket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "content": content,
                "subject": subject,
            },
            [["attachments", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["attachments", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/support/tickets",
            body=await async_maybe_transform(body, ticket_create_params.TicketCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketCreateResponse,
        )

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
    ) -> TicketRetrieveResponse:
        """
        Get ticket with all messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/support/tickets/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["open", "resolved", "closed"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketUpdateResponse:
        """
        Update ticket status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/support/tickets/{id}", id=id),
            body=await async_maybe_transform({"status": status}, ticket_update_params.TicketUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketListResponse:
        """List user's support tickets"""
        return await self._get(
            "/support/tickets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketListResponse,
        )

    async def reply(
        self,
        id: str,
        *,
        content: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TicketReplyResponse:
        """
        Reply to a support ticket

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        body = deepcopy_with_paths({"content": content}, [["attachments", "<array>"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["attachments", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/support/tickets/{id}/messages", id=id),
            body=await async_maybe_transform(body, ticket_reply_params.TicketReplyParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketReplyResponse,
        )


class TicketsResourceWithRawResponse:
    def __init__(self, tickets: TicketsResource) -> None:
        self._tickets = tickets

        self.create = to_raw_response_wrapper(
            tickets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tickets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tickets.update,
        )
        self.list = to_raw_response_wrapper(
            tickets.list,
        )
        self.reply = to_raw_response_wrapper(
            tickets.reply,
        )


class AsyncTicketsResourceWithRawResponse:
    def __init__(self, tickets: AsyncTicketsResource) -> None:
        self._tickets = tickets

        self.create = async_to_raw_response_wrapper(
            tickets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tickets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tickets.update,
        )
        self.list = async_to_raw_response_wrapper(
            tickets.list,
        )
        self.reply = async_to_raw_response_wrapper(
            tickets.reply,
        )


class TicketsResourceWithStreamingResponse:
    def __init__(self, tickets: TicketsResource) -> None:
        self._tickets = tickets

        self.create = to_streamed_response_wrapper(
            tickets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tickets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tickets.update,
        )
        self.list = to_streamed_response_wrapper(
            tickets.list,
        )
        self.reply = to_streamed_response_wrapper(
            tickets.reply,
        )


class AsyncTicketsResourceWithStreamingResponse:
    def __init__(self, tickets: AsyncTicketsResource) -> None:
        self._tickets = tickets

        self.create = async_to_streamed_response_wrapper(
            tickets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tickets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tickets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tickets.list,
        )
        self.reply = async_to_streamed_response_wrapper(
            tickets.reply,
        )
