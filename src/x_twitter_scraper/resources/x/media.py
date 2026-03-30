# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ...types.x import media_upload_params, media_download_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.media_upload_response import MediaUploadResponse
from ...types.x.media_download_response import MediaDownloadResponse

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    """Media upload & download"""

    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def download(
        self,
        *,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        tweet_input: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaDownloadResponse:
        """
        Download tweet media

        Args:
          tweet_ids: Array of tweet URLs or IDs (bulk, max 50)

          tweet_input: Tweet URL or ID (single tweet)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/media/download",
            body=maybe_transform(
                {
                    "tweet_ids": tweet_ids,
                    "tweet_input": tweet_input,
                },
                media_download_params.MediaDownloadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDownloadResponse,
        )

    def upload(
        self,
        *,
        account: str,
        file: FileTypes,
        is_long_video: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        Upload media

        Args:
          account: X account (@username or account ID)

          file: Media file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
                "is_long_video": is_long_video,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/x/media",
            body=maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class AsyncMediaResource(AsyncAPIResource):
    """Media upload & download"""

    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def download(
        self,
        *,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        tweet_input: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaDownloadResponse:
        """
        Download tweet media

        Args:
          tweet_ids: Array of tweet URLs or IDs (bulk, max 50)

          tweet_input: Tweet URL or ID (single tweet)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/media/download",
            body=await async_maybe_transform(
                {
                    "tweet_ids": tweet_ids,
                    "tweet_input": tweet_input,
                },
                media_download_params.MediaDownloadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDownloadResponse,
        )

    async def upload(
        self,
        *,
        account: str,
        file: FileTypes,
        is_long_video: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        Upload media

        Args:
          account: X account (@username or account ID)

          file: Media file to upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "account": account,
                "file": file,
                "is_long_video": is_long_video,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/x/media",
            body=await async_maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.download = to_raw_response_wrapper(
            media.download,
        )
        self.upload = to_raw_response_wrapper(
            media.upload,
        )


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.download = async_to_raw_response_wrapper(
            media.download,
        )
        self.upload = async_to_raw_response_wrapper(
            media.upload,
        )


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.download = to_streamed_response_wrapper(
            media.download,
        )
        self.upload = to_streamed_response_wrapper(
            media.upload,
        )


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.download = async_to_streamed_response_wrapper(
            media.download,
        )
        self.upload = async_to_streamed_response_wrapper(
            media.upload,
        )
