# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FootballLeague",
    "FootballTeamScore",
    "FootballSchedulePeriod",
    "FootballOdds",
    "FootballScheduleGameOdds",
    "FootballScheduleGame",
    "SportsTeamColor",
    "SportsTeamLogos",
    "SportsTeam",
    "FootballSchedule",
    "FootballScoreboardSituation",
    "FootballSide",
    "FootballPeriod",
    "FootballPlayScore",
    "FootballPlayStart",
    "FootballPlayOnField",
    "FootballPlayDetailPlayer",
    "FootballPlayDetailPenalty",
    "FootballPlayDetail",
    "FootballPlayPost",
    "FootballPlay",
    "FootballPlayerHeadshots",
    "FootballPlayerXUser",
    "FootballPlayer",
    "FootballScoreboard",
    "FootballTeamTotalsThirdDowns",
    "FootballFumbleStats",
    "FootballPassingStats",
    "FootballTeamTotalsPenalties",
    "FootballRushingStats",
    "FootballTeamTotals",
    "FootballPlayerStatsReceiving",
    "FootballPlayerStatsDefense",
    "FootballReturnStats",
    "FootballPlayerStatsPunts",
    "FootballPlayerStatsFieldGoals",
    "FootballPlayerStatsExtraPoints",
    "FootballPlayerStatsConversions",
    "FootballPlayerStats",
    "FootballTeamBox",
    "FootballBoxScore",
    "FootballDrive",
    "FootballQuarter",
    "FootballPlays",
]

FootballLeague: TypeAlias = Literal["nfl", "ncaafb"]


class FootballTeamScore(BaseModel):
    """A team's side of a game & its points."""

    team_id: Optional[str] = FieldInfo(alias="teamId")
    """The team, a key of teams."""

    points: Optional[int]
    """The team's points so far."""


class FootballSchedulePeriod(BaseModel):
    """A period of a listed game."""

    type: Optional[str]
    """X's name for the period, such as Quarter."""


class FootballOdds(BaseModel):
    """Betting odds titles for 1 team, as X shows them."""

    money_line: Optional[str] = FieldInfo(alias="moneyLine")
    """The money line. X sends it for the away team only."""

    spread: Optional[str]
    """The point spread."""

    total: Optional[str]
    """The over or under total."""


class FootballScheduleGameOdds(BaseModel):
    """Betting odds for each team, or null when X has none."""

    home: FootballOdds
    """Betting odds titles for 1 team, as X shows them."""

    away: FootballOdds
    """Betting odds titles for 1 team, as X shows them."""


class FootballScheduleGame(BaseModel):
    """A listed game, with its teams & score."""

    id: str
    """The game ID the other sports routes take."""

    season_type: Optional[str] = FieldInfo(alias="seasonType")
    """This game's part of the season, such as RegularSeason."""

    week: Optional[int]
    """This game's week of the season."""

    starts_at: Optional[datetime] = FieldInfo(alias="startsAt")
    """This game's kickoff time in UTC, or null when Xquik cannot read it."""

    status: Optional[str]
    """This game's status from X, such as Scheduled, InProgress or Closed."""

    clock: Optional[str]
    """This game's clock, as X writes it."""

    quarter: Optional[int]
    """This game's current or last quarter."""

    home: FootballTeamScore
    """A team's side of a game & its points."""

    away: FootballTeamScore
    """A team's side of a game & its points."""

    team_ids: List[str] = FieldInfo(alias="teamIds")
    """The game's teams, keys of teams."""

    periods: List[FootballSchedulePeriod]
    """The periods played so far."""

    odds: Optional[FootballScheduleGameOdds]
    """Betting odds for each team, or null when X has none."""


class SportsTeamColor(BaseModel):
    r: Optional[int]
    """Red, from 0 to 255."""

    g: Optional[int]
    """Green, from 0 to 255."""

    b: Optional[int]
    """Blue, from 0 to 255."""


class SportsTeamLogos(BaseModel):
    """The team's logo images."""

    default: Optional[str]
    """The logo X shows by default."""

    light: Optional[str]
    """The logo for light backgrounds."""

    dark: Optional[str]
    """The logo for dark backgrounds."""


