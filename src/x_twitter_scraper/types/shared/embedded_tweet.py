# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_media import TweetMedia
from .user_profile import UserProfile
from ..._dict_access import TweetEntitiesDictAccess
from .content_disclosure import ContentDisclosure

__all__ = [
    "EmbeddedTweet",
    "Article",
    "AuthorUnavailable",
    "Card",
    "CardUserReferenceError",
    "CashtagAttachment",
    "CommunityNote",
    "ConversationControl",
    "Coordinates",
    "Edit",
    "Entities",
    "EntitiesHashtag",
    "EntitiesHashtagTag",
    "EntitiesHashtagTagInfo",
    "EntitiesHashtagTagInfoInfo",
    "EntitiesSmarttag",
    "EntitiesSmarttagTag",
    "EntitiesSmarttagTagInfo",
    "EntitiesSmarttagTagInfoInfo",
    "EntitiesSymbol",
    "EntitiesSymbolTag",
    "EntitiesSymbolTagInfo",
    "EntitiesSymbolTagInfoInfo",
    "EntitiesTimestamp",
    "EntitiesTimestampTag",
    "EntitiesTimestampTagInfo",
    "EntitiesTimestampTagInfoInfo",
    "EntitiesURL",
    "EntitiesUserMention",
    "ExclusiveContent",
    "Geo",
    "Interstitial",
    "InterstitialText",
    "InterstitialTextEntity",
    "InterstitialTextEntityRef",
    "LimitedAction",
    "LimitedActionPrompt",
    "NoteTweet",
    "NoteTweetEntities",
    "NoteTweetEntitiesHashtag",
    "NoteTweetEntitiesHashtagTag",
    "NoteTweetEntitiesHashtagTagInfo",
    "NoteTweetEntitiesHashtagTagInfoInfo",
    "NoteTweetEntitiesSmarttag",
    "NoteTweetEntitiesSmarttagTag",
    "NoteTweetEntitiesSmarttagTagInfo",
    "NoteTweetEntitiesSmarttagTagInfoInfo",
    "NoteTweetEntitiesSymbol",
    "NoteTweetEntitiesSymbolTag",
    "NoteTweetEntitiesSymbolTagInfo",
    "NoteTweetEntitiesSymbolTagInfoInfo",
    "NoteTweetEntitiesTimestamp",
    "NoteTweetEntitiesTimestampTag",
    "NoteTweetEntitiesTimestampTagInfo",
    "NoteTweetEntitiesTimestampTagInfoInfo",
    "NoteTweetEntitiesURL",
    "NoteTweetEntitiesUserMention",
    "NoteTweetInlineMedia",
    "NoteTweetRichtextTag",
    "Place",
    "PreviousCounts",
    "QuotedTweet",
    "QuotedTweetArticle",
    "QuotedTweetCard",
    "QuotedTweetCardUserReferenceError",
    "QuotedTweetCommunityNote",
    "QuotedTweetConversationControl",
    "QuotedTweetEdit",
    "QuotedTweetEntities",
    "QuotedTweetEntitiesHashtag",
    "QuotedTweetEntitiesSmarttag",
    "QuotedTweetEntitiesSmarttagTag",
    "QuotedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetEntitiesSymbol",
    "QuotedTweetEntitiesSymbolTag",
    "QuotedTweetEntitiesSymbolTagInfo",
    "QuotedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetEntitiesTimestamp",
    "QuotedTweetEntitiesTimestampTag",
    "QuotedTweetEntitiesTimestampTagInfo",
    "QuotedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetEntitiesURL",
    "QuotedTweetEntitiesUserMention",
    "QuotedTweetLimitedAction",
    "QuotedTweetLimitedActionPrompt",
    "QuotedTweetNoteTweet",
    "QuotedTweetNoteTweetEntities",
    "QuotedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetNoteTweetEntitiesURL",
    "QuotedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetNoteTweetInlineMedia",
    "QuotedTweetNoteTweetRichtextTag",
    "QuotedTweetPermalink",
    "QuotedTweetPlace",
    "QuotedTweetPreviousCounts",
    "QuotedTweetQuotedTweet",
    "QuotedTweetQuotedTweetArticle",
    "QuotedTweetQuotedTweetCard",
    "QuotedTweetQuotedTweetCardUserReferenceError",
    "QuotedTweetQuotedTweetCommunityNote",
    "QuotedTweetQuotedTweetConversationControl",
    "QuotedTweetQuotedTweetEdit",
    "QuotedTweetQuotedTweetEntities",
    "QuotedTweetQuotedTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetEntitiesURL",
    "QuotedTweetQuotedTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetLimitedAction",
    "QuotedTweetQuotedTweetLimitedActionPrompt",
    "QuotedTweetQuotedTweetNoteTweet",
    "QuotedTweetQuotedTweetNoteTweetEntities",
    "QuotedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetNoteTweetEntitiesURL",
    "QuotedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetNoteTweetInlineMedia",
    "QuotedTweetQuotedTweetNoteTweetRichtextTag",
    "QuotedTweetQuotedTweetPlace",
    "QuotedTweetQuotedTweetPreviousCounts",
    "QuotedTweetQuotedTweetQuotedTweet",
    "QuotedTweetQuotedTweetQuotedTweetArticle",
    "QuotedTweetQuotedTweetQuotedTweetCard",
    "QuotedTweetQuotedTweetQuotedTweetCardUserReferenceError",
    "QuotedTweetQuotedTweetQuotedTweetCommunityNote",
    "QuotedTweetQuotedTweetQuotedTweetConversationControl",
    "QuotedTweetQuotedTweetQuotedTweetEdit",
    "QuotedTweetQuotedTweetQuotedTweetEntities",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesURL",
    "QuotedTweetQuotedTweetQuotedTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetQuotedTweetLimitedAction",
    "QuotedTweetQuotedTweetQuotedTweetLimitedActionPrompt",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweet",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntities",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia",
    "QuotedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag",
    "QuotedTweetQuotedTweetQuotedTweetPlace",
    "QuotedTweetQuotedTweetQuotedTweetPreviousCounts",
    "QuotedTweetQuotedTweetQuotedTweetReactionContext",
    "QuotedTweetQuotedTweetQuotedTweetSportsContext",
    "QuotedTweetQuotedTweetQuotedTweetSportsContextCompetitor",
    "QuotedTweetQuotedTweetQuotedTweetTombstone",
    "QuotedTweetQuotedTweetQuotedTweetTombstoneText",
    "QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntity",
    "QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef",
    "QuotedTweetQuotedTweetReactionContext",
    "QuotedTweetQuotedTweetRetweetedTweet",
    "QuotedTweetQuotedTweetRetweetedTweetArticle",
    "QuotedTweetQuotedTweetRetweetedTweetCard",
    "QuotedTweetQuotedTweetRetweetedTweetCardUserReferenceError",
    "QuotedTweetQuotedTweetRetweetedTweetCommunityNote",
    "QuotedTweetQuotedTweetRetweetedTweetConversationControl",
    "QuotedTweetQuotedTweetRetweetedTweetEdit",
    "QuotedTweetQuotedTweetRetweetedTweetEntities",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesURL",
    "QuotedTweetQuotedTweetRetweetedTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetRetweetedTweetLimitedAction",
    "QuotedTweetQuotedTweetRetweetedTweetLimitedActionPrompt",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweet",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntities",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia",
    "QuotedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag",
    "QuotedTweetQuotedTweetRetweetedTweetPlace",
    "QuotedTweetQuotedTweetRetweetedTweetPreviousCounts",
    "QuotedTweetQuotedTweetRetweetedTweetReactionContext",
    "QuotedTweetQuotedTweetRetweetedTweetSportsContext",
    "QuotedTweetQuotedTweetRetweetedTweetSportsContextCompetitor",
    "QuotedTweetQuotedTweetRetweetedTweetTombstone",
    "QuotedTweetQuotedTweetRetweetedTweetTombstoneText",
    "QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntity",
    "QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef",
    "QuotedTweetQuotedTweetSportsContext",
    "QuotedTweetQuotedTweetSportsContextCompetitor",
    "QuotedTweetQuotedTweetTombstone",
    "QuotedTweetQuotedTweetTombstoneText",
    "QuotedTweetQuotedTweetTombstoneTextEntity",
    "QuotedTweetQuotedTweetTombstoneTextEntityRef",
    "QuotedTweetReactionContext",
    "QuotedTweetRetweetedTweet",
    "QuotedTweetRetweetedTweetArticle",
    "QuotedTweetRetweetedTweetCard",
    "QuotedTweetRetweetedTweetCardUserReferenceError",
    "QuotedTweetRetweetedTweetCommunityNote",
    "QuotedTweetRetweetedTweetConversationControl",
    "QuotedTweetRetweetedTweetEdit",
    "QuotedTweetRetweetedTweetEntities",
    "QuotedTweetRetweetedTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetEntitiesURL",
    "QuotedTweetRetweetedTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetLimitedAction",
    "QuotedTweetRetweetedTweetLimitedActionPrompt",
    "QuotedTweetRetweetedTweetNoteTweet",
    "QuotedTweetRetweetedTweetNoteTweetEntities",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesURL",
    "QuotedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetNoteTweetInlineMedia",
    "QuotedTweetRetweetedTweetNoteTweetRichtextTag",
    "QuotedTweetRetweetedTweetPlace",
    "QuotedTweetRetweetedTweetPreviousCounts",
    "QuotedTweetRetweetedTweetQuotedTweet",
    "QuotedTweetRetweetedTweetQuotedTweetArticle",
    "QuotedTweetRetweetedTweetQuotedTweetCard",
    "QuotedTweetRetweetedTweetQuotedTweetCardUserReferenceError",
    "QuotedTweetRetweetedTweetQuotedTweetCommunityNote",
    "QuotedTweetRetweetedTweetQuotedTweetConversationControl",
    "QuotedTweetRetweetedTweetQuotedTweetEdit",
    "QuotedTweetRetweetedTweetQuotedTweetEntities",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesURL",
    "QuotedTweetRetweetedTweetQuotedTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetQuotedTweetLimitedAction",
    "QuotedTweetRetweetedTweetQuotedTweetLimitedActionPrompt",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweet",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntities",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia",
    "QuotedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag",
    "QuotedTweetRetweetedTweetQuotedTweetPlace",
    "QuotedTweetRetweetedTweetQuotedTweetPreviousCounts",
    "QuotedTweetRetweetedTweetQuotedTweetReactionContext",
    "QuotedTweetRetweetedTweetQuotedTweetSportsContext",
    "QuotedTweetRetweetedTweetQuotedTweetSportsContextCompetitor",
    "QuotedTweetRetweetedTweetQuotedTweetTombstone",
    "QuotedTweetRetweetedTweetQuotedTweetTombstoneText",
    "QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntity",
    "QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef",
    "QuotedTweetRetweetedTweetReactionContext",
    "QuotedTweetRetweetedTweetRetweetedTweet",
    "QuotedTweetRetweetedTweetRetweetedTweetArticle",
    "QuotedTweetRetweetedTweetRetweetedTweetCard",
    "QuotedTweetRetweetedTweetRetweetedTweetCardUserReferenceError",
    "QuotedTweetRetweetedTweetRetweetedTweetCommunityNote",
    "QuotedTweetRetweetedTweetRetweetedTweetConversationControl",
    "QuotedTweetRetweetedTweetRetweetedTweetEdit",
    "QuotedTweetRetweetedTweetRetweetedTweetEntities",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesURL",
    "QuotedTweetRetweetedTweetRetweetedTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetRetweetedTweetLimitedAction",
    "QuotedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweet",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntities",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia",
    "QuotedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag",
    "QuotedTweetRetweetedTweetRetweetedTweetPlace",
    "QuotedTweetRetweetedTweetRetweetedTweetPreviousCounts",
    "QuotedTweetRetweetedTweetRetweetedTweetReactionContext",
    "QuotedTweetRetweetedTweetRetweetedTweetSportsContext",
    "QuotedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor",
    "QuotedTweetRetweetedTweetRetweetedTweetTombstone",
    "QuotedTweetRetweetedTweetRetweetedTweetTombstoneText",
    "QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity",
    "QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef",
    "QuotedTweetRetweetedTweetSportsContext",
    "QuotedTweetRetweetedTweetSportsContextCompetitor",
    "QuotedTweetRetweetedTweetTombstone",
    "QuotedTweetRetweetedTweetTombstoneText",
    "QuotedTweetRetweetedTweetTombstoneTextEntity",
    "QuotedTweetRetweetedTweetTombstoneTextEntityRef",
    "QuotedTweetSportsContext",
    "QuotedTweetSportsContextCompetitor",
    "QuotedTweetTombstone",
    "QuotedTweetTombstoneText",
    "QuotedTweetTombstoneTextEntity",
    "QuotedTweetTombstoneTextEntityRef",
    "QuotedTweetUnavailable",
    "ReactionContext",
    "RetweetedTweet",
    "RetweetedTweetArticle",
    "RetweetedTweetCard",
    "RetweetedTweetCardUserReferenceError",
    "RetweetedTweetCommunityNote",
    "RetweetedTweetConversationControl",
    "RetweetedTweetEdit",
    "RetweetedTweetEntities",
    "RetweetedTweetEntitiesHashtag",
    "RetweetedTweetEntitiesSmarttag",
    "RetweetedTweetEntitiesSmarttagTag",
    "RetweetedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetEntitiesSymbol",
    "RetweetedTweetEntitiesSymbolTag",
    "RetweetedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetEntitiesTimestamp",
    "RetweetedTweetEntitiesTimestampTag",
    "RetweetedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetEntitiesURL",
    "RetweetedTweetEntitiesUserMention",
    "RetweetedTweetLimitedAction",
    "RetweetedTweetLimitedActionPrompt",
    "RetweetedTweetNoteTweet",
    "RetweetedTweetNoteTweetEntities",
    "RetweetedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetNoteTweetEntitiesURL",
    "RetweetedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetNoteTweetInlineMedia",
    "RetweetedTweetNoteTweetRichtextTag",
    "RetweetedTweetPlace",
    "RetweetedTweetPreviousCounts",
    "RetweetedTweetQuotedTweet",
    "RetweetedTweetQuotedTweetArticle",
    "RetweetedTweetQuotedTweetCard",
    "RetweetedTweetQuotedTweetCardUserReferenceError",
    "RetweetedTweetQuotedTweetCommunityNote",
    "RetweetedTweetQuotedTweetConversationControl",
    "RetweetedTweetQuotedTweetEdit",
    "RetweetedTweetQuotedTweetEntities",
    "RetweetedTweetQuotedTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetEntitiesURL",
    "RetweetedTweetQuotedTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetLimitedAction",
    "RetweetedTweetQuotedTweetLimitedActionPrompt",
    "RetweetedTweetQuotedTweetNoteTweet",
    "RetweetedTweetQuotedTweetNoteTweetEntities",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesURL",
    "RetweetedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetNoteTweetInlineMedia",
    "RetweetedTweetQuotedTweetNoteTweetRichtextTag",
    "RetweetedTweetQuotedTweetPlace",
    "RetweetedTweetQuotedTweetPreviousCounts",
    "RetweetedTweetQuotedTweetQuotedTweet",
    "RetweetedTweetQuotedTweetQuotedTweetArticle",
    "RetweetedTweetQuotedTweetQuotedTweetCard",
    "RetweetedTweetQuotedTweetQuotedTweetCardUserReferenceError",
    "RetweetedTweetQuotedTweetQuotedTweetCommunityNote",
    "RetweetedTweetQuotedTweetQuotedTweetConversationControl",
    "RetweetedTweetQuotedTweetQuotedTweetEdit",
    "RetweetedTweetQuotedTweetQuotedTweetEntities",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesURL",
    "RetweetedTweetQuotedTweetQuotedTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetQuotedTweetLimitedAction",
    "RetweetedTweetQuotedTweetQuotedTweetLimitedActionPrompt",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweet",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntities",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia",
    "RetweetedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag",
    "RetweetedTweetQuotedTweetQuotedTweetPlace",
    "RetweetedTweetQuotedTweetQuotedTweetPreviousCounts",
    "RetweetedTweetQuotedTweetQuotedTweetReactionContext",
    "RetweetedTweetQuotedTweetQuotedTweetSportsContext",
    "RetweetedTweetQuotedTweetQuotedTweetSportsContextCompetitor",
    "RetweetedTweetQuotedTweetQuotedTweetTombstone",
    "RetweetedTweetQuotedTweetQuotedTweetTombstoneText",
    "RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntity",
    "RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef",
    "RetweetedTweetQuotedTweetReactionContext",
    "RetweetedTweetQuotedTweetRetweetedTweet",
    "RetweetedTweetQuotedTweetRetweetedTweetArticle",
    "RetweetedTweetQuotedTweetRetweetedTweetCard",
    "RetweetedTweetQuotedTweetRetweetedTweetCardUserReferenceError",
    "RetweetedTweetQuotedTweetRetweetedTweetCommunityNote",
    "RetweetedTweetQuotedTweetRetweetedTweetConversationControl",
    "RetweetedTweetQuotedTweetRetweetedTweetEdit",
    "RetweetedTweetQuotedTweetRetweetedTweetEntities",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesURL",
    "RetweetedTweetQuotedTweetRetweetedTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetRetweetedTweetLimitedAction",
    "RetweetedTweetQuotedTweetRetweetedTweetLimitedActionPrompt",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweet",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntities",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia",
    "RetweetedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag",
    "RetweetedTweetQuotedTweetRetweetedTweetPlace",
    "RetweetedTweetQuotedTweetRetweetedTweetPreviousCounts",
    "RetweetedTweetQuotedTweetRetweetedTweetReactionContext",
    "RetweetedTweetQuotedTweetRetweetedTweetSportsContext",
    "RetweetedTweetQuotedTweetRetweetedTweetSportsContextCompetitor",
    "RetweetedTweetQuotedTweetRetweetedTweetTombstone",
    "RetweetedTweetQuotedTweetRetweetedTweetTombstoneText",
    "RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntity",
    "RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef",
    "RetweetedTweetQuotedTweetSportsContext",
    "RetweetedTweetQuotedTweetSportsContextCompetitor",
    "RetweetedTweetQuotedTweetTombstone",
    "RetweetedTweetQuotedTweetTombstoneText",
    "RetweetedTweetQuotedTweetTombstoneTextEntity",
    "RetweetedTweetQuotedTweetTombstoneTextEntityRef",
    "RetweetedTweetReactionContext",
    "RetweetedTweetRetweetedTweet",
    "RetweetedTweetRetweetedTweetArticle",
    "RetweetedTweetRetweetedTweetCard",
    "RetweetedTweetRetweetedTweetCardUserReferenceError",
    "RetweetedTweetRetweetedTweetCommunityNote",
    "RetweetedTweetRetweetedTweetConversationControl",
    "RetweetedTweetRetweetedTweetEdit",
    "RetweetedTweetRetweetedTweetEntities",
    "RetweetedTweetRetweetedTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetLimitedAction",
    "RetweetedTweetRetweetedTweetLimitedActionPrompt",
    "RetweetedTweetRetweetedTweetNoteTweet",
    "RetweetedTweetRetweetedTweetNoteTweetEntities",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetNoteTweetInlineMedia",
    "RetweetedTweetRetweetedTweetNoteTweetRichtextTag",
    "RetweetedTweetRetweetedTweetPlace",
    "RetweetedTweetRetweetedTweetPreviousCounts",
    "RetweetedTweetRetweetedTweetQuotedTweet",
    "RetweetedTweetRetweetedTweetQuotedTweetArticle",
    "RetweetedTweetRetweetedTweetQuotedTweetCard",
    "RetweetedTweetRetweetedTweetQuotedTweetCardUserReferenceError",
    "RetweetedTweetRetweetedTweetQuotedTweetCommunityNote",
    "RetweetedTweetRetweetedTweetQuotedTweetConversationControl",
    "RetweetedTweetRetweetedTweetQuotedTweetEdit",
    "RetweetedTweetRetweetedTweetQuotedTweetEntities",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetQuotedTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetQuotedTweetLimitedAction",
    "RetweetedTweetRetweetedTweetQuotedTweetLimitedActionPrompt",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweet",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntities",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia",
    "RetweetedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag",
    "RetweetedTweetRetweetedTweetQuotedTweetPlace",
    "RetweetedTweetRetweetedTweetQuotedTweetPreviousCounts",
    "RetweetedTweetRetweetedTweetQuotedTweetReactionContext",
    "RetweetedTweetRetweetedTweetQuotedTweetSportsContext",
    "RetweetedTweetRetweetedTweetQuotedTweetSportsContextCompetitor",
    "RetweetedTweetRetweetedTweetQuotedTweetTombstone",
    "RetweetedTweetRetweetedTweetQuotedTweetTombstoneText",
    "RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntity",
    "RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef",
    "RetweetedTweetRetweetedTweetReactionContext",
    "RetweetedTweetRetweetedTweetRetweetedTweet",
    "RetweetedTweetRetweetedTweetRetweetedTweetArticle",
    "RetweetedTweetRetweetedTweetRetweetedTweetCard",
    "RetweetedTweetRetweetedTweetRetweetedTweetCardUserReferenceError",
    "RetweetedTweetRetweetedTweetRetweetedTweetCommunityNote",
    "RetweetedTweetRetweetedTweetRetweetedTweetConversationControl",
    "RetweetedTweetRetweetedTweetRetweetedTweetEdit",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntities",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetRetweetedTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetRetweetedTweetLimitedAction",
    "RetweetedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweet",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntities",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia",
    "RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag",
    "RetweetedTweetRetweetedTweetRetweetedTweetPlace",
    "RetweetedTweetRetweetedTweetRetweetedTweetPreviousCounts",
    "RetweetedTweetRetweetedTweetRetweetedTweetReactionContext",
    "RetweetedTweetRetweetedTweetRetweetedTweetSportsContext",
    "RetweetedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor",
    "RetweetedTweetRetweetedTweetRetweetedTweetTombstone",
    "RetweetedTweetRetweetedTweetRetweetedTweetTombstoneText",
    "RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity",
    "RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef",
    "RetweetedTweetRetweetedTweetSportsContext",
    "RetweetedTweetRetweetedTweetSportsContextCompetitor",
    "RetweetedTweetRetweetedTweetTombstone",
    "RetweetedTweetRetweetedTweetTombstoneText",
    "RetweetedTweetRetweetedTweetTombstoneTextEntity",
    "RetweetedTweetRetweetedTweetTombstoneTextEntityRef",
    "RetweetedTweetSportsContext",
    "RetweetedTweetSportsContextCompetitor",
    "RetweetedTweetTombstone",
    "RetweetedTweetTombstoneText",
    "RetweetedTweetTombstoneTextEntity",
    "RetweetedTweetTombstoneTextEntityRef",
    "SportsContext",
    "SportsContextCompetitor",
    "SubscriberBadge",
    "TextHighlight",
    "Tombstone",
    "TombstoneText",
    "TombstoneTextEntity",
    "TombstoneTextEntityRef",
]


