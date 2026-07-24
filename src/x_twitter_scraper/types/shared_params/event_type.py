# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["EventType"]

EventType: TypeAlias = Literal[
    "tweet.new",
    "tweet.reply",
    "tweet.retweet",
    "tweet.quote",
    "tweet.media",
    "tweet.link",
    "tweet.poll",
    "tweet.mention",
    "tweet.hashtag",
    "tweet.longform",
    "profile.avatar.changed",
    "profile.banner.changed",
    "profile.name.changed",
    "profile.username.changed",
    "profile.bio.changed",
    "profile.location.changed",
    "profile.url.changed",
    "profile.verified.changed",
    "profile.protected.changed",
    "profile.pinned_tweet.changed",
    "profile.unavailable.changed",
]