class SportsTeam(BaseModel):
    """A team, as X's sports pages show it."""

    id: str
    """The team ID that games & players refer to."""

    name: Optional[str]
    """The team's full name."""

    short_name: Optional[str] = FieldInfo(alias="shortName")
    """The team's short name."""

    abbreviation: Optional[str]
    """The team's abbreviation."""

    alternate_id: Optional[str] = FieldInfo(alias="alternateId")
    """Another ID X keeps for the team."""

    location: Optional[str]
    """The school or place a college team plays for. X sends it only in college
    football schedules.
    """

    colors: List[SportsTeamColor]
    """The team's colors, as red, green & blue from 0 to 255."""

    logos: SportsTeamLogos
    """The team's logo images."""

    x_user_id: Optional[str] = FieldInfo(alias="xUserId")
    """The user ID of the team's X account."""


class FootballSchedule(BaseModel):
    """A league's games in a time window."""

    league: FootballLeague
    """The league whose games this list holds."""

    games: List[FootballScheduleGame]
    """The games, earliest first."""

    teams: Dict[str, SportsTeam]
    """The teams the games name, by team ID."""


class FootballScoreboardSituation(BaseModel):
    """Down & distance now, or null before kickoff."""

    down: Optional[int]
    """The current down, from 1 to 4."""

    yards_to_go: Optional[int] = FieldInfo(alias="yardsToGo")
    """The yards the offense needs now for a first down."""

    yardline: Optional[int]
    """The ball's current yard line."""

    yardline_team_id: Optional[str] = FieldInfo(alias="yardlineTeamId")
    """The team whose half the ball is in, a key of teams."""

    possession_team_id: Optional[str] = FieldInfo(alias="possessionTeamId")
    """The team with the ball, a key of teams."""


class FootballSide(BaseModel):
    """A team's side of a scoreboard."""

    team_id: Optional[str] = FieldInfo(alias="teamId")
    """The team, a key of teams."""

    points: Optional[int]
    """The team's points so far."""

    timeouts_left: Optional[int] = FieldInfo(alias="timeoutsLeft")
    """The timeouts the team has left."""


class FootballPeriod(BaseModel):
    """A period of a game & its points."""

    type: Optional[str]
    """X's name for the period, such as Quarter."""

    number: Optional[int]
    """The period's number, or null when X sends no digits."""

    sequence: Optional[int]
    """The period's place in the game, from 1."""

    home_points: Optional[int] = FieldInfo(alias="homePoints")
    """The home team's points in the period."""

    away_points: Optional[int] = FieldInfo(alias="awayPoints")
    """The away team's points in the period."""


class FootballPlayScore(BaseModel):
    """The points a scoring play added, or null."""

    home_points: Optional[int] = FieldInfo(alias="homePoints")
    """The home team's score once this scoring play counted."""

    away_points: Optional[int] = FieldInfo(alias="awayPoints")
    """The away team's score once this scoring play counted."""

    points: Optional[int]
    """The points the play scored."""


class FootballPlayStart(BaseModel):
    """Down & distance when the play started, or null."""

    down: Optional[int]
    """The down, from 1 to 4."""

    yards_to_go: Optional[int] = FieldInfo(alias="yardsToGo")
    """The yards needed for a first down."""

    yardline: Optional[int]
    """The yard line of the ball."""

    yardline_side: Optional[str] = FieldInfo(alias="yardlineSide")
    """Whose half the ball was in. Home or Away in NFL games, the team's alternateId
    in college games.
    """

    possession: Optional[str]
    """The team with the ball. Home or Away in NFL games, the team's alternateId in
    college games.
    """


class FootballPlayOnField(BaseModel):
    """Flags X shows on the field for the play, or null."""

    called_back: Optional[bool] = FieldInfo(alias="calledBack")
    """Whether a penalty called the play back."""

    penalty_on_field: Optional[bool] = FieldInfo(alias="penaltyOnField")
    """Whether a flag was thrown."""

    timeout: Optional[bool]
    """Whether a timeout followed the play."""

    under_review: Optional[bool] = FieldInfo(alias="underReview")
    """Whether officials were reviewing the play."""


class FootballPlayDetailPlayer(BaseModel):
    player_id: Optional[str] = FieldInfo(alias="playerId")
    """The player, a key of players."""

    player_role: Optional[str] = FieldInfo(alias="playerRole")
    """The player's role, such as Pass, Receive or Tackle."""


