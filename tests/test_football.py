# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    FootballPlays,
    FootballBoxScore,
    FootballSchedule,
    FootballScoreboard,
    SportsGameAudience,
)

SCHEDULE = {
    "league": "nfl",
    "games": [
        {
            "id": "2055084502741811200",
            "seasonType": "RegularSeason",
            "week": 6,
            "startsAt": "2026-10-20T00:15:00.000Z",
            "status": "Closed",
            "clock": "00:00:00",
            "quarter": 4,
            "home": {"teamId": "689566294702555136", "points": 23},
            "away": {"teamId": "689566294702555136", "points": 23},
            "teamIds": ["689566294702555136", "689566304366292992"],
            "periods": [{"type": "Quarter"}],
            "odds": {
                "home": {"moneyLine": "text", "spread": "text", "total": "text"},
                "away": {"moneyLine": "text", "spread": "text", "total": "text"},
            },
        }
    ],
    "teams": {
        "689566294702555136": {
            "id": "689566294702555136",
            "name": "San Francisco 49ers",
            "shortName": "49ers",
            "abbreviation": "SF",
            "alternateId": "f0e724b0-4cbf-495a-be47-013907608da9",
            "location": "Virginia Tech",
            "colors": [{"r": 170, "g": 0, "b": 0}],
            "logos": {
                "default": "https://pbs.twimg.com/semantic_core_img/2094846255792873472/BUi2WqsC?format=png&name=orig",
                "light": "https://pbs.twimg.com/semantic_core_img/2094841642129739776/YCBRBHV5?format=png&name=orig",
                "dark": "https://pbs.twimg.com/semantic_core_img/2094848191451598848/82O7RY0H?format=png&name=orig",
            },
            "xUserId": "43403778",
            "record": {"wins": 7, "losses": 1, "ties": 0},
        }
    },
}

SCOREBOARD = {
    "id": "2055084502741811200",
    "league": "nfl",
    "seasonId": "2039131233582546945",
    "seasonType": "RegularSeason",
    "week": 6,
    "startsAt": "2026-10-20T00:15:00.000Z",
    "venue": "Levi's Stadium",
    "status": "Closed",
    "clock": "00:00:00",
    "quarter": 4,
    "situation": {
        "down": 3,
        "yardsToGo": 22,
        "yardline": 40,
        "yardlineTeamId": "689566294702555136",
        "possessionTeamId": "689566304366292992",
    },
    "home": {"teamId": "689566294702555136", "points": 23, "timeoutsLeft": 2},
    "away": {"teamId": "689566294702555136", "points": 23, "timeoutsLeft": 2},
    "periods": [{"number": 1, "type": "Quarter", "sequence": 1, "homePoints": 13, "awayPoints": 3}],
    "lastPlay": {
        "id": "170",
        "sequence": 9,
        "clock": "00:10:58",
        "type": "Pass",
        "direction": "Left",
        "description": "(10:58) B.Purdy pass short left to G.Kittle for 11 yards, TOUCHDOWN.",
        "scoring": True,
        "homePoints": 6,
        "awayPoints": 0,
        "score": {"homePoints": 6, "awayPoints": 0, "points": 6},
        "start": {
            "down": 1,
            "yardsToGo": 10,
            "yardline": 11,
            "yardlineSide": "Away",
            "possession": "5c218a3b-a013-4037-97b6-603c9502b701",
        },
        "onField": {"calledBack": False, "penaltyOnField": False, "timeout": True, "underReview": False},
        "details": [
            {
                "sequence": 1,
                "category": "Pass",
                "description": "Pass attempt",
                "direction": None,
                "yards": None,
                "players": [{"playerId": "1520565710329499648", "playerRole": "Pass"}],
                "penalty": None,
            }
        ],
        "post": {"id": "2112339130483151117", "username": "text"},
        "videoPostId": "2112339130483151117",
        "videoReplyPostId": "text",
    },
    "teams": {
        "689566294702555136": {
            "id": "689566294702555136",
            "name": "San Francisco 49ers",
            "shortName": "49ers",
            "abbreviation": "SF",
            "alternateId": "f0e724b0-4cbf-495a-be47-013907608da9",
            "location": "Virginia Tech",
            "colors": [{"r": 170, "g": 0, "b": 0}],
            "logos": {
                "default": "https://pbs.twimg.com/semantic_core_img/2094846255792873472/BUi2WqsC?format=png&name=orig",
                "light": "https://pbs.twimg.com/semantic_core_img/2094841642129739776/YCBRBHV5?format=png&name=orig",
                "dark": "https://pbs.twimg.com/semantic_core_img/2094848191451598848/82O7RY0H?format=png&name=orig",
            },
            "xUserId": "43403778",
            "record": None,
        }
    },
    "players": {
        "1520565710329499648": {
            "id": "1520565710329499648",
            "teamId": "689566294702555136",
            "name": "Brock Purdy",
            "shortName": "B.Purdy",
            "jersey": "13",
            "position": "QB",
            "college": "Iowa State",
            "birthPlace": "Gilbert, AZ, USA",
            "birthDate": "1999-12-27",
            "headshots": {
                "original": "https://ton.twimg.com/twitter-assets/sports-product/headshots/nfl/1520565710329499648_large_c96c3d47bd.png",
                "large": "https://pbs.twimg.com/semantic_core_img/1960525277903106048/qEOJWYP6?format=png&name=orig",
                "medium": "https://pbs.twimg.com/semantic_core_img/1960514226075602944/OZ6rz5aH?format=png&name=orig",
                "small": "https://pbs.twimg.com/semantic_core_img/1960202905849405441/OnS0Xdd9?format=png&name=orig",
            },
            "xUser": {"id": "723177170382647296", "username": "brockpurdy13", "blueVerified": True},
        }
    },
}

