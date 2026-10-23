# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import (
    sport_list_games_params,
    sport_retrieve_plays_params,
    sport_retrieve_box_score_params,
    sport_retrieve_scoreboard_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.football import FootballPlays, FootballBoxScore, FootballSchedule, FootballScoreboard

__all__ = ["SportsResource", "AsyncSportsResource"]


class SportsResource(SyncAPIResource):
    """NFL & college football games, scoreboards, box scores & play-by-play"""

    @cached_property
    def with_raw_response(self) -> SportsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return SportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return SportsResourceWithStreamingResponse(self)

    def list_games(
        self,
        league: str,
        *,
        fields: str | Omit = omit,
        from_: str | Omit = omit,
        omit: str | Omit = omit,
        team: str | Omit = omit,
        to: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballSchedule:
        """
        Lists NFL or college football games in a time window, with teams & scores. Use
        it to find game IDs & team IDs. Without from or to, X picks about 5 weeks around
        today. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          from_: Start of the window. Takes an ISO 8601 date or time, such as 2026-10-01,
              or Unix seconds. A time without a zone reads as UTC. Defaults to 7 days
              before to. Alias sinceTime.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          team: Keeps only 1 team's games, by team ID. Each game lists its teamIds.
              Aliases teamId & team_id.

          to: End of the window. Takes the forms of from. Defaults to 7 days after from.
              Alias untilTime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return self._get(
            path_template("/x/sports/{league}/games", league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "from_": from_,
                        "omit": omit,
                        "team": team,
                        "to": to,
                    },
                    sport_list_games_params.SportListGamesParams,
                ),
            ),
            cast_to=FootballSchedule,
        )

    def retrieve_scoreboard(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballScoreboard:
        """
        Returns 1 game's scoreboard. It has the teams, the score by period, the status &
        clock, down & distance, the venue & the latest play. Each request costs 1
        credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return self._get(
            path_template("/x/sports/{league}/games/{id}", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_scoreboard_params.SportRetrieveScoreboardParams,
                ),
            ),
            cast_to=FootballScoreboard,
        )

    def retrieve_box_score(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballBoxScore:
        """
        Returns each team's totals & each player's stats for 1 game. Stats cover
        passing, rushing, receiving, defense, kicking & returns. A game that has not
        started has no stats yet. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return self._get(
            path_template("/x/sports/{league}/games/{id}/box-score", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_box_score_params.SportRetrieveBoxScoreParams,
                ),
            ),
            cast_to=FootballBoxScore,
        )

    def retrieve_plays(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballPlays:
        """
        Returns every drive & play of 1 game, by quarter. Each play has its clock, down
        & distance, details, penalties & linked posts. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return self._get(
            path_template("/x/sports/{league}/games/{id}/plays", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_plays_params.SportRetrievePlaysParams,
                ),
            ),
            cast_to=FootballPlays,
        )