class FootballPlayDetailPenalty(BaseModel):
    """The penalty this step called, or null."""

    description: Optional[str]
    """The penalty's name."""

    next_down: Optional[str] = FieldInfo(alias="nextDown")
    """What the penalty does to the down."""

    result: Optional[str]
    """Whether the penalty was accepted or declined."""

    team_id: Optional[str] = FieldInfo(alias="teamId")
    """The penalized team, a key of teams."""

    yards: Optional[int]
    """The penalty's yards."""


class FootballPlayDetail(BaseModel):
    """1 step of a play, such as a pass, a tackle or a penalty."""

    sequence: Optional[int]
    """The step's place in the play, from 1."""

    category: Optional[str]
    """X's kind of step, such as Pass, Tackle or Penalty."""

    description: Optional[str]
    """What happened in the step."""

    direction: Optional[str]
    """The direction X gives for the step."""

    yards: Optional[int]
    """The yards the step gained or lost."""

    players: List[FootballPlayDetailPlayer]
    """The players in the step & their roles."""

    penalty: Optional[FootballPlayDetailPenalty]
    """The penalty this step called, or null."""


class FootballPlayPost(BaseModel):
    """The post X links to the play, or null."""

    id: str
    """The post's ID."""

    username: Optional[str]
    """The username of the post's author, when X sends it."""


class FootballPlay(BaseModel):
    """A play, with its situation, steps & linked posts."""

    id: Optional[str]
    """X's ID for the play within the game."""

    sequence: Optional[int]
    """The play's place in its drive, or null when X sends no digits."""

    clock: Optional[str]
    """The game clock when the play started, as HH:MM:SS."""

    type: Optional[str]
    """X's kind of play, such as Pass, Rush, Punt or Conversion."""

    direction: Optional[str]
    """Where the play went, such as Left or Middle."""

    description: Optional[str]
    """The play as the official play-by-play writes it."""

    scoring: Optional[bool]
    """Whether the play scored points."""

    home_points: Optional[int] = FieldInfo(alias="homePoints")
    """The home team's points after the play."""

    away_points: Optional[int] = FieldInfo(alias="awayPoints")
    """The away team's points after the play."""

    score: Optional[FootballPlayScore]
    """The points a scoring play added, or null."""

    start: Optional[FootballPlayStart]
    """Down & distance when the play started, or null."""

    on_field: Optional[FootballPlayOnField] = FieldInfo(alias="onField")
    """Flags X shows on the field for the play, or null."""

    details: List[FootballPlayDetail]
    """The play's steps, in order."""

    post: Optional[FootballPlayPost]
    """The post X links to the play, or null."""

    video_post_id: Optional[str] = FieldInfo(alias="videoPostId")
    """The ID of a post with the play's video."""

    video_reply_post_id: Optional[str] = FieldInfo(alias="videoReplyPostId")
    """The ID of a reply with the play's video."""


class FootballPlayerHeadshots(BaseModel):
    """Photos of the player. Any of them can be null."""

    original: Optional[str]
    """The photo X shows on the player's card."""

    large: Optional[str]
    """The large photo."""

    medium: Optional[str]
    """The medium photo."""

    small: Optional[str]
    """The small photo."""


class FootballPlayerXUser(BaseModel):
    """The player's X account, or null without one."""

    id: str
    """The account's user ID."""

    username: Optional[str]
    """The account's username, without @."""

    blue_verified: Optional[bool] = FieldInfo(alias="blueVerified")
    """Whether the account has a blue check."""


class FootballPlayer(BaseModel):
    """A football player, as X's sports pages show them."""

    id: str
    """The player ID that plays & stats refer to."""

    team_id: Optional[str] = FieldInfo(alias="teamId")
    """The player's team, a key of teams."""

    name: Optional[str]
    """The player's full name."""

    short_name: Optional[str] = FieldInfo(alias="shortName")
    """The name play descriptions use."""

    jersey: Optional[str]
    """The jersey number, as text."""

    position: Optional[str]
    """The position abbreviation, such as QB or DE."""

    college: Optional[str]
    """The college the player came from."""

    birth_place: Optional[str] = FieldInfo(alias="birthPlace")
    """Where the player was born."""

    birth_date: Optional[str] = FieldInfo(alias="birthDate")
    """The birth date, as YYYY-MM-DD."""

    headshots: FootballPlayerHeadshots
    """Photos of the player. Any of them can be null."""

    x_user: Optional[FootballPlayerXUser] = FieldInfo(alias="xUser")
    """The player's X account, or null without one."""


