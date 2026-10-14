# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import dm_send_params, dm_delete_message_params, dm_retrieve_history_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.dm_send_response import DmSendResponse
from ...types.x.dm_delete_message_response import DmDeleteMessageResponse
from ...types.x.dm_retrieve_history_response import DmRetrieveHistoryResponse

__all__ = ["DmResource", "AsyncDmResource"]


class DmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DmResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return DmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return DmResourceWithStreamingResponse(self)

    def delete_message(
        self,
        message_id: str,
        *,
        user_id: str,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmDeleteMessageResponse:
        """Deletes 1 DM from the account's side; the other person keeps it.

        Success means
        the account's conversation no longer shows it. Still shown gets 422
        `x_dm_not_deleted`, uncharged.

        Args:
          user_id: The other person in the conversation: user ID, username with or without @, or
              URL-encoded profile URL, such as x.com/nasa. Xquik looks up a username's ID
              first. Anything else gets 400 `invalid_user_id`.

          account: Connected X account (@username or ID) that sees the DM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._delete(
            path_template("/x/dm/{user_id}/messages/{message_id}", user_id=user_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account": account}, dm_delete_message_params.DmDeleteMessageParams),
            ),
            cast_to=DmDeleteMessageResponse,
        )

    def retrieve_history(
        self,
        user_id: str,
        *,
        account: str,
        cursor: str | Omit = omit,
        max_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmRetrieveHistoryResponse:
        """
        Returns message history with one user for the connected X account.

        Args:
          account: X handle (without the `@` prefix) of the connected X account used to read the
              conversation. The account must be a participant in the conversation.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

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
                        "account": account,
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
        idempotency_key: str,
        media_ids: SequenceNotStr[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmSendResponse:
        """Sends a direct message through a connected X account.

        Once X rate limits an
        account's DMs, its DMs get 429 until X's reset. Xquik sends nothing to X &
        charges nothing. `Retry-After` & `nextAction.afterMs` give the wait.

        Args:
          account: X account (@username or ID) sending the DM

          media_ids: Optional array containing exactly 1 uploaded media ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._post(
            path_template("/x/dm/{user_id}", user_id=user_id),
            body=maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "media_ids": media_ids,
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
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncDmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncDmResourceWithStreamingResponse(self)

    async def delete_message(
        self,
        message_id: str,
        *,
        user_id: str,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmDeleteMessageResponse:
        """Deletes 1 DM from the account's side; the other person keeps it.

        Success means
        the account's conversation no longer shows it. Still shown gets 422
        `x_dm_not_deleted`, uncharged.

        Args:
          user_id: The other person in the conversation: user ID, username with or without @, or
              URL-encoded profile URL, such as x.com/nasa. Xquik looks up a username's ID
              first. Anything else gets 400 `invalid_user_id`.

          account: Connected X account (@username or ID) that sees the DM.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._delete(
            path_template("/x/dm/{user_id}/messages/{message_id}", user_id=user_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"account": account}, dm_delete_message_params.DmDeleteMessageParams),
            ),
            cast_to=DmDeleteMessageResponse,
        )

    async def retrieve_history(
        self,
        user_id: str,
        *,
        account: str,
        cursor: str | Omit = omit,
        max_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmRetrieveHistoryResponse:
        """
        Returns message history with one user for the connected X account.

        Args:
          account: X handle (without the `@` prefix) of the connected X account used to read the
              conversation. The account must be a participant in the conversation.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

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
                        "account": account,
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
        idempotency_key: str,
        media_ids: SequenceNotStr[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DmSendResponse:
        """Sends a direct message through a connected X account.

        Once X rate limits an
        account's DMs, its DMs get 429 until X's reset. Xquik sends nothing to X &
        charges nothing. `Retry-After` & `nextAction.afterMs` give the wait.

        Args:
          account: X account (@username or ID) sending the DM

          media_ids: Optional array containing exactly 1 uploaded media ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._post(
            path_template("/x/dm/{user_id}", user_id=user_id),
            body=await async_maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "media_ids": media_ids,
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

        self.delete_message = to_raw_response_wrapper(
            dm.delete_message,
        )
        self.retrieve_history = to_raw_response_wrapper(
            dm.retrieve_history,
        )
        self.send = to_raw_response_wrapper(
            dm.send,
        )


class AsyncDmResourceWithRawResponse:
    def __init__(self, dm: AsyncDmResource) -> None:
        self._dm = dm

        self.delete_message = async_to_raw_response_wrapper(
            dm.delete_message,
        )
        self.retrieve_history = async_to_raw_response_wrapper(
            dm.retrieve_history,
        )
        self.send = async_to_raw_response_wrapper(
            dm.send,
        )


class DmResourceWithStreamingResponse:
    def __init__(self, dm: DmResource) -> None:
        self._dm = dm

        self.delete_message = to_streamed_response_wrapper(
            dm.delete_message,
        )
        self.retrieve_history = to_streamed_response_wrapper(
            dm.retrieve_history,
        )
        self.send = to_streamed_response_wrapper(
            dm.send,
        )


class AsyncDmResourceWithStreamingResponse:
    def __init__(self, dm: AsyncDmResource) -> None:
        self._dm = dm

        self.delete_message = async_to_streamed_response_wrapper(
            dm.delete_message,
        )
        self.retrieve_history = async_to_streamed_response_wrapper(
            dm.retrieve_history,
        )
        self.send = async_to_streamed_response_wrapper(
            dm.send,
        )