BOX_SCORE = {
    "id": "2055084502741811200",
    "league": "nfl",
    "home": {
        "teamId": "689566294702555136",
        "totals": {
            "firstDowns": 20,
            "thirdDowns": {"attempts": 14, "successes": 7},
            "fumbles": {"lost": 1, "opponentRecoveryTouchdowns": 0, "ownRecoveryTouchdowns": 0},
            "passing": {
                "attempts": 29,
                "avgYards": 9.10345,
                "completions": 21,
                "interceptions": 0,
                "netYards": 249,
                "rating": 111.85345,
                "sackYards": 15,
                "sacks": 2,
                "touchdowns": 1,
                "yards": 264,
            },
            "penalties": {"count": 11, "yards": 88},
            "rushing": {"attempts": 5, "avgYards": 5.6, "longest": 11, "touchdowns": 0, "yards": 28},
            "timeOfPossessionSeconds": 1785,
            "totalYards": 375,
            "turnovers": 1,
        },
        "players": [
            {
                "playerId": "1520565710329499648",
                "passing": {
                    "attempts": 29,
                    "avgYards": 9.10345,
                    "completions": 21,
                    "interceptions": 0,
                    "netYards": 249,
                    "rating": 111.85345,
                    "sackYards": 15,
                    "sacks": 2,
                    "touchdowns": 1,
                    "yards": 264,
                },
                "rushing": {"attempts": 5, "avgYards": 5.6, "longest": 11, "touchdowns": 0, "yards": 28},
                "receiving": {"avgYards": 3, "longest": 3, "receptions": 1, "targets": 1, "touchdowns": 0, "yards": 3},
                "defense": {
                    "combined": 8,
                    "forcedFumbles": 0,
                    "interceptions": 0,
                    "passesDefended": 0,
                    "sacks": 0.5,
                    "tackles": 6,
                    "tacklesForLoss": 0,
                },
                "fumbles": {"lost": 1, "opponentRecoveryTouchdowns": 0, "ownRecoveryTouchdowns": 0},
                "kickReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "puntReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "interceptionReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "punts": {
                    "attempts": 4,
                    "avgNetYards": 47.8,
                    "avgYards": 47.75,
                    "inside20": 0,
                    "longest": 49,
                    "yards": 191,
                },
                "fieldGoals": {"attempts": 1, "longest": 33, "made": 1},
                "extraPoints": {"attempts": 3, "made": 2},
                "conversions": {"defenseSuccesses": 0, "passSuccesses": 1, "rushSuccesses": 0, "turnoverSuccesses": 0},
            }
        ],
    },
    "away": {
        "teamId": "689566294702555136",
        "totals": {
            "firstDowns": 20,
            "thirdDowns": {"attempts": 14, "successes": 7},
            "fumbles": {"lost": 1, "opponentRecoveryTouchdowns": 0, "ownRecoveryTouchdowns": 0},
            "passing": {
                "attempts": 29,
                "avgYards": 9.10345,
                "completions": 21,
                "interceptions": 0,
                "netYards": 249,
                "rating": 111.85345,
                "sackYards": 15,
                "sacks": 2,
                "touchdowns": 1,
                "yards": 264,
            },
            "penalties": {"count": 11, "yards": 88},
            "rushing": {"attempts": 5, "avgYards": 5.6, "longest": 11, "touchdowns": 0, "yards": 28},
            "timeOfPossessionSeconds": 1785,
            "totalYards": 375,
            "turnovers": 1,
        },
        "players": [
            {
                "playerId": "1520565710329499648",
                "passing": {
                    "attempts": 29,
                    "avgYards": 9.10345,
                    "completions": 21,
                    "interceptions": 0,
                    "netYards": 249,
                    "rating": 111.85345,
                    "sackYards": 15,
                    "sacks": 2,
                    "touchdowns": 1,
                    "yards": 264,
                },
                "rushing": {"attempts": 5, "avgYards": 5.6, "longest": 11, "touchdowns": 0, "yards": 28},
                "receiving": {"avgYards": 3, "longest": 3, "receptions": 1, "targets": 1, "touchdowns": 0, "yards": 3},
                "defense": {
                    "combined": 8,
                    "forcedFumbles": 0,
                    "interceptions": 0,
                    "passesDefended": 0,
                    "sacks": 0.5,
                    "tackles": 6,
                    "tacklesForLoss": 0,
                },
                "fumbles": {"lost": 1, "opponentRecoveryTouchdowns": 0, "ownRecoveryTouchdowns": 0},
                "kickReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "puntReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "interceptionReturns": {"avgYards": 24, "longest": 24, "returns": 1, "touchdowns": 0, "yards": 24},
                "punts": {
                    "attempts": 4,
                    "avgNetYards": 47.8,
                    "avgYards": 47.75,
                    "inside20": 0,
                    "longest": 49,
                    "yards": 191,
                },
                "fieldGoals": {"attempts": 1, "longest": 33, "made": 1},
                "extraPoints": {"attempts": 3, "made": 2},
                "conversions": {"defenseSuccesses": 0, "passSuccesses": 1, "rushSuccesses": 0, "turnoverSuccesses": 0},
            }
        ],
    },
    "teams": {
        "689566294702555136": {
            "id": "689566294702555136",
            "name": "San Francisco 49ers",
            "shortName": "49ers",
            "abbreviation": "SF",
            "alternateId": "f0e724b0-4cbf-495a-be47-013907608da9",
            "location": "Virginia Tech",
            "colors": [{"r": 170, "g": 0, "b": 0}],
            "logos": {
                "default": "https://pbs.twimg.com/semantic_core_img/2094846255792873472/BUi2WqsC?format=png&name=orig",
                "light": "https://pbs.twimg.com/semantic_core_img/2094841642129739776/YCBRBHV5?format=png&name=orig",
                "dark": "https://pbs.twimg.com/semantic_core_img/2094848191451598848/82O7RY0H?format=png&name=orig",
            },
            "xUserId": "43403778",
            "record": None,
        }
    },
    "players": {
        "1520565710329499648": {
            "id": "1520565710329499648",
            "teamId": "689566294702555136",
            "name": "Brock Purdy",
            "shortName": "B.Purdy",
            "jersey": "13",
            "position": "QB",
            "college": "Iowa State",
            "birthPlace": "Gilbert, AZ, USA",
            "birthDate": "1999-12-27",
            "headshots": {
                "original": "https://ton.twimg.com/twitter-assets/sports-product/headshots/nfl/1520565710329499648_large_c96c3d47bd.png",
                "large": "https://pbs.twimg.com/semantic_core_img/1960525277903106048/qEOJWYP6?format=png&name=orig",
                "medium": "https://pbs.twimg.com/semantic_core_img/1960514226075602944/OZ6rz5aH?format=png&name=orig",
                "small": "https://pbs.twimg.com/semantic_core_img/1960202905849405441/OnS0Xdd9?format=png&name=orig",
            },
            "xUser": {"id": "723177170382647296", "username": "brockpurdy13", "blueVerified": True},
        }
    },
}

