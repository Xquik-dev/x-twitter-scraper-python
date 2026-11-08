# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from ..._utils import extract_files, required_args, maybe_transform, strip_not_given, async_maybe_transform
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
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
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
        image_shows: str | Omit = omit,
        tweet_id: str | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        tweet_input: str | Omit = omit,
        tweet_url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaDownloadResponse:
        """
        Downloads images and videos attached to selected tweets.

        Args:
          image_shows: Save only posts whose photos show this. Send charts, screenshots,
              product_photos, memes or people, or describe it in words, such as a rocket. AI-powered
              analysis checks posts with photos X doesn't mark sensitive & keeps scores of 0.5 or
              more. Each post saved costs 2 credits, the AI analysis price, on top of its save
              price, & a post the filter drops costs nothing. imageFilter states the cutoff &
              counts.

          tweet_id: Numeric tweet ID alias for tweetInput

          tweet_ids: Tweet URLs or IDs. An item that names no post gets 400 `invalid_tweet_id`, which
              says which item. Posts Xquik had no time to read come back in
              `unprocessedTweetIds`, with no charge. Send them again.

          tweet_input: Tweet URL or ID (single tweet)

          tweet_url: Tweet URL alias for tweetInput

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/media/download",
            body=maybe_transform(
                {
                    "image_shows": image_shows,
                    "tweet_id": tweet_id,
                    "tweet_ids": tweet_ids,
                    "tweet_input": tweet_input,
                    "tweet_url": tweet_url,
                },
                media_download_params.MediaDownloadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDownloadResponse,
        )

    @required_args(["account", "idempotency_key", "url"], ["account", "file", "idempotency_key"])
    def upload(
        self,
        *,
        account: str,
        idempotency_key: str,
        file: FileTypes | Omit = omit,
        is_long_video: bool | Omit = omit,
        url: str | Omit = omit,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        Uploads media and returns an identifier for later writes.

        Args:
          account: X account (@username or ID) uploading media

          file: Media file to upload, up to 15 MB. A larger file gets 413 `media_too_large`
              before any account lookup. Send file or url.

          is_long_video: Set true only for video/mp4 multipart uploads longer than 140 seconds.

          url: HTTPS URL to download and upload as media, up to 15 MB. Another scheme gets 400
              `invalid_media_url`. Send url or file.

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
                "file": file,
                "is_long_video": is_long_video,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
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
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
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
        image_shows: str | Omit = omit,
        tweet_id: str | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        tweet_input: str | Omit = omit,
        tweet_url: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaDownloadResponse:
        """
        Downloads images and videos attached to selected tweets.

        Args:
          image_shows: Save only posts whose photos show this. Send charts, screenshots,
              product_photos, memes or people, or describe it in words, such as a rocket. AI-powered
              analysis checks posts with photos X doesn't mark sensitive & keeps scores of 0.5 or
              more. Each post saved costs 2 credits, the AI analysis price, on top of its save
              price, & a post the filter drops costs nothing. imageFilter states the cutoff &
              counts.

          tweet_id: Numeric tweet ID alias for tweetInput

          tweet_ids: Tweet URLs or IDs. An item that names no post gets 400 `invalid_tweet_id`, which
              says which item. Posts Xquik had no time to read come back in
              `unprocessedTweetIds`, with no charge. Send them again.

          tweet_input: Tweet URL or ID (single tweet)

          tweet_url: Tweet URL alias for tweetInput

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/media/download",
            body=await async_maybe_transform(
                {
                    "image_shows": image_shows,
                    "tweet_id": tweet_id,
                    "tweet_ids": tweet_ids,
                    "tweet_input": tweet_input,
                    "tweet_url": tweet_url,
                },
                media_download_params.MediaDownloadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaDownloadResponse,
        )

    @required_args(["account", "idempotency_key", "url"], ["account", "file", "idempotency_key"])
    async def upload(
        self,
        *,
        account: str,
        idempotency_key: str,
        file: FileTypes | Omit = omit,
        is_long_video: bool | Omit = omit,
        url: str | Omit = omit,
        prefer: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        Uploads media and returns an identifier for later writes.

        Args:
          account: X account (@username or ID) uploading media

          file: Media file to upload, up to 15 MB. A larger file gets 413 `media_too_large`
              before any account lookup. Send file or url.

          is_long_video: Set true only for video/mp4 multipart uploads longer than 140 seconds.

          url: HTTPS URL to download and upload as media, up to 15 MB. Another scheme gets 400
              `invalid_media_url`. Send url or file.

          prefer: A long write answers 202 with a status link, then lands on X. `wait=<seconds>`
              asks for the answer within that many seconds, up to 85. If the write is still
              running then, the API answers 202 with Location. Poll Location until `terminal`
              is true, and don't send the write again.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            "Idempotency-Key": idempotency_key,
            **strip_not_given({"Prefer": prefer}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        body = deepcopy_with_paths(
            {
                "account": account,
                "url": url,
                "file": file,
                "is_long_video": is_long_video,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            extra_headers["Content-Type"] = "multipart/form-data"
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
