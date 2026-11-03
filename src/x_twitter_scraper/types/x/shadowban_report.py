# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ShadowbanVerdict",
    "ShadowbanReport",
    "Checks",
    "ChecksAccount",
    "ChecksAccountEvidence",
    "ChecksSearch",
    "ChecksSearchEvidence",
    "ChecksSuggestion",
    "ChecksSuggestionEvidence",
    "ChecksReplies",
    "ChecksRepliesEvidence",
    "ChecksRepliesEvidenceReply",
]

ShadowbanVerdict: TypeAlias = Literal["pass", "fail", "unknown"]


class ChecksAccountEvidence(BaseModel):
    """Where to see the account on X."""

    profile_url: str = FieldInfo(alias="profileUrl")
    """Profile of the account on X."""


class ChecksAccount(BaseModel):
    """Passes an active or protected account & fails a suspended one."""

    verdict: ShadowbanVerdict
    """Pass means X shows the account there, and fail means it doesn't.

    Unknown means the check had nothing to test or X didn't answer.
    """

    reason: Literal["active", "protected", "suspended"]
    """State of the account on X."""

    evidence: ChecksAccountEvidence
    """Where to see the account on X."""


class ChecksSearchEvidence(BaseModel):
    """The search & the posts it looked for."""

    query: str
    """The search it ran."""

    search_url: str = FieldInfo(alias="searchUrl")
    """The same search on X, sorted by Latest."""

    recent_post_ids: List[str] = FieldInfo(alias="recentPostIds")
    """Up to 5 recent posts of the account."""

    found_post_ids: List[str] = FieldInfo(alias="foundPostIds")
    """Up to 5 posts of the account that search showed."""


class ChecksSearch(BaseModel):
    """Looks for the account's recent posts in X search, sorted by Latest.

    `listed` passes & `missing` fails.
    """

    verdict: ShadowbanVerdict
    """Pass means X shows the account there, and fail means it doesn't.

    Unknown means the check had nothing to test or X didn't answer.
    """

    reason: Literal["listed", "missing", "no_recent_posts", "unavailable", "protected", "suspended"]
    """`listed` means search shows its posts & `missing` means it shows none.

    `no_recent_posts` means the account has no recent post to look for.
    """

    evidence: Optional[ChecksSearchEvidence]
    """The search & the posts it looked for."""


class ChecksSuggestionEvidence(BaseModel):
    """The username searched & the accounts X suggested."""

    query: str
    """The username it typed."""

    suggested_usernames: List[str] = FieldInfo(alias="suggestedUsernames")
    """Up to 10 accounts X suggested, in its order."""


class ChecksSuggestion(BaseModel):
    """Looks for the account among the accounts X suggests for its username.

    `suggested` passes & `not_suggested` fails.
    """

    verdict: ShadowbanVerdict
    """Pass means X shows the account there, and fail means it doesn't.

    Unknown means the check had nothing to test or X didn't answer.
    """

    reason: Literal["suggested", "not_suggested", "unavailable", "suspended"]
    """`suggested` means X suggests the account for its username."""

    evidence: Optional[ChecksSuggestionEvidence]
    """The username searched & the accounts X suggested."""


class ChecksRepliesEvidenceReply(BaseModel):
    reply_id: str = FieldInfo(alias="replyId")
    """ID of the reply."""

    reply_url: str = FieldInfo(alias="replyUrl")
    """The reply on X."""

    parent_id: str = FieldInfo(alias="parentId")
    """ID of the post it replies to."""

    parent_url: str = FieldInfo(alias="parentUrl")
    """The thread of that post on X."""

    placement: Literal["thread", "more_replies", "not_found"]
    """`thread` means the reply shows in the thread.

    `more_replies` means it shows only behind X's hidden replies prompt.
    """


class ChecksRepliesEvidence(BaseModel):
    """Each reply it opened & where it showed."""

    replies: List[ChecksRepliesEvidenceReply]
    """Up to 3 replies, newest first."""


class ChecksReplies(BaseModel):
    """Opens the threads of up to 3 recent replies to other accounts.

    `in_thread` passes. X ranks replies for each viewer, so `more_replies` can't
    tell.
    """

    verdict: ShadowbanVerdict
    """Pass means X shows the account there, and fail means it doesn't.

    Unknown means the check had nothing to test or X didn't answer.
    """

    reason: Literal[
        "in_thread", "more_replies", "no_recent_replies", "not_found", "unavailable", "protected", "suspended"
    ]
    """`more_replies` means X put a reply behind its hidden replies prompt.

    `not_found` means no reply showed on the pages the check read.
    """

    evidence: Optional[ChecksRepliesEvidence]
    """Each reply it opened & where it showed."""


class Checks(BaseModel):
    """The 4 checks, each with a verdict, a reason & evidence."""

    account: ChecksAccount
    """Passes an active or protected account & fails a suspended one."""

    search: ChecksSearch
    """Looks for the account's recent posts in X search, sorted by Latest.

    `listed` passes & `missing` fails.
    """

    suggestion: ChecksSuggestion
    """Looks for the account among the accounts X suggests for its username.

    `suggested` passes & `not_suggested` fails.
    """

    replies: ChecksReplies
    """Opens the threads of up to 3 recent replies to other accounts.

    `in_thread` passes. X ranks replies for each viewer, so `more_replies` can't
    tell.
    """


class ShadowbanReport(BaseModel):
    """Says whether X limits 1 account in search, search suggestions or reply threads.

    Each check holds a verdict, its reason & the evidence it read. Evidence is null
    for a check that couldn't read the account.
    """

    username: Optional[str]
    """Username of the account. Null for a suspended account asked for by ID."""

    user_id: Optional[str] = FieldInfo(alias="userId")
    """ID of the account. Null for a suspended account asked for by username."""

    account: Literal["active", "protected", "suspended"]
    """Whether the account is active, protected or suspended."""

    checks: Checks
    """The 4 checks, each with a verdict, a reason & evidence."""
