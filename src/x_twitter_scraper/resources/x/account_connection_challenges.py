# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import account_connection_challenge_submit_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.account_connection_challenge_submit_response import AccountConnectionChallengeSubmitResponse

__all__ = ["AccountConnectionChallengesResource", "AsyncAccountConnectionChallengesResource"]


class AccountConnectionChallengesResource(SyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AccountConnectionChallengesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AccountConnectionChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountConnectionChallengesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AccountConnectionChallengesResourceWithStreamingResponse(self)

    def submit(
        self,
        id: str,
        *,
        email_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionChallengeSubmitResponse:
        """
        Submit X account email verification code

        Args:
          email_code: Code sent to the account email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/x/account-connection-challenges/{id}/submit", id=id),
            body=maybe_transform(
                {"email_code": email_code},
                account_connection_challenge_submit_params.AccountConnectionChallengeSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionChallengeSubmitResponse,
        )


class AsyncAccountConnectionChallengesResource(AsyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AsyncAccountConnectionChallengesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountConnectionChallengesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountConnectionChallengesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncAccountConnectionChallengesResourceWithStreamingResponse(self)

    async def submit(
        self,
        id: str,
        *,
        email_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionChallengeSubmitResponse:
        """
        Submit X account email verification code

        Args:
          email_code: Code sent to the account email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/x/account-connection-challenges/{id}/submit", id=id),
            body=await async_maybe_transform(
                {"email_code": email_code},
                account_connection_challenge_submit_params.AccountConnectionChallengeSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionChallengeSubmitResponse,
        )


class AccountConnectionChallengesResourceWithRawResponse:
    def __init__(self, account_connection_challenges: AccountConnectionChallengesResource) -> None:
        self._account_connection_challenges = account_connection_challenges

        self.submit = to_raw_response_wrapper(
            account_connection_challenges.submit,
        )


class AsyncAccountConnectionChallengesResourceWithRawResponse:
    def __init__(self, account_connection_challenges: AsyncAccountConnectionChallengesResource) -> None:
        self._account_connection_challenges = account_connection_challenges

        self.submit = async_to_raw_response_wrapper(
            account_connection_challenges.submit,
        )


class AccountConnectionChallengesResourceWithStreamingResponse:
    def __init__(self, account_connection_challenges: AccountConnectionChallengesResource) -> None:
        self._account_connection_challenges = account_connection_challenges

        self.submit = to_streamed_response_wrapper(
            account_connection_challenges.submit,
        )


class AsyncAccountConnectionChallengesResourceWithStreamingResponse:
    def __init__(self, account_connection_challenges: AsyncAccountConnectionChallengesResource) -> None:
        self._account_connection_challenges = account_connection_challenges

        self.submit = async_to_streamed_response_wrapper(
            account_connection_challenges.submit,
        )
