# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import (
    analysis_news_params,
    analysis_brand_params,
    analysis_classify_params,
    analysis_sentiment_params,
    analysis_viral_score_params,
    analysis_market_signals_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.analysis_news_response import AnalysisNewsResponse
from ...types.x.analysis_brand_response import AnalysisBrandResponse
from ...types.x.analysis_classify_response import AnalysisClassifyResponse
from ...types.x.analysis_sentiment_response import AnalysisSentimentResponse
from ...types.x.analysis_viral_score_response import AnalysisViralScoreResponse
from ...types.x.analysis_market_signals_response import AnalysisMarketSignalsResponse

__all__ = ["AnalysisResource", "AsyncAnalysisResource"]


class AnalysisResource(SyncAPIResource):
    """AI analysis of posts, at 2 credits per analyzed post"""

    @cached_property
    def with_raw_response(self) -> AnalysisResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AnalysisResourceWithStreamingResponse(self)

    def brand(
        self,
        *,
        analysis: analysis_brand_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_brand_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisBrandResponse:
        """
        Answers whether each post is about your brand, the author's attitude toward it &
        the author's relationship with it. Name the brand in analysis.targets. Each
        analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/brand",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_brand_params.AnalysisBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisBrandResponse,
        )

    def classify(
        self,
        *,
        analysis: analysis_classify_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_classify_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisClassifyResponse:
        """Answers 1 to 8 questions you write in analysis.questions.

        A choice picks a
        category, such as a topic. A score picks a level. A probability answers yes or
        no. Without questions it answers the sentiment questions. Each analyzed post
        costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/classify",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_classify_params.AnalysisClassifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisClassifyResponse,
        )

    def market_signals(
        self,
        *,
        analysis: analysis_market_signals_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_market_signals_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisMarketSignalsResponse:
        """
        Answers each post's stance on an asset, its content type, its conviction & its
        relevance. The summary counts bullish & bearish posts per cashtag. Name the
        asset in analysis.targets. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/market-signals",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_market_signals_params.AnalysisMarketSignalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisMarketSignalsResponse,
        )

    def news(
        self,
        *,
        analysis: analysis_news_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_news_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisNewsResponse:
        """
        Answers each post's format, such as reporting, commentary or speculation, its
        source attribution & its relevance to your topic. Name the topic in
        analysis.targets. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/news",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_news_params.AnalysisNewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisNewsResponse,
        )

    def sentiment(
        self,
        *,
        analysis: analysis_sentiment_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_sentiment_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisSentimentResponse:
        """Answers each post's attitude, its intensity & its sarcasm probability.

        Send post
        IDs, an X search, an account, a List, a post's replies or quotes, or your own
        texts. Each analyzed post costs 2 credits. A post without an analysis costs
        nothing.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/sentiment",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_sentiment_params.AnalysisSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisSentimentResponse,
        )

    def viral_score(
        self,
        *,
        analysis: analysis_viral_score_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_viral_score_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisViralScoreResponse:
        """
        Answers each post's hook, clarity, payoff, humor, spam risk & likely reaction, &
        adds a Viral Score from 0 to 100 with a verdict. The score rates the wording. It
        does not predict likes or views. Send drafts in texts to score them before
        posting. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/analysis/viral-score",
            body=maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_viral_score_params.AnalysisViralScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisViralScoreResponse,
        )