class FootballScoreboard(BaseModel):
    """1 game's scoreboard."""

    id: str
    """The game ID from your request."""

    league: FootballLeague
    """The league from your request."""

    season_id: Optional[str] = FieldInfo(alias="seasonId")
    """X's ID for the season. NFL games have one."""

    season_type: Optional[str] = FieldInfo(alias="seasonType")
    """The part of the season, such as RegularSeason."""

    week: Optional[int]
    """The week of the season."""

    starts_at: Optional[datetime] = FieldInfo(alias="startsAt")
    """The kickoff time in UTC, or null when X sends none Xquik can read."""

    venue: Optional[str]
    """The stadium."""

    status: Optional[str]
    """X's game status, such as Scheduled, InProgress or Closed."""

    clock: Optional[str]
    """The game clock, as X writes it."""

    quarter: Optional[int]
    """The current or last quarter."""

    situation: Optional[FootballScoreboardSituation]
    """Down & distance now, or null before kickoff."""

    home: FootballSide
    """A team's side of a scoreboard."""

    away: FootballSide
    """A team's side of a scoreboard."""

    periods: List[FootballPeriod]
    """Points by period, in order."""

    last_play: Optional[FootballPlay] = FieldInfo(alias="lastPlay")
    """The latest play, or null before kickoff."""

    teams: Dict[str, SportsTeam]
    """The teams this answer names, by team ID."""

    players: Dict[str, FootballPlayer]
    """The players this answer names, by player ID."""


class FootballTeamTotalsThirdDowns(BaseModel):
    """Third downs tried & converted."""

    attempts: Optional[int]
    """Third downs tried."""

    successes: Optional[int]
    """Third downs converted."""


class FootballFumbleStats(BaseModel):
    """Fumble stats."""

    lost: Optional[int]
    """Fumbles the other team recovered."""

    opponent_recovery_touchdowns: Optional[int] = FieldInfo(alias="opponentRecoveryTouchdowns")
    """Touchdowns scored after recovering the other team's fumble."""

    own_recovery_touchdowns: Optional[int] = FieldInfo(alias="ownRecoveryTouchdowns")
    """Touchdowns scored after recovering an own fumble."""


class FootballPassingStats(BaseModel):
    """Passing stats."""

    attempts: Optional[int]
    """Passes thrown."""

    avg_yards: Optional[float] = FieldInfo(alias="avgYards")
    """Yards per pass."""

    completions: Optional[int]
    """Passes caught."""

    interceptions: Optional[int]
    """Passes intercepted."""

    net_yards: Optional[int] = FieldInfo(alias="netYards")
    """Passing yards minus sack yards."""

    rating: Optional[float]
    """The passer rating."""

    sack_yards: Optional[int] = FieldInfo(alias="sackYards")
    """Yards lost to sacks."""

    sacks: Optional[int]
    """Times sacked."""

    touchdowns: Optional[int]
    """Passing touchdowns."""

    yards: Optional[int]
    """Passing yards."""


class FootballTeamTotalsPenalties(BaseModel):
    """Penalties against the team."""

    count: Optional[int]
    """Penalties."""

    yards: Optional[int]
    """Penalty yards."""


class FootballRushingStats(BaseModel):
    """Rushing stats."""

    attempts: Optional[int]
    """Rushes."""

    avg_yards: Optional[float] = FieldInfo(alias="avgYards")
    """Yards per rush."""

    longest: Optional[int]
    """The longest rush, in yards."""

    touchdowns: Optional[int]
    """Rushing touchdowns."""

    yards: Optional[int]
    """Rushing yards."""


class FootballTeamTotals(BaseModel):
    """A team's totals for 1 game."""

    first_downs: Optional[int] = FieldInfo(alias="firstDowns")
    """First downs."""

    third_downs: Optional[FootballTeamTotalsThirdDowns] = FieldInfo(alias="thirdDowns")
    """Third downs tried & converted."""

    fumbles: Optional[FootballFumbleStats]
    """The team's fumbles, or null."""

    passing: Optional[FootballPassingStats]
    """The team's passing, or null."""

    penalties: Optional[FootballTeamTotalsPenalties]
    """Penalties against the team."""

    rushing: Optional[FootballRushingStats]
    """The team's rushing, or null."""

    time_of_possession_seconds: Optional[int] = FieldInfo(alias="timeOfPossessionSeconds")
    """Time with the ball, in seconds."""

    total_yards: Optional[int] = FieldInfo(alias="totalYards")
    """Total yards."""

    turnovers: Optional[int]
    """Turnovers."""