class Article(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class AuthorUnavailable(BaseModel):
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason such as Suspended or NotFound. Omitted when the author is available.
    """

    reason: str
    """X's reason code."""

    message: Optional[str] = None
    """X's notice text for the reason."""


class CardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class Card(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[CardUserReferenceError]] = FieldInfo(alias="userReferenceErrors", default=None)
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class CashtagAttachment(BaseModel):
    cashtag: str
    """The cashtag with its `$`."""

    candle_size: Optional[str] = FieldInfo(alias="candleSize", default=None)
    """Span of each candle."""

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """Time of the chart's last price."""

    size_variant: Optional[int] = FieldInfo(alias="sizeVariant", default=None)
    """X's size for the chart."""

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
    """Time of the chart's first candle."""

    timeframe: Optional[str] = None
    """Span the chart covers."""


class CommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class ConversationControl(BaseModel):
    """Reply policy & conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)
    """Regions whose accounts may reply, as country codes.

    Sent with the `country_of_origin` mode.
    """

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None
    """
    Reply policy from X's newer field, such as `my_network`, `premium` or
    `country_of_origin`. Omitted when X sends none.
    """

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)
    """The conversation owner's account ID."""

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class Coordinates(BaseModel):
    """Author-published point, with longitude before latitude."""

    coordinates: List[float]

    type: Literal["Point"]


class Edit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class EntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesHashtagTagInfo(BaseModel):
    info: Optional[EntitiesHashtagTagInfoInfo] = None


class EntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesHashtagTagInfo] = None


class EntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class EntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSmarttagTagInfo(BaseModel):
    info: Optional[EntitiesSmarttagTagInfoInfo] = None


class EntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesSmarttagTagInfo] = None


class EntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class EntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSymbolTagInfo(BaseModel):
    info: Optional[EntitiesSymbolTagInfoInfo] = None


class EntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesSymbolTagInfo] = None


class EntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class EntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesTimestampTagInfo(BaseModel):
    info: Optional[EntitiesTimestampTagInfoInfo] = None


class EntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesTimestampTagInfo] = None


class EntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class EntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class EntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class Entities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[EntitiesHashtag]] = None

    smarttags: Optional[List[EntitiesSmarttag]] = None

    symbols: Optional[List[EntitiesSymbol]] = None

    timestamps: Optional[List[EntitiesTimestamp]] = None

    urls: Optional[List[EntitiesURL]] = None

    user_mentions: Optional[List[EntitiesUserMention]] = None


class ExclusiveContent(BaseModel):
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public posts.
    """

    creator_user_name: str = FieldInfo(alias="creatorUserName")
    """Username of the creator whose subscription unlocks the post."""

    subscribe_url: Optional[str] = FieldInfo(alias="subscribeUrl", default=None)
    """Subscribe link X shows non-subscribers. Omitted when X serves the full post."""


class Geo(BaseModel):
    """Author-published point, with latitude before longitude."""

    coordinates: List[float]

    type: Literal["Point"]


class InterstitialTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class InterstitialTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[InterstitialTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class InterstitialText(BaseModel):
    entities: Optional[List[InterstitialTextEntity]] = None
    """Links inside the notice, by character range."""

    rtl: Optional[bool] = None
    """Whether X writes it right to left."""

    text: Optional[str] = None
    """The notice's text."""


