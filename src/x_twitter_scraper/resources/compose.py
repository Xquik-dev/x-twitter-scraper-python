# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import compose_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.compose_create_response import ComposeCreateResponse

__all__ = ["ComposeResource", "AsyncComposeResource"]


class ComposeResource(SyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> ComposeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ComposeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComposeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return ComposeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        step: Literal["compose", "refine", "score"],
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        draft: str | Omit = omit,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        style_username: str | Omit = omit,
        tone: str | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """
        Compose, refine, or score a tweet

        Args:
          step: Workflow step

          additional_context: Extra context or URLs (refine)

          call_to_action: Desired call to action (refine)

          draft: Tweet draft text to evaluate (score)

          goal: Optimization goal

          has_link: Whether a link is attached (score)

          has_media: Whether media is attached (score)

          media_type: Media type (refine)

          style_username: Cached style username for voice matching (compose)

          tone: Desired tone (refine)

          topic: Tweet topic (compose, refine)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/compose",
            body=maybe_transform(
                {
                    "step": step,
                    "additional_context": additional_context,
                    "call_to_action": call_to_action,
                    "draft": draft,
                    "goal": goal,
                    "has_link": has_link,
                    "has_media": has_media,
                    "media_type": media_type,
                    "style_username": style_username,
                    "tone": tone,
                    "topic": topic,
                },
                compose_create_params.ComposeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComposeCreateResponse,
        )


class AsyncComposeResource(AsyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> AsyncComposeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComposeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComposeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncComposeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        step: Literal["compose", "refine", "score"],
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        draft: str | Omit = omit,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        style_username: str | Omit = omit,
        tone: str | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """
        Compose, refine, or score a tweet

        Args:
          step: Workflow step

          additional_context: Extra context or URLs (refine)

          call_to_action: Desired call to action (refine)

          draft: Tweet draft text to evaluate (score)

          goal: Optimization goal

          has_link: Whether a link is attached (score)

          has_media: Whether media is attached (score)

          media_type: Media type (refine)

          style_username: Cached style username for voice matching (compose)

          tone: Desired tone (refine)

          topic: Tweet topic (compose, refine)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/compose",
            body=await async_maybe_transform(
                {
                    "step": step,
                    "additional_context": additional_context,
                    "call_to_action": call_to_action,
                    "draft": draft,
                    "goal": goal,
                    "has_link": has_link,
                    "has_media": has_media,
                    "media_type": media_type,
                    "style_username": style_username,
                    "tone": tone,
                    "topic": topic,
                },
                compose_create_params.ComposeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComposeCreateResponse,
        )


class ComposeResourceWithRawResponse:
    def __init__(self, compose: ComposeResource) -> None:
        self._compose = compose

        self.create = to_raw_response_wrapper(
            compose.create,
        )


class AsyncComposeResourceWithRawResponse:
    def __init__(self, compose: AsyncComposeResource) -> None:
        self._compose = compose

        self.create = async_to_raw_response_wrapper(
            compose.create,
        )


class ComposeResourceWithStreamingResponse:
    def __init__(self, compose: ComposeResource) -> None:
        self._compose = compose

        self.create = to_streamed_response_wrapper(
            compose.create,
        )


class AsyncComposeResourceWithStreamingResponse:
    def __init__(self, compose: AsyncComposeResource) -> None:
        self._compose = compose

        self.create = async_to_streamed_response_wrapper(
            compose.create,
        )
