# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetArticleResponse", "Article", "ArticleContent", "Author"]


class ArticleContent(BaseModel):
    height: Optional[int] = None

    text: Optional[str] = None

    type: Optional[str] = None
    """
    Block type: unstyled, header-one, header-two, header-three, unordered-list-item,
    ordered-list-item, image, gif, divider
    """

    url: Optional[str] = None
    """Media URL for image/gif blocks"""

    width: Optional[int] = None


class Article(BaseModel):
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
    """Author of a tweet with follower count and verification status."""

    id: str

    followers: int

    username: str

    verified: bool

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)


class XGetArticleResponse(BaseModel):
    article: Article

    author: Optional[Author] = None
    """Author of a tweet with follower count and verification status."""
