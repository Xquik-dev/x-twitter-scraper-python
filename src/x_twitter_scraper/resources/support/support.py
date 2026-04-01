# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tickets import (
    TicketsResource,
    AsyncTicketsResource,
    TicketsResourceWithRawResponse,
    AsyncTicketsResourceWithRawResponse,
    TicketsResourceWithStreamingResponse,
    AsyncTicketsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SupportResource", "AsyncSupportResource"]


class SupportResource(SyncAPIResource):
    @cached_property
    def tickets(self) -> TicketsResource:
        """Support ticket management"""
        return TicketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return SupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return SupportResourceWithStreamingResponse(self)


class AsyncSupportResource(AsyncAPIResource):
    @cached_property
    def tickets(self) -> AsyncTicketsResource:
        """Support ticket management"""
        return AsyncTicketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSupportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSupportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSupportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncSupportResourceWithStreamingResponse(self)


class SupportResourceWithRawResponse:
    def __init__(self, support: SupportResource) -> None:
        self._support = support

    @cached_property
    def tickets(self) -> TicketsResourceWithRawResponse:
        """Support ticket management"""
        return TicketsResourceWithRawResponse(self._support.tickets)


class AsyncSupportResourceWithRawResponse:
    def __init__(self, support: AsyncSupportResource) -> None:
        self._support = support

    @cached_property
    def tickets(self) -> AsyncTicketsResourceWithRawResponse:
        """Support ticket management"""
        return AsyncTicketsResourceWithRawResponse(self._support.tickets)


class SupportResourceWithStreamingResponse:
    def __init__(self, support: SupportResource) -> None:
        self._support = support

    @cached_property
    def tickets(self) -> TicketsResourceWithStreamingResponse:
        """Support ticket management"""
        return TicketsResourceWithStreamingResponse(self._support.tickets)


class AsyncSupportResourceWithStreamingResponse:
    def __init__(self, support: AsyncSupportResource) -> None:
        self._support = support

    @cached_property
    def tickets(self) -> AsyncTicketsResourceWithStreamingResponse:
        """Support ticket management"""
        return AsyncTicketsResourceWithStreamingResponse(self._support.tickets)