class AsyncSportsResource(AsyncAPIResource):
    """NFL & college football games, scoreboards, box scores & play-by-play"""

    @cached_property
    def with_raw_response(self) -> AsyncSportsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncSportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncSportsResourceWithStreamingResponse(self)

    async def list_games(
        self,
        league: str,
        *,
        fields: str | Omit = omit,
        from_: str | Omit = omit,
        omit: str | Omit = omit,
        team: str | Omit = omit,
        to: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballSchedule:
        """
        Lists NFL or college football games in a time window, with teams & scores. Use
        it to find game IDs & team IDs. Without from or to, X picks about 5 weeks around
        today. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          from_: Start of the window. Takes an ISO 8601 date or time, such as 2026-10-01,
              or Unix seconds. A time without a zone reads as UTC. Defaults to 7 days
              before to. Alias sinceTime.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          team: Keeps only 1 team's games, by team ID. Each game lists its teamIds.
              Aliases teamId & team_id.

          to: End of the window. Takes the forms of from. Defaults to 7 days after from.
              Alias untilTime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return await self._get(
            path_template("/x/sports/{league}/games", league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "from_": from_,
                        "omit": omit,
                        "team": team,
                        "to": to,
                    },
                    sport_list_games_params.SportListGamesParams,
                ),
            ),
            cast_to=FootballSchedule,
        )

    async def retrieve_scoreboard(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballScoreboard:
        """
        Returns 1 game's scoreboard. It has the teams, the score by period, the status &
        clock, down & distance, the venue & the latest play. Each request costs 1
        credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return await self._get(
            path_template("/x/sports/{league}/games/{id}", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_scoreboard_params.SportRetrieveScoreboardParams,
                ),
            ),
            cast_to=FootballScoreboard,
        )

    async def retrieve_box_score(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballBoxScore:
        """
        Returns each team's totals & each player's stats for 1 game. Stats cover
        passing, rushing, receiving, defense, kicking & returns. A game that has not
        started has no stats yet. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return await self._get(
            path_template("/x/sports/{league}/games/{id}/box-score", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_box_score_params.SportRetrieveBoxScoreParams,
                ),
            ),
            cast_to=FootballBoxScore,
        )

    async def retrieve_plays(
        self,
        id: str,
        *,
        league: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FootballPlays:
        """
        Returns every drive & play of 1 game, by quarter. Each play has its clock, down
        & distance, details, penalties & linked posts. Each request costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields,
              such as author.username. A list keeps the field in each item. Case &
              underscores do not matter. A row that lacks a field leaves it out.
              Cursors, counts & diagnostics always stay. An unknown name answers 400
              unknown_field with the valid names, before any read. The price stays the
              same. SDK row types then hold only the named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not league:
            raise ValueError(f"Expected a non-empty value for `league` but received {league!r}")
        return await self._get(
            path_template("/x/sports/{league}/games/{id}/plays", id=id, league=league),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    sport_retrieve_plays_params.SportRetrievePlaysParams,
                ),
            ),
            cast_to=FootballPlays,
        )


class SportsResourceWithRawResponse:
    def __init__(self, sports: SportsResource) -> None:
        self._sports = sports

        self.list_games = to_raw_response_wrapper(
            sports.list_games,
        )
        self.retrieve_scoreboard = to_raw_response_wrapper(
            sports.retrieve_scoreboard,
        )
        self.retrieve_box_score = to_raw_response_wrapper(
            sports.retrieve_box_score,
        )
        self.retrieve_plays = to_raw_response_wrapper(
            sports.retrieve_plays,
        )


class AsyncSportsResourceWithRawResponse:
    def __init__(self, sports: AsyncSportsResource) -> None:
        self._sports = sports

        self.list_games = async_to_raw_response_wrapper(
            sports.list_games,
        )
        self.retrieve_scoreboard = async_to_raw_response_wrapper(
            sports.retrieve_scoreboard,
        )
        self.retrieve_box_score = async_to_raw_response_wrapper(
            sports.retrieve_box_score,
        )
        self.retrieve_plays = async_to_raw_response_wrapper(
            sports.retrieve_plays,
        )


class SportsResourceWithStreamingResponse:
    def __init__(self, sports: SportsResource) -> None:
        self._sports = sports

        self.list_games = to_streamed_response_wrapper(
            sports.list_games,
        )
        self.retrieve_scoreboard = to_streamed_response_wrapper(
            sports.retrieve_scoreboard,
        )
        self.retrieve_box_score = to_streamed_response_wrapper(
            sports.retrieve_box_score,
        )
        self.retrieve_plays = to_streamed_response_wrapper(
            sports.retrieve_plays,
        )


class AsyncSportsResourceWithStreamingResponse:
    def __init__(self, sports: AsyncSportsResource) -> None:
        self._sports = sports

        self.list_games = async_to_streamed_response_wrapper(
            sports.list_games,
        )
        self.retrieve_scoreboard = async_to_streamed_response_wrapper(
            sports.retrieve_scoreboard,
        )
        self.retrieve_box_score = async_to_streamed_response_wrapper(
            sports.retrieve_box_score,
        )
        self.retrieve_plays = async_to_streamed_response_wrapper(
            sports.retrieve_plays,
        )
