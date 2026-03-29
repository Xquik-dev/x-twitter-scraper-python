# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ...types.x import profile_patch_all_params, profile_update_avatar_params, profile_update_banner_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.profile_patch_all_response import ProfilePatchAllResponse
from ...types.x.profile_update_avatar_response import ProfileUpdateAvatarResponse
from ...types.x.profile_update_banner_response import ProfileUpdateBannerResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def patch_all(
        self,
        *,
        account: str,
        description: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePatchAllResponse:
        """
        Update X profile

        Args:
          account: X account (@username or account ID)

          description: Bio description

          name: Display name

          url: Website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                profile_patch_all_params.ProfilePatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePatchAllResponse,
        )

    def update_avatar(
        self,
        *,
        account: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateAvatarResponse:
        """
        Update profile avatar

        Args:
          account: X account (@username or account ID)

          file: Avatar image (max 716KB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
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
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateBannerResponse:
        """
        Update profile banner

        Args:
          account: X account (@username or account ID)

          file: Banner image (max 2MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
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
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def patch_all(
        self,
        *,
        account: str,
        description: str | Omit = omit,
        location: str | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePatchAllResponse:
        """
        Update X profile

        Args:
          account: X account (@username or account ID)

          description: Bio description

          name: Display name

          url: Website URL

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
                profile_patch_all_params.ProfilePatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePatchAllResponse,
        )

    async def update_avatar(
        self,
        *,
        account: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateAvatarResponse:
        """
        Update profile avatar

        Args:
          account: X account (@username or account ID)

          file: Avatar image (max 716KB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
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
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateBannerResponse:
        """
        Update profile banner

        Args:
          account: X account (@username or account ID)

          file: Banner image (max 2MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
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

        self.patch_all = to_raw_response_wrapper(
            profile.patch_all,
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

        self.patch_all = async_to_raw_response_wrapper(
            profile.patch_all,
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

        self.patch_all = to_streamed_response_wrapper(
            profile.patch_all,
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

        self.patch_all = async_to_streamed_response_wrapper(
            profile.patch_all,
        )
        self.update_avatar = async_to_streamed_response_wrapper(
            profile.update_avatar,
        )
        self.update_banner = async_to_streamed_response_wrapper(
            profile.update_banner,
        )