PLAYS = {
    "id": "2055084502741811200",
    "league": "nfl",
    "homeTeamId": "689566294702555136",
    "awayTeamId": "689566304366292992",
    "quarters": [
        {
            "id": "quarter-1",
            "number": 1,
            "sequence": 1,
            "drives": [
                {
                    "id": "drive-2",
                    "sequence": 2,
                    "offense": "Home",
                    "defense": "Away",
                    "startClock": "00:14:55",
                    "endClock": "00:10:53",
                    "startReason": "Kickoff",
                    "endReason": "Touchdown",
                    "playCount": 10,
                    "firstDowns": 0,
                    "netYards": 64,
                    "scoring": True,
                    "plays": [
                        {
                            "id": "170",
                            "sequence": 9,
                            "clock": "00:10:58",
                            "type": "Pass",
                            "direction": "Left",
                            "description": "(10:58) B.Purdy pass short left to G.Kittle for 11 yards, TOUCHDOWN.",
                            "scoring": True,
                            "homePoints": 6,
                            "awayPoints": 0,
                            "score": {"homePoints": 6, "awayPoints": 0, "points": 6},
                            "start": {
                                "down": 1,
                                "yardsToGo": 10,
                                "yardline": 11,
                                "yardlineSide": "Away",
                                "possession": "5c218a3b-a013-4037-97b6-603c9502b701",
                            },
                            "onField": {
                                "calledBack": False,
                                "penaltyOnField": False,
                                "timeout": True,
                                "underReview": False,
                            },
                            "details": [
                                {
                                    "sequence": 1,
                                    "category": "Pass",
                                    "description": "Pass attempt",
                                    "direction": None,
                                    "yards": None,
                                    "players": [{"playerId": "1520565710329499648", "playerRole": "Pass"}],
                                    "penalty": None,
                                }
                            ],
                            "post": {"id": "2112339130483151117", "username": "text"},
                            "videoPostId": "2112339130483151117",
                            "videoReplyPostId": "text",
                        }
                    ],
                }
            ],
        }
    ],
    "teams": {
        "689566294702555136": {
            "id": "689566294702555136",
            "name": "San Francisco 49ers",
            "shortName": "49ers",
            "abbreviation": "SF",
            "alternateId": "f0e724b0-4cbf-495a-be47-013907608da9",
            "location": "Virginia Tech",
            "colors": [{"r": 170, "g": 0, "b": 0}],
            "logos": {
                "default": "https://pbs.twimg.com/semantic_core_img/2094846255792873472/BUi2WqsC?format=png&name=orig",
                "light": "https://pbs.twimg.com/semantic_core_img/2094841642129739776/YCBRBHV5?format=png&name=orig",
                "dark": "https://pbs.twimg.com/semantic_core_img/2094848191451598848/82O7RY0H?format=png&name=orig",
            },
            "xUserId": "43403778",
            "record": None,
        }
    },
    "players": {
        "1520565710329499648": {
            "id": "1520565710329499648",
            "teamId": "689566294702555136",
            "name": "Brock Purdy",
            "shortName": "B.Purdy",
            "jersey": "13",
            "position": "QB",
            "college": "Iowa State",
            "birthPlace": "Gilbert, AZ, USA",
            "birthDate": "1999-12-27",
            "headshots": {
                "original": "https://ton.twimg.com/twitter-assets/sports-product/headshots/nfl/1520565710329499648_large_c96c3d47bd.png",
                "large": "https://pbs.twimg.com/semantic_core_img/1960525277903106048/qEOJWYP6?format=png&name=orig",
                "medium": "https://pbs.twimg.com/semantic_core_img/1960514226075602944/OZ6rz5aH?format=png&name=orig",
                "small": "https://pbs.twimg.com/semantic_core_img/1960202905849405441/OnS0Xdd9?format=png&name=orig",
            },
            "xUser": {"id": "723177170382647296", "username": "brockpurdy13", "blueVerified": True},
        }
    },
}


