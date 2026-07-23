# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import guest_wallet_topup_params, guest_wallet_create_params
from .._types import Body, Query, Headers, NotGiven, omit, not_given
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
from ..types.guest_wallet_topup_response import GuestWalletTopupResponse
from ..types.guest_wallet_create_response import GuestWalletCreateResponse
from ..types.guest_wallet_retrieve_status_response import GuestWalletRetrieveStatusResponse

__all__ = ["GuestWalletsResource", "AsyncGuestWalletsResource"]


class GuestWalletsResource(SyncAPIResource):
    """Accountless prepaid access for paid read endpoints"""

    @cached_property
    def with_raw_response(self) -> GuestWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return GuestWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuestWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return GuestWalletsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount_minor: int,
        currency: Literal["usd"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletCreateResponse:
        """
        Create a one-use Stripe-hosted checkout after the user explicitly confirms a
        $10-$250 USD amount. This request creates no charge by itself. The user opens
        checkout_url on Stripe. This endpoint returns the paid-read API key without
        requiring an Xquik account, email, dashboard, or Xquik web page. An idempotent
        replay returns the same key.

        Args:
          amount_minor: USD cents accepted for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-api-key": omit, "Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/guest-wallets",
            body=maybe_transform(
                {
                    "amount_minor": amount_minor,
                    "currency": currency,
                },
                guest_wallet_create_params.GuestWalletCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=GuestWalletCreateResponse,
        )

    def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletRetrieveStatusResponse:
        """Poll after Stripe payment.

        Use usable to decide whether paid reads can run. An
        active wallet can remain usable while a top-up is pending. A new wallet becomes
        usable only after verified webhook fulfillment. Send the guest key as
        Authorization: Bearer.
        """
        return self._get(
            "/guest-wallets/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key": True},
            ),
            cast_to=GuestWalletRetrieveStatusResponse,
        )

    def topup(
        self,
        *,
        amount_minor: int,
        currency: Literal["usd"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletTopupResponse:
        """
        Create a one-use Stripe-hosted checkout for an existing paid-read guest key
        after the user explicitly confirms a $10-$250 USD amount. The key remains the
        same. This request creates no charge by itself and never redirects through an
        Xquik web page.

        Args:
          amount_minor: USD cents accepted for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/guest-wallets/topups",
            body=maybe_transform(
                {
                    "amount_minor": amount_minor,
                    "currency": currency,
                },
                guest_wallet_topup_params.GuestWalletTopupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key": True},
            ),
            cast_to=GuestWalletTopupResponse,
        )


class AsyncGuestWalletsResource(AsyncAPIResource):
    """Accountless prepaid access for paid read endpoints"""

    @cached_property
    def with_raw_response(self) -> AsyncGuestWalletsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuestWalletsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuestWalletsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncGuestWalletsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount_minor: int,
        currency: Literal["usd"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletCreateResponse:
        """
        Create a one-use Stripe-hosted checkout after the user explicitly confirms a
        $10-$250 USD amount. This request creates no charge by itself. The user opens
        checkout_url on Stripe. This endpoint returns the paid-read API key without
        requiring an Xquik account, email, dashboard, or Xquik web page. An idempotent
        replay returns the same key.

        Args:
          amount_minor: USD cents accepted for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"x-api-key": omit, "Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/guest-wallets",
            body=await async_maybe_transform(
                {
                    "amount_minor": amount_minor,
                    "currency": currency,
                },
                guest_wallet_create_params.GuestWalletCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=GuestWalletCreateResponse,
        )

    async def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletRetrieveStatusResponse:
        """Poll after Stripe payment.

        Use usable to decide whether paid reads can run. An
        active wallet can remain usable while a top-up is pending. A new wallet becomes
        usable only after verified webhook fulfillment. Send the guest key as
        Authorization: Bearer.
        """
        return await self._get(
            "/guest-wallets/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key": True},
            ),
            cast_to=GuestWalletRetrieveStatusResponse,
        )

    async def topup(
        self,
        *,
        amount_minor: int,
        currency: Literal["usd"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuestWalletTopupResponse:
        """
        Create a one-use Stripe-hosted checkout for an existing paid-read guest key
        after the user explicitly confirms a $10-$250 USD amount. The key remains the
        same. This request creates no charge by itself and never redirects through an
        Xquik web page.

        Args:
          amount_minor: USD cents accepted for this checkout.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/guest-wallets/topups",
            body=await async_maybe_transform(
                {
                    "amount_minor": amount_minor,
                    "currency": currency,
                },
                guest_wallet_topup_params.GuestWalletTopupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"api_key": True},
            ),
            cast_to=GuestWalletTopupResponse,
        )


class GuestWalletsResourceWithRawResponse:
    def __init__(self, guest_wallets: GuestWalletsResource) -> None:
        self._guest_wallets = guest_wallets

        self.create = to_raw_response_wrapper(
            guest_wallets.create,
        )
        self.retrieve_status = to_raw_response_wrapper(
            guest_wallets.retrieve_status,
        )
        self.topup = to_raw_response_wrapper(
            guest_wallets.topup,
        )


class AsyncGuestWalletsResourceWithRawResponse:
    def __init__(self, guest_wallets: AsyncGuestWalletsResource) -> None:
        self._guest_wallets = guest_wallets

        self.create = async_to_raw_response_wrapper(
            guest_wallets.create,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            guest_wallets.retrieve_status,
        )
        self.topup = async_to_raw_response_wrapper(
            guest_wallets.topup,
        )


class GuestWalletsResourceWithStreamingResponse:
    def __init__(self, guest_wallets: GuestWalletsResource) -> None:
        self._guest_wallets = guest_wallets

        self.create = to_streamed_response_wrapper(
            guest_wallets.create,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            guest_wallets.retrieve_status,
        )
        self.topup = to_streamed_response_wrapper(
            guest_wallets.topup,
        )


class AsyncGuestWalletsResourceWithStreamingResponse:
    def __init__(self, guest_wallets: AsyncGuestWalletsResource) -> None:
        self._guest_wallets = guest_wallets

        self.create = async_to_streamed_response_wrapper(
            guest_wallets.create,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            guest_wallets.retrieve_status,
        )
        self.topup = async_to_streamed_response_wrapper(
            guest_wallets.topup,
        )