class Interstitial(BaseModel):
    """
    The notice x.com covers the post with until the reader views it, such as X's public interest notice on a post that broke its rules but stays up.
    """

    display_type: Optional[str] = FieldInfo(alias="displayType", default=None)
    """How x.com shows the notice. `NonCompliant` marks a post that broke X's rules."""

    text: Optional[InterstitialText] = None


class LimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class LimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[LimitedActionPrompt] = None


class NoteTweetEntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesHashtagTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesHashtagTagInfoInfo] = None


class NoteTweetEntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesHashtagTagInfo] = None


class NoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class NoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSmarttagTagInfoInfo] = None


class NoteTweetEntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesSmarttagTagInfo] = None


class NoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSymbolTagInfoInfo] = None


class NoteTweetEntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesSymbolTagInfo] = None


class NoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesTimestampTagInfoInfo] = None


class NoteTweetEntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesTimestampTagInfo] = None


class NoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class NoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class NoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class NoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[NoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[NoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[NoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[NoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[NoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[NoteTweetEntitiesUserMention]] = None


class NoteTweetInlineMedia(BaseModel):
    index: int
    """Whole number from 0."""

    media_id: str = FieldInfo(alias="mediaId")


class NoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")
    """Whole number from 0."""

    to_index: int = FieldInfo(alias="toIndex")
    """Whole number from 0."""

    types: List[str]


class NoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None
    """X's global ID of the Note, base64 of `NoteTweet:<noteId>`."""

    entities: Optional[NoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[NoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)
    """The Note's own ID, apart from the post's."""

    richtext_tags: Optional[List[NoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class Place(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class PreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)
    """Whole number from 0."""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)
    """Whole number from 0."""

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)
    """Whole number from 0."""

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)
    """Whole number from 0."""

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)
    """Whole number from 0."""


class QuotedTweetPermalink(BaseModel):
    """The quoted post's link, kept when X withholds that post."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)

    expanded_url: Optional[str] = FieldInfo(alias="expandedUrl", default=None)

    url: Optional[str] = None


class QuotedTweetUnavailable(BaseModel):
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reason: str
    """
    X's reason, such as `Suspended` for a suspended author or `Protected` for an
    author who protects their posts.
    """


class SubscriberBadge(BaseModel):
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation. Omitted on a post without the badge.
    """

    creator_id: str = FieldInfo(alias="creatorId")
    """Account ID of the creator the author subscribes to."""


class TextHighlight(BaseModel):
    end_index: int = FieldInfo(alias="endIndex")
    """The first code point after the match."""

    start_index: int = FieldInfo(alias="startIndex")
    """The first code point of the match."""


class QuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetEntitiesUserMention]] = None


class QuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetLimitedActionPrompt] = None


class QuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetNoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetNoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class QuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetQuotedTweetLimitedActionPrompt] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetQuotedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetQuotedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetQuotedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetQuotedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetQuotedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetQuotedTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetQuotedTweetQuotedTweetLimitedActionPrompt] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetQuotedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetQuotedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetQuotedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetQuotedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetQuotedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetQuotedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetQuotedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetQuotedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetQuotedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetQuotedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetQuotedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetQuotedTweetQuotedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetQuotedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetQuotedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetQuotedTweetQuotedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetQuotedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetQuotedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetQuotedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetQuotedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetQuotedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[QuotedTweetQuotedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetQuotedTweetQuotedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetQuotedTweetQuotedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetQuotedTweetQuotedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetQuotedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetQuotedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetQuotedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetQuotedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetQuotedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetQuotedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetRetweetedTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetQuotedTweetRetweetedTweetLimitedActionPrompt] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetQuotedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetQuotedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetQuotedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetQuotedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetQuotedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetQuotedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetQuotedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetQuotedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetQuotedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetQuotedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetQuotedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetQuotedTweetRetweetedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetQuotedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetQuotedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetQuotedTweetRetweetedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetQuotedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetQuotedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetQuotedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetQuotedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetQuotedTweetRetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[QuotedTweetQuotedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetQuotedTweetRetweetedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetQuotedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetQuotedTweetRetweetedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetQuotedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetQuotedTweet(BaseModel):
    """Nested tweet context at depth 3."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetQuotedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[QuotedTweetQuotedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[QuotedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetQuotedTweetPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[QuotedTweetQuotedTweetQuotedTweet] = None
    """Final nested tweet context at depth 4."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetQuotedTweetReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[QuotedTweetQuotedTweetRetweetedTweet] = None
    """Final nested tweet context at depth 4."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetQuotedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetRetweetedTweetLimitedActionPrompt] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetRetweetedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetRetweetedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetRetweetedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetRetweetedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetRetweetedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetQuotedTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetRetweetedTweetQuotedTweetLimitedActionPrompt] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetRetweetedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetRetweetedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetRetweetedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetRetweetedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetRetweetedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetRetweetedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetRetweetedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetRetweetedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetRetweetedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetRetweetedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetRetweetedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetRetweetedTweetQuotedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetRetweetedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetRetweetedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetRetweetedTweetQuotedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetRetweetedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetRetweetedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetRetweetedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetRetweetedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetRetweetedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[QuotedTweetRetweetedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetRetweetedTweetQuotedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetRetweetedTweetQuotedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetRetweetedTweetQuotedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetRetweetedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetRetweetedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[QuotedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class QuotedTweetRetweetedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class QuotedTweetRetweetedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class QuotedTweetRetweetedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class QuotedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetRetweetedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetRetweetedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetRetweetedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetRetweetedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetRetweetedTweetRetweetedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetRetweetedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetRetweetedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetRetweetedTweetRetweetedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetRetweetedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetRetweetedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetRetweetedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetRetweetedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetRetweetedTweetRetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[QuotedTweetRetweetedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetRetweetedTweetRetweetedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetRetweetedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetRetweetedTweetRetweetedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetRetweetedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweetRetweetedTweet(BaseModel):
    """Nested tweet context at depth 3."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetRetweetedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetRetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[QuotedTweetRetweetedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[QuotedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetRetweetedTweetPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[QuotedTweetRetweetedTweetQuotedTweet] = None
    """Final nested tweet context at depth 4."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[QuotedTweetRetweetedTweetRetweetedTweet] = None
    """Final nested tweet context at depth 4."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetRetweetedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class QuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class QuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[QuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class QuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class QuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[QuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class QuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[QuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class QuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[QuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class QuotedTweet(BaseModel):
    """Nested tweet context at depth 2."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[QuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[QuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[QuotedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[QuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[QuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[QuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[QuotedTweetLimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[QuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[QuotedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[QuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[QuotedTweetPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[QuotedTweetQuotedTweet] = None
    """Nested tweet context at depth 3."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[QuotedTweetReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[QuotedTweetRetweetedTweet] = None
    """Nested tweet context at depth 3."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[QuotedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[QuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class ReactionContext(BaseModel):
    """Public post & user this reaction references."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetEntitiesUserMention]] = None


class RetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetLimitedActionPrompt] = None


class RetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetNoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetNoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class RetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetQuotedTweetLimitedActionPrompt] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetQuotedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetQuotedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetQuotedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetQuotedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetQuotedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetQuotedTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetQuotedTweetQuotedTweetLimitedActionPrompt] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetQuotedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetQuotedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetQuotedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetQuotedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetQuotedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetQuotedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetQuotedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetQuotedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetQuotedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetQuotedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetQuotedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetQuotedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetQuotedTweetQuotedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetQuotedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetQuotedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetQuotedTweetQuotedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetQuotedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetQuotedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetQuotedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetQuotedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetQuotedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[RetweetedTweetQuotedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetQuotedTweetQuotedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetQuotedTweetQuotedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetQuotedTweetQuotedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetQuotedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetQuotedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetQuotedTweetRetweetedTweetLimitedActionPrompt] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetQuotedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetQuotedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetQuotedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetQuotedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetQuotedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetQuotedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetQuotedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetQuotedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetQuotedTweetRetweetedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetQuotedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetQuotedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetQuotedTweetRetweetedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetQuotedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetQuotedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetQuotedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetQuotedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetQuotedTweetRetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[RetweetedTweetQuotedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetQuotedTweetRetweetedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetQuotedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetQuotedTweetRetweetedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetQuotedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetQuotedTweet(BaseModel):
    """Nested tweet context at depth 3."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetQuotedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[RetweetedTweetQuotedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[RetweetedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetQuotedTweetPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[RetweetedTweetQuotedTweetQuotedTweet] = None
    """Final nested tweet context at depth 4."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetQuotedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[RetweetedTweetQuotedTweetRetweetedTweet] = None
    """Final nested tweet context at depth 4."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetQuotedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetRetweetedTweetLimitedActionPrompt] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetQuotedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetRetweetedTweetQuotedTweetLimitedActionPrompt] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetRetweetedTweetQuotedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetRetweetedTweetQuotedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetQuotedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetRetweetedTweetQuotedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetRetweetedTweetQuotedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetRetweetedTweetQuotedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetRetweetedTweetQuotedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetRetweetedTweetQuotedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetRetweetedTweetQuotedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetRetweetedTweetQuotedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetRetweetedTweetQuotedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetRetweetedTweetQuotedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetRetweetedTweetQuotedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetRetweetedTweetQuotedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetRetweetedTweetQuotedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetRetweetedTweetQuotedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetRetweetedTweetQuotedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[RetweetedTweetRetweetedTweetQuotedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetRetweetedTweetQuotedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetRetweetedTweetQuotedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetRetweetedTweetQuotedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetRetweetedTweetQuotedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetRetweetedTweetRetweetedTweetArticle(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetCard(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetCommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[RetweetedTweetRetweetedTweetRetweetedTweetLimitedActionPrompt] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None

    name: Optional[str] = None

    ticker: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfoInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag(BaseModel):
    id: Optional[str] = None

    info: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTagInfo] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntitiesUserMention]] = None


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class RetweetedTweetRetweetedTweetRetweetedTweetNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetInlineMedia]] = FieldInfo(
        alias="inlineMedia", default=None
    )
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)

    richtext_tags: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweetRichtextTag]] = FieldInfo(
        alias="richtextTags", default=None
    )


class RetweetedTweetRetweetedTweetRetweetedTweetPlace(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class RetweetedTweetRetweetedTweetRetweetedTweetPreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class RetweetedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetRetweetedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetRetweetedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetRetweetedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetRetweetedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetRetweetedTweetRetweetedTweet(BaseModel):
    """Final nested tweet context at depth 4."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetRetweetedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetRetweetedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetRetweetedTweetRetweetedTweetCommunityNote] = FieldInfo(
        alias="communityNote", default=None
    )
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetRetweetedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetRetweetedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetRetweetedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetRetweetedTweetRetweetedTweetNoteTweet] = FieldInfo(
        alias="noteTweet", default=None
    )
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[RetweetedTweetRetweetedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetRetweetedTweetRetweetedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetRetweetedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetRetweetedTweetRetweetedTweetSportsContext] = FieldInfo(
        alias="sportsContext", default=None
    )
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetRetweetedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetRetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetRetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetRetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetRetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetRetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetRetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetRetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetRetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetRetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetRetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweetRetweetedTweet(BaseModel):
    """Nested tweet context at depth 3."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetRetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetRetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetRetweetedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetRetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetRetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetRetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetRetweetedTweetLimitedAction]] = FieldInfo(
        alias="limitedActions", default=None
    )
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetRetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[RetweetedTweetRetweetedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[RetweetedTweetRetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetRetweetedTweetPreviousCounts] = FieldInfo(
        alias="previousCounts", default=None
    )
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[RetweetedTweetRetweetedTweetQuotedTweet] = None
    """Final nested tweet context at depth 4."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetRetweetedTweetReactionContext] = FieldInfo(
        alias="reactionContext", default=None
    )
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[RetweetedTweetRetweetedTweetRetweetedTweet] = None
    """Final nested tweet context at depth 4."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetRetweetedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetRetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class RetweetedTweetSportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class RetweetedTweetSportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[RetweetedTweetSportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class RetweetedTweetTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class RetweetedTweetTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[RetweetedTweetTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class RetweetedTweetTombstoneText(BaseModel):
    entities: Optional[List[RetweetedTweetTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class RetweetedTweetTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[RetweetedTweetTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class RetweetedTweet(BaseModel):
    """Nested tweet context at depth 2."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[RetweetedTweetArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)

    card: Optional[RetweetedTweetCard] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)

    community_note: Optional[RetweetedTweetCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[RetweetedTweetConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[RetweetedTweetEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[RetweetedTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)

    geo: Optional[Geo] = None

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[RetweetedTweetLimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[RetweetedTweetNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[RetweetedTweetQuotedTweet] = FieldInfo(alias="parentTweet", default=None)

    place: Optional[RetweetedTweetPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[RetweetedTweetPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[RetweetedTweetQuotedTweet] = None
    """Nested tweet context at depth 3."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)

    reaction_context: Optional[RetweetedTweetReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[RetweetedTweetRetweetedTweet] = None
    """Nested tweet context at depth 3."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[RetweetedTweetSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)

    tombstone: Optional[RetweetedTweetTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class SportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None
    """Team display color."""

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """Active competitor."""

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)
    """Winning competitor."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class SportsContext(BaseModel):
    """Game metadata attached to this post."""

    competitors: Optional[List[SportsContextCompetitor]] = None
    """Teams & reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None
    """League ID."""

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix milliseconds, retaining the source type."""

    state: Optional[str] = None
    """Reported game state."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Game progress text."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class TombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class TombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[TombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class TombstoneText(BaseModel):
    entities: Optional[List[TombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class Tombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[TombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class EmbeddedTweet(BaseModel):
    """A parent, quoted or retweeted tweet.

    It has the TweetPublicData fields and an author. Nesting stops after 4 levels.
    """

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[Article] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[UserProfile] = None
    """Public X profile."""

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason
    such as Suspended or NotFound. Omitted when the author is available.
    """

    card: Optional[Card] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)
    """Price charts the author attached under the post, 1 per cashtag.

    Absent when the post has none. X may send a cashtag without a chart window.
    """

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)
    """Community name. Present when X sends it with the post."""

    community_note: Optional[CommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[ConversationControl] = FieldInfo(alias="conversationControl", default=None)
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None
    """Author-published point, with longitude before latitude."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[Edit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[Entities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public
    posts.
    """

    geo: Optional[Geo] = None
    """Author-published point, with latitude before longitude."""

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)
    """Grok's translation of the post, as X shows it."""

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)
    """Whether X holds Community Notes on the post, shown or not."""

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None
    """
    The notice x.com covers the post with until the reader views it, such as X's
    public interest notice on a post that broke its rules but stays up.
    """

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[LimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[NoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[QuotedTweet] = FieldInfo(alias="parentTweet", default=None)
    """The post this one replies to, with the same fields."""

    place: Optional[Place] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[PreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[QuotedTweet] = None
    """Nested tweet context at depth 2."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)
    """The quoted post's link, kept when X withholds that post."""

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reaction_context: Optional[ReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[RetweetedTweet] = None
    """Nested tweet context at depth 2."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[SportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation.
    Omitted on a post without the badge.
    """

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)
    """Where `text` matches the search, on each row a search read.

    Offsets count code points of `text`, as `displayTextRange` does. Empty when X
    marks nothing in the post. X marks matches only in a post's first 280
    characters.
    """

    tombstone: Optional[Tombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)
    """The author's ID when X withholds the author's profile."""

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)

    if TYPE_CHECKING:
        # Pydantic <2.8 rejects a value on __pydantic_extra__ at runtime.
        # https://github.com/pydantic/pydantic/pull/9659
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
