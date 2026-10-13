# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TweetTranslateResponse",
    "Translation",
    "TranslationEntities",
    "TranslationEntitiesHashtag",
    "TranslationEntitiesHashtagTag",
    "TranslationEntitiesHashtagTagInfo",
    "TranslationEntitiesHashtagTagInfoInfo",
    "TranslationEntitiesSmarttag",
    "TranslationEntitiesSmarttagTag",
    "TranslationEntitiesSmarttagTagInfo",
    "TranslationEntitiesSmarttagTagInfoInfo",
    "TranslationEntitiesSymbol",
    "TranslationEntitiesSymbolTag",
    "TranslationEntitiesSymbolTagInfo",
    "TranslationEntitiesSymbolTagInfoInfo",
    "TranslationEntitiesTimestamp",
    "TranslationEntitiesTimestampTag",
    "TranslationEntitiesTimestampTagInfo",
    "TranslationEntitiesTimestampTagInfoInfo",
    "TranslationEntitiesURL",
    "TranslationEntitiesUserMention",
]


class TranslationEntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class TranslationEntitiesHashtagTagInfo(BaseModel):
    info: Optional[TranslationEntitiesHashtagTagInfoInfo] = None


class TranslationEntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[TranslationEntitiesHashtagTagInfo] = None


class TranslationEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[TranslationEntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class TranslationEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class TranslationEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[TranslationEntitiesSmarttagTagInfoInfo] = None


class TranslationEntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[TranslationEntitiesSmarttagTagInfo] = None


class TranslationEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[TranslationEntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class TranslationEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class TranslationEntitiesSymbolTagInfo(BaseModel):
    info: Optional[TranslationEntitiesSymbolTagInfoInfo] = None


class TranslationEntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[TranslationEntitiesSymbolTagInfo] = None


class TranslationEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[TranslationEntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class TranslationEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class TranslationEntitiesTimestampTagInfo(BaseModel):
    info: Optional[TranslationEntitiesTimestampTagInfoInfo] = None


class TranslationEntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[TranslationEntitiesTimestampTagInfo] = None


class TranslationEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[TranslationEntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class TranslationEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class TranslationEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class TranslationEntities(BaseModel):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[TranslationEntitiesHashtag]] = None

    smarttags: Optional[List[TranslationEntitiesSmarttag]] = None

    symbols: Optional[List[TranslationEntitiesSymbol]] = None

    timestamps: Optional[List[TranslationEntitiesTimestamp]] = None

    urls: Optional[List[TranslationEntitiesURL]] = None

    user_mentions: Optional[List[TranslationEntitiesUserMention]] = None


class Translation(BaseModel):
    """Holds X's translation of one tweet into the requested language.

    `entities` holds the links, mentions, and tags with their offsets in the translated text, and is empty when the text has none.
    """

    entities: TranslationEntities
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    language: str
    """Language code of the translated text, in lower case."""

    text: str
    """Translated tweet text."""

    tweet_id: str = FieldInfo(alias="tweetId")
    """ID of the translated tweet."""

    source_language: Optional[str] = FieldInfo(alias="sourceLanguage", default=None)
    """Language code X detects in the tweet, when it names one."""


class TweetTranslateResponse(BaseModel):
    translation: Translation
    """Holds X's translation of one tweet into the requested language.

    `entities` holds the links, mentions, and tags with their offsets in the
    translated text, and is empty when the text has none.
    """
