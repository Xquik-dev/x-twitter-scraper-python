# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import account_connection_link_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.x_account_connection_link import XAccountConnectionLink
from ...types.x.account_connection_link_create_response import AccountConnectionLinkCreateResponse
from ...types.x.account_connection_link_delete_response import AccountConnectionLinkDeleteResponse

__all__ = ["AccountConnectionLinksResource", "AsyncAccountConnectionLinksResource"]


class AccountConnectionLinksResource(SyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AccountConnectionLinksResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AccountConnectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountConnectionLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AccountConnectionLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | Omit = omit,
        reference: str | Omit = omit,
        return_url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionLinkCreateResponse:
        """
        Creates a link to a page Xquik hosts, where a person connects an X account with
        no Xquik signup. Your backend never receives their password or 2FA secret, and
        the account belongs to you. Send `account_id` to reconnect 1 of your accounts
        instead. Connecting is free. The link works for 30 minutes, & the response is
        the only place its token appears.

        Args:
          account_id: The ID of 1 of your X accounts. The link then reconnects that account.

          reference: Your own ID for this person. It comes back when you read the link.

          return_url: A public https URL the page offers as a button once the account connects. Xquik
              never redirects by itself, & never adds the token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/account-connection-links",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "reference": reference,
                    "return_url": return_url,
                },
                account_connection_link_create_params.AccountConnectionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionLinkCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XAccountConnectionLink:
        """
        Reads what happened on a link. `status` reads `connected` once the person
        finishes, with `x_user_id`, `x_username` & `health`. It never holds the token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/account-connection-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XAccountConnectionLink,
        )

    def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionLinkDeleteResponse:
        """
        Stops a link working. An account it already connected stays connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/x/account-connection-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionLinkDeleteResponse,
        )


class AsyncAccountConnectionLinksResource(AsyncAPIResource):
    """Connected X account management"""

    @cached_property
    def with_raw_response(self) -> AsyncAccountConnectionLinksResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncAccountConnectionLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountConnectionLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncAccountConnectionLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | Omit = omit,
        reference: str | Omit = omit,
        return_url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionLinkCreateResponse:
        """
        Creates a link to a page Xquik hosts, where a person connects an X account with
        no Xquik signup. Your backend never receives their password or 2FA secret, and
        the account belongs to you. Send `account_id` to reconnect 1 of your accounts
        instead. Connecting is free. The link works for 30 minutes, & the response is
        the only place its token appears.

        Args:
          account_id: The ID of 1 of your X accounts. The link then reconnects that account.

          reference: Your own ID for this person. It comes back when you read the link.

          return_url: A public https URL the page offers as a button once the account connects. Xquik
              never redirects by itself, & never adds the token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/account-connection-links",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "reference": reference,
                    "return_url": return_url,
                },
                account_connection_link_create_params.AccountConnectionLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionLinkCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XAccountConnectionLink:
        """
        Reads what happened on a link. `status` reads `connected` once the person
        finishes, with `x_user_id`, `x_username` & `health`. It never holds the token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/account-connection-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=XAccountConnectionLink,
        )

    async def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountConnectionLinkDeleteResponse:
        """
        Stops a link working. An account it already connected stays connected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/x/account-connection-links/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountConnectionLinkDeleteResponse,
        )


class AccountConnectionLinksResourceWithRawResponse:
    def __init__(self, account_connection_links: AccountConnectionLinksResource) -> None:
        self._account_connection_links = account_connection_links

        self.create = to_raw_response_wrapper(
            account_connection_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            account_connection_links.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            account_connection_links.delete,
        )


class AsyncAccountConnectionLinksResourceWithRawResponse:
    def __init__(self, account_connection_links: AsyncAccountConnectionLinksResource) -> None:
        self._account_connection_links = account_connection_links

        self.create = async_to_raw_response_wrapper(
            account_connection_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            account_connection_links.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            account_connection_links.delete,
        )


class AccountConnectionLinksResourceWithStreamingResponse:
    def __init__(self, account_connection_links: AccountConnectionLinksResource) -> None:
        self._account_connection_links = account_connection_links

        self.create = to_streamed_response_wrapper(
            account_connection_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            account_connection_links.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            account_connection_links.delete,
        )


class AsyncAccountConnectionLinksResourceWithStreamingResponse:
    def __init__(self, account_connection_links: AsyncAccountConnectionLinksResource) -> None:
        self._account_connection_links = account_connection_links

        self.create = async_to_streamed_response_wrapper(
            account_connection_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            account_connection_links.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_connection_links.delete,
        )
