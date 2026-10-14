# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import extract_files, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import profile_update_params, profile_update_avatar_params, profile_update_banner_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.profile_update_response import ProfileUpdateResponse
from ...types.x.profile_update_avatar_response import ProfileUpdateAvatarResponse
from ...types.x.profile_update_banner_response import ProfileUpdateBannerResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account: str,
        idempotency_key: str,
        description: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Updates editable fields on a connected X profile.

        Args:
          account: X account (@username or ID) to update profile

          description: Bio, up to 160 characters. An emoji counts as 2.

          location: Location, up to 30 characters. An emoji counts as 2.

          name: Display name, 1 to 50 characters. An emoji counts as 2.

          url: Website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._patch(
            "/x/profile",
            body=maybe_transform(
                {
                    "account": account,
                    "description": description,
                    "location": location,
                    "name": name,
                    "url": url,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    def update_avatar(
        self,
        *,
        account: str,
        url: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateAvatarResponse:
        """
        Replaces the avatar on a connected X profile.

        Args:
          account: X account (@username or ID) receiving avatar from URL

          url: HTTPS URL to the avatar image to download

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
        return self._patch(
            "/x/profile/avatar",
            body=maybe_transform(body, profile_update_avatar_params.ProfileUpdateAvatarParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateAvatarResponse,
        )

    def update_banner(
        self,
        *,
        account: str,
        url: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateBannerResponse:
        """
        Replaces the banner on a connected X profile.

        Args:
          account: X account (@username or ID) receiving banner from URL

          url: HTTPS URL to the banner image to download

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
        return self._patch(
            "/x/profile/banner",
            body=maybe_transform(body, profile_update_banner_params.ProfileUpdateBannerParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateBannerResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account: str,
        idempotency_key: str,
        description: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Updates editable fields on a connected X profile.

        Args:
          account: X account (@username or ID) to update profile

          description: Bio, up to 160 characters. An emoji counts as 2.

          location: Location, up to 30 characters. An emoji counts as 2.

          name: Display name, 1 to 50 characters. An emoji counts as 2.

          url: Website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._patch(
            "/x/profile",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "description": description,
                    "location": location,
                    "name": name,
                    "url": url,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    async def update_avatar(
        self,
        *,
        account: str,
        url: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateAvatarResponse:
        """
        Replaces the avatar on a connected X profile.

        Args:
          account: X account (@username or ID) receiving avatar from URL

          url: HTTPS URL to the avatar image to download

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
        return await self._patch(
            "/x/profile/avatar",
            body=await async_maybe_transform(body, profile_update_avatar_params.ProfileUpdateAvatarParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateAvatarResponse,
        )

    async def update_banner(
        self,
        *,
        account: str,
        url: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateBannerResponse:
        """
        Replaces the banner on a connected X profile.

        Args:
          account: X account (@username or ID) receiving banner from URL

          url: HTTPS URL to the banner image to download

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
        return await self._patch(
            "/x/profile/banner",
            body=await async_maybe_transform(body, profile_update_banner_params.ProfileUpdateBannerParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateBannerResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.update = to_raw_response_wrapper(
            profile.update,
        )
        self.update_avatar = to_raw_response_wrapper(
            profile.update_avatar,
        )
        self.update_banner = to_raw_response_wrapper(
            profile.update_banner,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.update = async_to_raw_response_wrapper(
            profile.update,
        )
        self.update_avatar = async_to_raw_response_wrapper(
            profile.update_avatar,
        )
        self.update_banner = async_to_raw_response_wrapper(
            profile.update_banner,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.update = to_streamed_response_wrapper(
            profile.update,
        )
        self.update_avatar = to_streamed_response_wrapper(
            profile.update_avatar,
        )
        self.update_banner = to_streamed_response_wrapper(
            profile.update_banner,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )
        self.update_avatar = async_to_streamed_response_wrapper(
            profile.update_avatar,
        )
        self.update_banner = async_to_streamed_response_wrapper(
            profile.update_banner,
        )