AUDIENCE = {
    "id": "2055084502741811200",
    "league": "ncaafb",
    "viewers": {"count": 155, "asOf": "2026-10-20T06:19:50.000Z"},
    "teamPicks": {
        "total": 7976,
        "teams": [
            {"teamId": "689566294702555136", "count": 4998},
            {"teamId": "689566304366292992", "count": 2978},
        ],
    },
    "chat": {
        "available": False,
        "broadcastId": "nfl-2055084502741811200",
        "opensIn": {"days": 0, "hours": 12, "minutes": 2},
    },
    "teams": {
        "689566294702555136": {
            "id": "689566294702555136",
            "name": "Virginia Tech Hokies",
            "shortName": None,
            "abbreviation": "VT",
            "alternateId": None,
            "location": "Virginia Tech",
            "colors": [{"r": 134, "g": 31, "b": 65}],
            "logos": {"default": None, "light": None, "dark": None},
            "xUserId": None,
            "record": None,
        }
    },
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_list_games_sends_the_league_and_window(asynchronous: bool) -> None:
    request, schedule = await send_with_mock_transport(
        lambda client: client.x.sports.list_games(
            "nfl", from_="2026-10-01", to="2026-10-08", team="689566294702555136"
        ),
        lambda client: client.x.sports.list_games(
            "nfl", from_="2026-10-01", to="2026-10-08", team="689566294702555136"
        ),
        SCHEDULE,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/x/sports/nfl/games"
    assert dict(request.url.params) == {"from": "2026-10-01", "to": "2026-10-08", "team": "689566294702555136"}
    assert isinstance(schedule, FootballSchedule)
    game = schedule.games[0]
    assert game.id == "2055084502741811200"
    assert game.starts_at == datetime(2026, 10, 20, 0, 15, tzinfo=timezone.utc)
    assert game.team_ids == ["689566294702555136", "689566304366292992"]
    assert game.odds is not None and game.odds.away.spread == "text"
    team = schedule.teams["689566294702555136"]
    assert team.abbreviation == "SF"
    assert team.colors[0].r == 170
    assert team.x_user_id == "43403778"
    assert team.record is not None and (team.record.wins, team.record.losses, team.record.ties) == (7, 1, 0)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_scoreboard_reads_1_game(asynchronous: bool) -> None:
    request, scoreboard = await send_with_mock_transport(
        lambda client: client.x.sports.retrieve_scoreboard("2055084502741811200", league="nfl", fields="id,home"),
        lambda client: client.x.sports.retrieve_scoreboard("2055084502741811200", league="nfl", fields="id,home"),
        SCOREBOARD,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/sports/nfl/games/2055084502741811200"
    assert dict(request.url.params) == {"fields": "id,home"}
    assert isinstance(scoreboard, FootballScoreboard)
    assert scoreboard.venue == "Levi's Stadium"
    assert scoreboard.situation is not None and scoreboard.situation.yards_to_go == 22
    assert scoreboard.home.timeouts_left == 2
    assert scoreboard.periods[0].home_points == 13
    assert scoreboard.last_play is not None and scoreboard.last_play.id == "170"
    x_user = scoreboard.players["1520565710329499648"].x_user
    assert x_user is not None and x_user.username == "brockpurdy13"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_box_score_reads_team_and_player_stats(asynchronous: bool) -> None:
    request, box = await send_with_mock_transport(
        lambda client: client.x.sports.retrieve_box_score("2055084502741811200", league="ncaafb"),
        lambda client: client.x.sports.retrieve_box_score("2055084502741811200", league="ncaafb"),
        BOX_SCORE,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/sports/ncaafb/games/2055084502741811200/box-score"
    assert isinstance(box, FootballBoxScore)
    totals = box.home.totals
    assert totals is not None and totals.third_downs is not None and totals.third_downs.attempts == 14
    player = box.home.players[0]
    assert player.passing is not None and player.passing.yards == 264
    assert player.defense is not None and player.defense.sacks == 0.5


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_plays_reads_drives_and_plays(asynchronous: bool) -> None:
    request, plays = await send_with_mock_transport(
        lambda client: client.x.sports.retrieve_plays("2055084502741811200", league="nfl", omit="players"),
        lambda client: client.x.sports.retrieve_plays("2055084502741811200", league="nfl", omit="players"),
        PLAYS,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/sports/nfl/games/2055084502741811200/plays"
    assert dict(request.url.params) == {"omit": "players"}
    assert isinstance(plays, FootballPlays)
    drive = plays.quarters[0].drives[0]
    assert drive.start_reason == "Kickoff"
    play = drive.plays[0]
    assert play.type == "Pass"
    assert play.details[0].players[0].player_role == "Pass"
    assert play.details[0].yards is None
    assert play.post is not None and play.post.id == "2112339130483151117"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_audience_reads_viewers_team_picks_and_chat(asynchronous: bool) -> None:
    request, audience = await send_with_mock_transport(
        lambda client: client.x.sports.retrieve_audience("2055084502741811200", league="ncaafb", fields="viewers,chat"),
        lambda client: client.x.sports.retrieve_audience("2055084502741811200", league="ncaafb", fields="viewers,chat"),
        AUDIENCE,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/x/sports/ncaafb/games/2055084502741811200/audience"
    assert dict(request.url.params) == {"fields": "viewers,chat"}
    assert isinstance(audience, SportsGameAudience)
    assert audience.viewers is not None and audience.viewers.as_of == datetime(
        2026, 10, 20, 6, 19, 50, tzinfo=timezone.utc
    )
    assert [pick.count for pick in audience.team_picks.teams] == [4998, 2978]
    assert audience.chat.broadcast_id == "nfl-2055084502741811200"
    assert audience.chat.opens_in is not None and audience.chat.opens_in.hours == 12
    team = audience.teams["689566294702555136"]
    assert team.location == "Virginia Tech"
    assert team.record is None


@pytest.mark.parametrize("method", ["retrieve_scoreboard", "retrieve_box_score", "retrieve_plays", "retrieve_audience"])
def test_an_empty_id_or_league_raises_before_any_request(client: XTwitterScraper, method: str) -> None:
    with pytest.raises(ValueError, match="`id`"):
        getattr(client.x.sports, method)("", league="nfl")
    with pytest.raises(ValueError, match="`league`"):
        getattr(client.x.sports, method)("1", league="")
    with pytest.raises(ValueError, match="`league`"):
        client.x.sports.list_games("")


@pytest.mark.parametrize("method", ["retrieve_scoreboard", "retrieve_box_score", "retrieve_plays", "retrieve_audience"])
async def test_an_async_empty_id_or_league_raises_before_any_request(
    async_client: AsyncXTwitterScraper, method: str
) -> None:
    with pytest.raises(ValueError, match="`id`"):
        await getattr(async_client.x.sports, method)("", league="nfl")
    with pytest.raises(ValueError, match="`league`"):
        await getattr(async_client.x.sports, method)("1", league="")
    with pytest.raises(ValueError, match="`league`"):
        await async_client.x.sports.list_games("")
