# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncCursorPage", "AsyncCursorPage", "SyncCursorPageLegacy", "AsyncCursorPageLegacy"]

_T = TypeVar("_T")


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tweets: Optional[List[object]] = None
    users: Optional[List[object]] = None
    next_cursor: Optional[str] = None
    has_next_page: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tweets: Optional[List[object]] = None
    users: Optional[List[object]] = None
    next_cursor: Optional[str] = None
    has_next_page: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncCursorPageLegacy(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"afterCursor": next_cursor})


class AsyncCursorPageLegacy(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"afterCursor": next_cursor})
