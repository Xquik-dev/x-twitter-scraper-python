# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ..types import compose_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ComposeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComposeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return ComposeResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        step: Literal["compose"],
        topic: str,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        style_username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          topic: Subject for the post.

          goal: Editorial goal used to order the rules and questions.

          style_username: Username from a style analysis saved to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        goal: Literal["engagement", "followers", "authority", "conversation"],
        step: Literal["refine"],
        tone: str,
        topic: str,
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          goal: Editorial goal for the guidance.

          tone: Requested writing tone.

          topic: Subject for the post.

          additional_context: Audience, constraints, sources, or other writing context.

          call_to_action: Specific action the draft should request.

          media_type: Planned media type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        draft: str,
        step: Literal["score"],
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          draft: Full post text for deterministic editorial checks.

          has_link: True when a separate link card is attached.

          has_media: Accepted for backward compatibility. Text checks ignore this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["step", "topic"], ["goal", "step", "tone", "topic"], ["draft", "step"])
    def create(
        self,
        *,
        step: Literal["compose"] | Literal["refine"] | Literal["score"],
        topic: str | Omit = omit,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        style_username: str | Omit = omit,
        tone: str | Omit = omit,
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        draft: str | Omit = omit,
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        return cast(
            ComposeCreateResponse,
            self._post(
                "/compose",
                body=maybe_transform(
                    {
                        "step": step,
                        "topic": topic,
                        "goal": goal,
                        "style_username": style_username,
                        "tone": tone,
                        "additional_context": additional_context,
                        "call_to_action": call_to_action,
                        "media_type": media_type,
                        "draft": draft,
                        "has_link": has_link,
                        "has_media": has_media,
                    },
                    compose_create_params.ComposeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ComposeCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncComposeResource(AsyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> AsyncComposeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComposeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComposeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncComposeResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        step: Literal["compose"],
        topic: str,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        style_username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          topic: Subject for the post.

          goal: Editorial goal used to order the rules and questions.

          style_username: Username from a style analysis saved to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        goal: Literal["engagement", "followers", "authority", "conversation"],
        step: Literal["refine"],
        tone: str,
        topic: str,
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          goal: Editorial goal for the guidance.

          tone: Requested writing tone.

          topic: Subject for the post.

          additional_context: Audience, constraints, sources, or other writing context.

          call_to_action: Specific action the draft should request.

          media_type: Planned media type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        draft: str,
        step: Literal["score"],
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        """Run one step of Xquik's three-step writing workflow.

        Compose returns questions
        and editorial rules. Refine returns goal-specific guidance. Score applies
        deterministic text checks. It does not predict reach or expose X ranking
        weights.

        Args:
          draft: Full post text for deterministic editorial checks.

          has_link: True when a separate link card is attached.

          has_media: Accepted for backward compatibility. Text checks ignore this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["step", "topic"], ["goal", "step", "tone", "topic"], ["draft", "step"])
    async def create(
        self,
        *,
        step: Literal["compose"] | Literal["refine"] | Literal["score"],
        topic: str | Omit = omit,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        style_username: str | Omit = omit,
        tone: str | Omit = omit,
        additional_context: str | Omit = omit,
        call_to_action: str | Omit = omit,
        media_type: Literal["photo", "video", "none"] | Omit = omit,
        draft: str | Omit = omit,
        has_link: bool | Omit = omit,
        has_media: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ComposeCreateResponse:
        return cast(
            ComposeCreateResponse,
            await self._post(
                "/compose",
                body=await async_maybe_transform(
                    {
                        "step": step,
                        "topic": topic,
                        "goal": goal,
                        "style_username": style_username,
                        "tone": tone,
                        "additional_context": additional_context,
                        "call_to_action": call_to_action,
                        "media_type": media_type,
                        "draft": draft,
                        "has_link": has_link,
                        "has_media": has_media,
                    },
                    compose_create_params.ComposeCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ComposeCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
