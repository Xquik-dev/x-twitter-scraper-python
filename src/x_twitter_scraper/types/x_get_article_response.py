# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetArticleResponse", "Article", "ArticleContent", "ArticleContentInlineStyleRange", "Author"]


class ArticleContentInlineStyleRange(BaseModel):
    length: Optional[int] = None

    offset: Optional[int] = None

    style: Optional[str] = None


class ArticleContent(BaseModel):
    height: Optional[int] = None

    inline_style_ranges: Optional[List[ArticleContentInlineStyleRange]] = FieldInfo(
        alias="inlineStyleRanges", default=None
    )
    """Inline text formatting ranges"""

    preview_url: Optional[str] = FieldInfo(alias="previewUrl", default=None)
    """Preview image URL for media blocks"""

    text: Optional[str] = None

    type: Optional[str] = None
    """
    Block type: paragraph, header-one, header-two, header-three, header-four,
    header-five, header-six, unordered-list-item, ordered-list-item, blockquote,
    code-block, media, divider
    """

    url: Optional[str] = None
    """Media URL for media blocks"""

    width: Optional[int] = None


class Article(BaseModel):
    body_text: Optional[str] = FieldInfo(alias="bodyText", default=None)
    """Plain text joined from all article blocks"""

    contents: Optional[List[ArticleContent]] = None

    cover_image_url: Optional[str] = FieldInfo(alias="coverImageUrl", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    title: Optional[str] = None

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)


class Author(BaseModel):
    """X Article author profile fields returned when available."""

    id: str

    name: str

    username: str

    can_dm: Optional[bool] = FieldInfo(alias="canDm", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    favourites_count: Optional[int] = FieldInfo(alias="favouritesCount", default=None)

    followers_count: Optional[int] = FieldInfo(alias="followersCount", default=None)

    following_count: Optional[int] = FieldInfo(alias="followingCount", default=None)

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)

    is_translator: Optional[bool] = FieldInfo(alias="isTranslator", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    location: Optional[str] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    profile_banner_url: Optional[str] = FieldInfo(alias="profileBannerUrl", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    protected: Optional[bool] = None

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    url: Optional[str] = None


class XGetArticleResponse(BaseModel):
    article: Article

    author: Optional[Author] = None
    """X Article author profile fields returned when available."""
