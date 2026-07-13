# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    credit_topup_balance_params,
    credit_retrieve_topup_status_params,
    credit_redirect_topup_checkout_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.credit_topup_balance_response import CreditTopupBalanceResponse
from ..types.credit_retrieve_balance_response import CreditRetrieveBalanceResponse
from ..types.credit_retrieve_topup_status_response import CreditRetrieveTopupStatusResponse

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    """Subscription, billing, and credits"""

    @cached_property
    def with_raw_response(self) -> CreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return CreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return CreditsResourceWithStreamingResponse(self)

    def redirect_topup_checkout(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirect to an active top-up payment page

        Args:
          session_id: Billing session ID returned by the top-up billing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/credits/topup/redirect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"session_id": session_id}, credit_redirect_topup_checkout_params.CreditRedirectTopupCheckoutParams
                ),
                security={},
            ),
            cast_to=NoneType,
        )

    def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditRetrieveBalanceResponse:
        """Get credits balance"""
        return self._get(
            "/credits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditRetrieveBalanceResponse,
        )

    def retrieve_topup_status(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditRetrieveTopupStatusResponse:
        """
        Get top-up billing status

        Args:
          session_id: Billing session ID returned by the top-up billing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/credits/topup/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"session_id": session_id}, credit_retrieve_topup_status_params.CreditRetrieveTopupStatusParams
                ),
            ),
            cast_to=CreditRetrieveTopupStatusResponse,
        )

    def topup_balance(
        self,
        *,
        dollars: int,
        locale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditTopupBalanceResponse:
        """Create a Stripe Checkout session only after the user confirms.

        The request never
        completes payment or adds credits by itself.

        Args:
          dollars: Amount to top up in US dollars. Minimum 10.

          locale: Optional checkout locale. Defaults to en.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credits/topup",
            body=maybe_transform(
                {
                    "dollars": dollars,
                    "locale": locale,
                },
                credit_topup_balance_params.CreditTopupBalanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditTopupBalanceResponse,
        )


class AsyncCreditsResource(AsyncAPIResource):
    """Subscription, billing, and credits"""

    @cached_property
    def with_raw_response(self) -> AsyncCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncCreditsResourceWithStreamingResponse(self)

    async def redirect_topup_checkout(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Redirect to an active top-up payment page

        Args:
          session_id: Billing session ID returned by the top-up billing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/credits/topup/redirect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, credit_redirect_topup_checkout_params.CreditRedirectTopupCheckoutParams
                ),
                security={},
            ),
            cast_to=NoneType,
        )

    async def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditRetrieveBalanceResponse:
        """Get credits balance"""
        return await self._get(
            "/credits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditRetrieveBalanceResponse,
        )

    async def retrieve_topup_status(
        self,
        *,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditRetrieveTopupStatusResponse:
        """
        Get top-up billing status

        Args:
          session_id: Billing session ID returned by the top-up billing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/credits/topup/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, credit_retrieve_topup_status_params.CreditRetrieveTopupStatusParams
                ),
            ),
            cast_to=CreditRetrieveTopupStatusResponse,
        )

    async def topup_balance(
        self,
        *,
        dollars: int,
        locale: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditTopupBalanceResponse:
        """Create a Stripe Checkout session only after the user confirms.

        The request never
        completes payment or adds credits by itself.

        Args:
          dollars: Amount to top up in US dollars. Minimum 10.

          locale: Optional checkout locale. Defaults to en.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credits/topup",
            body=await async_maybe_transform(
                {
                    "dollars": dollars,
                    "locale": locale,
                },
                credit_topup_balance_params.CreditTopupBalanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditTopupBalanceResponse,
        )


class CreditsResourceWithRawResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.redirect_topup_checkout = to_raw_response_wrapper(
            credits.redirect_topup_checkout,
        )
        self.retrieve_balance = to_raw_response_wrapper(
            credits.retrieve_balance,
        )
        self.retrieve_topup_status = to_raw_response_wrapper(
            credits.retrieve_topup_status,
        )
        self.topup_balance = to_raw_response_wrapper(
            credits.topup_balance,
        )


class AsyncCreditsResourceWithRawResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.redirect_topup_checkout = async_to_raw_response_wrapper(
            credits.redirect_topup_checkout,
        )
        self.retrieve_balance = async_to_raw_response_wrapper(
            credits.retrieve_balance,
        )
        self.retrieve_topup_status = async_to_raw_response_wrapper(
            credits.retrieve_topup_status,
        )
        self.topup_balance = async_to_raw_response_wrapper(
            credits.topup_balance,
        )


class CreditsResourceWithStreamingResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.redirect_topup_checkout = to_streamed_response_wrapper(
            credits.redirect_topup_checkout,
        )
        self.retrieve_balance = to_streamed_response_wrapper(
            credits.retrieve_balance,
        )
        self.retrieve_topup_status = to_streamed_response_wrapper(
            credits.retrieve_topup_status,
        )
        self.topup_balance = to_streamed_response_wrapper(
            credits.topup_balance,
        )


class AsyncCreditsResourceWithStreamingResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.redirect_topup_checkout = async_to_streamed_response_wrapper(
            credits.redirect_topup_checkout,
        )
        self.retrieve_balance = async_to_streamed_response_wrapper(
            credits.retrieve_balance,
        )
        self.retrieve_topup_status = async_to_streamed_response_wrapper(
            credits.retrieve_topup_status,
        )
        self.topup_balance = async_to_streamed_response_wrapper(
            credits.topup_balance,
        )