class FootballPlayerStatsReceiving(BaseModel):
    """Receiving stats."""

    avg_yards: Optional[float] = FieldInfo(alias="avgYards")
    """Yards per catch."""

    longest: Optional[int]
    """The longest catch, in yards."""

    receptions: Optional[int]
    """Catches."""

    targets: Optional[int]
    """Passes thrown to the player."""

    touchdowns: Optional[int]
    """Receiving touchdowns."""

    yards: Optional[int]
    """Receiving yards."""


class FootballPlayerStatsDefense(BaseModel):
    """Defensive stats."""

    combined: Optional[float]
    """Solo & assisted tackles together."""

    forced_fumbles: Optional[int] = FieldInfo(alias="forcedFumbles")
    """Fumbles forced."""

    interceptions: Optional[int]
    """Interceptions."""

    passes_defended: Optional[int] = FieldInfo(alias="passesDefended")
    """Passes defended."""

    sacks: Optional[float]
    """Sacks, with a shared sack as 0.5."""

    tackles: Optional[float]
    """Solo tackles."""

    tackles_for_loss: Optional[float] = FieldInfo(alias="tacklesForLoss")
    """Tackles for a loss."""


class FootballReturnStats(BaseModel):
    """Kick, punt or interception return stats."""

    avg_yards: Optional[float] = FieldInfo(alias="avgYards")
    """Yards per return."""

    longest: Optional[int]
    """The longest return, in yards."""

    returns: Optional[int]
    """Returns."""

    touchdowns: Optional[int]
    """Return touchdowns."""

    yards: Optional[int]
    """Return yards."""


class FootballPlayerStatsPunts(BaseModel):
    """Punting stats."""

    attempts: Optional[int]
    """Punts."""

    avg_net_yards: Optional[float] = FieldInfo(alias="avgNetYards")
    """Net yards per punt, after returns."""

    avg_yards: Optional[float] = FieldInfo(alias="avgYards")
    """Yards per punt."""

    inside20: Optional[int]
    """Punts downed inside the 20."""

    longest: Optional[int]
    """The longest punt, in yards."""

    yards: Optional[int]
    """Punting yards."""


class FootballPlayerStatsFieldGoals(BaseModel):
    """Field goal stats."""

    attempts: Optional[int]
    """Field goals tried."""

    longest: Optional[int]
    """The longest made field goal, in yards."""

    made: Optional[int]
    """Field goals made."""


class FootballPlayerStatsExtraPoints(BaseModel):
    """Extra point kicks."""

    attempts: Optional[int]
    """Extra points tried."""

    made: Optional[int]
    """Extra points made."""


class FootballPlayerStatsConversions(BaseModel):
    """2-point conversions."""

    defense_successes: Optional[int] = FieldInfo(alias="defenseSuccesses")
    """Defensive 2-point returns."""

    pass_successes: Optional[int] = FieldInfo(alias="passSuccesses")
    """2-point conversions by pass."""

    rush_successes: Optional[int] = FieldInfo(alias="rushSuccesses")
    """2-point conversions by rush."""

    turnover_successes: Optional[int] = FieldInfo(alias="turnoverSuccesses")
    """2-point conversions after a turnover."""


