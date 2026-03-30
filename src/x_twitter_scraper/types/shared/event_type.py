# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EventType"]

EventType: TypeAlias = Literal[
    "tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"
]
