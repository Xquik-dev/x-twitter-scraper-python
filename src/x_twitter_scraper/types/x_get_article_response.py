# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "XGetArticleResponse",
    "Article",
    "ArticleContent",
    "ArticleContentInlineStyleRange",
    "ArticleContentLink",
    "ArticleContentVariant",
    "Author",
]


class ArticleContentInlineStyleRange(BaseModel):
    length: Optional[int] = None

    offset: Optional[int] = None

    style: Optional[str] = None
    """X's name for the style, such as Bold or Italic"""


class ArticleContentLink(BaseModel):
    length: Optional[int] = None

    offset: Optional[int] = None

    url: Optional[str] = None


class ArticleContentVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class ArticleContent(BaseModel):
    alt_text: Optional[str] = FieldInfo(alias="altText", default=None)
    """Alt text of the image or preview image"""

    caption: Optional[str] = None
    """Caption the author wrote under a media block"""

    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)
    """Length of a video, in milliseconds"""

    height: Optional[int] = None
    """Height of the image or preview image"""

    inline_style_ranges: Optional[List[ArticleContentInlineStyleRange]] = FieldInfo(
        alias="inlineStyleRanges", default=None
    )
    """Inline text formatting ranges"""

    links: Optional[List[ArticleContentLink]] = None
    """Links in the block's text, with the text range each covers"""

    media_type: Optional[Literal["image", "video", "gif"]] = FieldInfo(alias="mediaType", default=None)
    """What a media block holds"""

    preview_url: Optional[str] = FieldInfo(alias="previewUrl", default=None)
    """Image of a media block, or the preview image of a video or GIF"""

    text: Optional[str] = None

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
    """ID of the post a tweet block embeds"""

    type: Optional[str] = None
    """
    Block type: paragraph, header-one, header-two, header-three, header-four,
    header-five, header-six, unordered-list-item, ordered-list-item, blockquote,
    code-block, markdown, media, tweet, divider
    """

    url: Optional[str] = None
    """Image URL of an image block.

    A video or GIF block lists its files in `variants`.
    """

    variants: Optional[List[ArticleContentVariant]] = None
    """Files of a video or GIF block, in X's order"""

    width: Optional[int] = None
    """Width of the image or preview image"""


class Article(BaseModel):
    article_id: Optional[str] = FieldInfo(alias="articleId", default=None)
    """X's ID for the Article, which differs from its post's ID"""

    body_markdown: Optional[str] = FieldInfo(alias="bodyMarkdown", default=None)
    """
    Article blocks as Markdown, with headings, lists, bold, italic, links, images &
    embedded posts as their x.com URLs. Holds no HTML.
    """

    body_text: Optional[str] = FieldInfo(alias="bodyText", default=None)
    """Plain text joined from all article blocks"""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)
    """Accounts that bookmarked the Article's post. 0 or more."""

    contents: Optional[List[ArticleContent]] = None

    cover_image_url: Optional[str] = FieldInfo(alias="coverImageUrl", default=None)

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)
    """Reposts of the Article's post. 0 or more."""

    summary_text: Optional[str] = FieldInfo(alias="summaryText", default=None)
    """X's summary of the Article, when X has one"""

    title: Optional[str] = None

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)


class Author(BaseModel):
    """Available X Article author fields."""

    id: str

    name: str

    username: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    favourites_count: Optional[int] = FieldInfo(alias="favouritesCount", default=None)
    """Whole number from 0."""

    followers_count: Optional[int] = FieldInfo(alias="followersCount", default=None)
    """Whole number from 0."""

    following_count: Optional[int] = FieldInfo(alias="followingCount", default=None)
    """Whole number from 0."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)

    is_translator: Optional[bool] = FieldInfo(alias="isTranslator", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    location: Optional[str] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)
    """Whole number from 0."""

    profile_banner_url: Optional[str] = FieldInfo(alias="profileBannerUrl", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    protected: Optional[bool] = None

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)
    """Whole number from 0."""

    url: Optional[str] = None


class XGetArticleResponse(BaseModel):
    article: Article

    author: Optional[Author] = None
    """Available X Article author fields."""