class FootballPlayerStats(BaseModel):
    """1 player's stats for 1 game. Only the stat groups X sent are present."""

    player_id: Optional[str] = FieldInfo(alias="playerId")
    """The player these stats belong to, a key of players."""

    passing: Optional[FootballPassingStats] = None
    """Passing stats."""

    rushing: Optional[FootballRushingStats] = None
    """Rushing stats."""

    receiving: Optional[FootballPlayerStatsReceiving] = None
    """Receiving stats."""

    defense: Optional[FootballPlayerStatsDefense] = None
    """Defensive stats."""

    fumbles: Optional[FootballFumbleStats] = None
    """Fumble stats."""

    kick_returns: Optional[FootballReturnStats] = FieldInfo(alias="kickReturns", default=None)
    """Kick, punt or interception return stats."""

    punt_returns: Optional[FootballReturnStats] = FieldInfo(alias="puntReturns", default=None)
    """Kick, punt or interception return stats."""

    interception_returns: Optional[FootballReturnStats] = FieldInfo(alias="interceptionReturns", default=None)
    """Kick, punt or interception return stats."""

    punts: Optional[FootballPlayerStatsPunts] = None
    """Punting stats."""

    field_goals: Optional[FootballPlayerStatsFieldGoals] = FieldInfo(alias="fieldGoals", default=None)
    """Field goal stats."""

    extra_points: Optional[FootballPlayerStatsExtraPoints] = FieldInfo(alias="extraPoints", default=None)
    """Extra point kicks."""

    conversions: Optional[FootballPlayerStatsConversions] = None
    """2-point conversions."""


class FootballTeamBox(BaseModel):
    """1 team's totals & player stats."""

    team_id: Optional[str] = FieldInfo(alias="teamId")
    """The team these totals belong to, a key of teams."""

    totals: Optional[FootballTeamTotals]
    """The team's totals, or null before kickoff."""

    players: List[FootballPlayerStats]
    """Each player with stats, 1 entry per player."""


class FootballBoxScore(BaseModel):
    """1 game's team totals & player stats."""

    id: str
    """The ID of the game this box score covers."""

    league: FootballLeague
    """The league of the game this box score covers."""

    home: FootballTeamBox
    """1 team's totals & player stats."""

    away: FootballTeamBox
    """1 team's totals & player stats."""

    teams: Dict[str, SportsTeam]
    """The teams this box score names, by team ID."""

    players: Dict[str, FootballPlayer]
    """The players this box score names, by player ID."""


class FootballDrive(BaseModel):
    """A drive, with its result & plays."""

    id: Optional[str]
    """X's ID for the drive within the game."""

    sequence: Optional[int]
    """The drive's place in the game, from 1."""

    offense: Optional[str]
    """The team that drove. Home or Away in NFL games, the team's alternateId in
    college games.
    """

    defense: Optional[str]
    """The team on defense. Home or Away in NFL games, the team's alternateId in
    college games.
    """

    start_clock: Optional[str] = FieldInfo(alias="startClock")
    """The game clock when the drive started, as HH:MM:SS."""

    end_clock: Optional[str] = FieldInfo(alias="endClock")
    """The game clock when the drive ended, as HH:MM:SS."""

    start_reason: Optional[str] = FieldInfo(alias="startReason")
    """How the drive started, such as Kickoff or Punt."""

    end_reason: Optional[str] = FieldInfo(alias="endReason")
    """How the drive ended, such as Touchdown or Punt."""

    play_count: Optional[int] = FieldInfo(alias="playCount")
    """The drive's plays."""

    first_downs: Optional[int] = FieldInfo(alias="firstDowns")
    """The first downs the drive gained."""

    net_yards: Optional[int] = FieldInfo(alias="netYards")
    """The yards the drive gained."""

    scoring: Optional[bool]
    """Whether the drive scored."""

    plays: List[FootballPlay]
    """The drive's plays, in order."""


class FootballQuarter(BaseModel):
    """A quarter & its drives."""

    id: Optional[str]
    """X's ID for the quarter within the game."""

    number: Optional[int]
    """The quarter's number."""

    sequence: Optional[int]
    """The quarter's place in the game, from 1."""

    drives: List[FootballDrive]
    """The quarter's drives, in order."""


class FootballPlays(BaseModel):
    """1 game's drives & plays, by quarter."""

    id: str
    """The ID of the game these plays come from."""

    league: FootballLeague
    """The league of the game these plays come from."""

    home_team_id: Optional[str] = FieldInfo(alias="homeTeamId")
    """The home team, a key of teams."""

    away_team_id: Optional[str] = FieldInfo(alias="awayTeamId")
    """The away team, a key of teams."""

    quarters: List[FootballQuarter]
    """The game's quarters, in order. Empty before kickoff."""

    teams: Dict[str, SportsTeam]
    """The teams these plays name, by team ID."""

    players: Dict[str, FootballPlayer]
    """The players these plays name, by player ID."""
