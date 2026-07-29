# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

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
from ...types.x.account_connection_attempt_retrieve_response import AccountConnectionAttemptRetrieveResponse

__all__ = ["AccountConnectionAttemptsResource", "AsyncAccountConnectionAttemptsResource"]


class AccountConnectionAttemptsResource(SyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AccountConnectionAttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AccountConnectionAttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountConnectionAttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AccountConnectionAttemptsResourceWithStreamingResponse(self)

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
    ) -> AccountConnectionAttemptRetrieveResponse:
        """
        Get X account connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AccountConnectionAttemptRetrieveResponse,
            self._get(
                path_template("/x/account-connection-attempts/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountConnectionAttemptRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAccountConnectionAttemptsResource(AsyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AsyncAccountConnectionAttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountConnectionAttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountConnectionAttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncAccountConnectionAttemptsResourceWithStreamingResponse(self)

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
    ) -> AccountConnectionAttemptRetrieveResponse:
        """
        Get X account connection status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            AccountConnectionAttemptRetrieveResponse,
            await self._get(
                path_template("/x/account-connection-attempts/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountConnectionAttemptRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AccountConnectionAttemptsResourceWithRawResponse:
    def __init__(self, account_connection_attempts: AccountConnectionAttemptsResource) -> None:
        self._account_connection_attempts = account_connection_attempts

        self.retrieve = to_raw_response_wrapper(
            account_connection_attempts.retrieve,
        )


class AsyncAccountConnectionAttemptsResourceWithRawResponse:
    def __init__(self, account_connection_attempts: AsyncAccountConnectionAttemptsResource) -> None:
        self._account_connection_attempts = account_connection_attempts

        self.retrieve = async_to_raw_response_wrapper(
            account_connection_attempts.retrieve,
        )


class AccountConnectionAttemptsResourceWithStreamingResponse:
    def __init__(self, account_connection_attempts: AccountConnectionAttemptsResource) -> None:
        self._account_connection_attempts = account_connection_attempts

        self.retrieve = to_streamed_response_wrapper(
            account_connection_attempts.retrieve,
        )


class AsyncAccountConnectionAttemptsResourceWithStreamingResponse:
    def __init__(self, account_connection_attempts: AsyncAccountConnectionAttemptsResource) -> None:
        self._account_connection_attempts = account_connection_attempts

        self.retrieve = async_to_streamed_response_wrapper(
            account_connection_attempts.retrieve,
        )