class AsyncAnalysisResource(AsyncAPIResource):
    """AI analysis of posts, at 2 credits per analyzed post"""

    @cached_property
    def with_raw_response(self) -> AsyncAnalysisResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalysisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncAnalysisResourceWithStreamingResponse(self)

    async def brand(
        self,
        *,
        analysis: analysis_brand_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_brand_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisBrandResponse:
        """
        Answers whether each post is about your brand, the author's attitude toward it &
        the author's relationship with it. Name the brand in analysis.targets. Each
        analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/brand",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_brand_params.AnalysisBrandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisBrandResponse,
        )

    async def classify(
        self,
        *,
        analysis: analysis_classify_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_classify_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisClassifyResponse:
        """Answers 1 to 8 questions you write in analysis.questions.

        A choice picks a
        category, such as a topic. A score picks a level. A probability answers yes or
        no. Without questions it answers the sentiment questions. Each analyzed post
        costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/classify",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_classify_params.AnalysisClassifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisClassifyResponse,
        )

    async def market_signals(
        self,
        *,
        analysis: analysis_market_signals_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_market_signals_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisMarketSignalsResponse:
        """
        Answers each post's stance on an asset, its content type, its conviction & its
        relevance. The summary counts bullish & bearish posts per cashtag. Name the
        asset in analysis.targets. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/market-signals",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_market_signals_params.AnalysisMarketSignalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisMarketSignalsResponse,
        )

    async def news(
        self,
        *,
        analysis: analysis_news_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_news_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisNewsResponse:
        """
        Answers each post's format, such as reporting, commentary or speculation, its
        source attribution & its relevance to your topic. Name the topic in
        analysis.targets. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/news",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_news_params.AnalysisNewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisNewsResponse,
        )

    async def sentiment(
        self,
        *,
        analysis: analysis_sentiment_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_sentiment_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisSentimentResponse:
        """Answers each post's attitude, its intensity & its sarcasm probability.

        Send post
        IDs, an X search, an account, a List, a post's replies or quotes, or your own
        texts. Each analyzed post costs 2 credits. A post without an analysis costs
        nothing.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/sentiment",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_sentiment_params.AnalysisSentimentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisSentimentResponse,
        )

    async def viral_score(
        self,
        *,
        analysis: analysis_viral_score_params.Analysis | Omit = omit,
        baseline: Iterable[analysis_viral_score_params.Baseline] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        query: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes_of: str | Omit = omit,
        replies_to: str | Omit = omit,
        since_time: Union[str, int] | Omit = omit,
        texts: SequenceNotStr[str] | Omit = omit,
        tweet_ids: SequenceNotStr[str] | Omit = omit,
        until_time: Union[str, int] | Omit = omit,
        username: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalysisViralScoreResponse:
        """
        Answers each post's hook, clarity, payoff, humor, spam risk & likely reaction, &
        adds a Viral Score from 0 to 100 with a verdict. The score rates the wording. It
        does not predict likes or views. Send drafts in texts to score them before
        posting. Each analyzed post costs 2 credits.

        Args:
          analysis: Analysis settings, the same as the analysis input of Xquik's AI Actors. Leave it
              out for the route's own questions.

          baseline: Rows of an earlier answer to compare with, such as its results. Each needs the
              post's id, or tweet.id, & its answers. Send monitor too, so other settings show
              as not_comparable. Each result's monitor says whether the post is new, changed
              or unchanged. The comparison costs nothing extra.

          cursor: The next_cursor of the page before. Send the same search with it.

          limit: Maximum posts to analyze from the search. Credits can return fewer.

          list_id: Analyze a public List's posts. Send its ID or URL.

          query: X search to analyze, with the operators of /x/tweets/search, such as from:nasa
              or lang:en. X searches up to 512 characters, counted with the other search
              fields, as /x/tweets/search counts q.

          query_type: Search order. Default Latest.

          quotes_of: Analyze the quotes of 1 post. Send its ID or URL.

          replies_to: Analyze the replies in 1 post's conversation. Send its ID or URL.

          since_time: Inclusive start of the search, such as 2026-09-25T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          texts: Your own texts to analyze, such as drafts. Reads nothing from X. Each text costs
              the same as 1 analyzed post.

          tweet_ids: Post IDs or post URLs to analyze, up to 100.

          until_time: Exclusive end of the search, such as 2026-09-26T00:00:00Z. Unix seconds also
              work. A time without an offset is UTC.

          username: Analyze 1 account's posts. Send a handle, with or without @, or a profile URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/analysis/viral-score",
            body=await async_maybe_transform(
                {
                    "analysis": analysis,
                    "baseline": baseline,
                    "cursor": cursor,
                    "limit": limit,
                    "list_id": list_id,
                    "query": query,
                    "query_type": query_type,
                    "quotes_of": quotes_of,
                    "replies_to": replies_to,
                    "since_time": since_time,
                    "texts": texts,
                    "tweet_ids": tweet_ids,
                    "until_time": until_time,
                    "username": username,
                },
                analysis_viral_score_params.AnalysisViralScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnalysisViralScoreResponse,
        )


class AnalysisResourceWithRawResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.brand = to_raw_response_wrapper(
            analysis.brand,
        )
        self.classify = to_raw_response_wrapper(
            analysis.classify,
        )
        self.market_signals = to_raw_response_wrapper(
            analysis.market_signals,
        )
        self.news = to_raw_response_wrapper(
            analysis.news,
        )
        self.sentiment = to_raw_response_wrapper(
            analysis.sentiment,
        )
        self.viral_score = to_raw_response_wrapper(
            analysis.viral_score,
        )


class AsyncAnalysisResourceWithRawResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.brand = async_to_raw_response_wrapper(
            analysis.brand,
        )
        self.classify = async_to_raw_response_wrapper(
            analysis.classify,
        )
        self.market_signals = async_to_raw_response_wrapper(
            analysis.market_signals,
        )
        self.news = async_to_raw_response_wrapper(
            analysis.news,
        )
        self.sentiment = async_to_raw_response_wrapper(
            analysis.sentiment,
        )
        self.viral_score = async_to_raw_response_wrapper(
            analysis.viral_score,
        )


class AnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AnalysisResource) -> None:
        self._analysis = analysis

        self.brand = to_streamed_response_wrapper(
            analysis.brand,
        )
        self.classify = to_streamed_response_wrapper(
            analysis.classify,
        )
        self.market_signals = to_streamed_response_wrapper(
            analysis.market_signals,
        )
        self.news = to_streamed_response_wrapper(
            analysis.news,
        )
        self.sentiment = to_streamed_response_wrapper(
            analysis.sentiment,
        )
        self.viral_score = to_streamed_response_wrapper(
            analysis.viral_score,
        )


class AsyncAnalysisResourceWithStreamingResponse:
    def __init__(self, analysis: AsyncAnalysisResource) -> None:
        self._analysis = analysis

        self.brand = async_to_streamed_response_wrapper(
            analysis.brand,
        )
        self.classify = async_to_streamed_response_wrapper(
            analysis.classify,
        )
        self.market_signals = async_to_streamed_response_wrapper(
            analysis.market_signals,
        )
        self.news = async_to_streamed_response_wrapper(
            analysis.news,
        )
        self.sentiment = async_to_streamed_response_wrapper(
            analysis.sentiment,
        )
        self.viral_score = async_to_streamed_response_wrapper(
            analysis.viral_score,
        )
