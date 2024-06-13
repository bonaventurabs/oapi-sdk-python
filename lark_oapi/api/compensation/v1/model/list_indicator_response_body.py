# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .indicator import Indicator


class ListIndicatorResponseBody(object):
    _types = {
        "items": List[Indicator],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Indicator]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListIndicatorResponseBodyBuilder":
        return ListIndicatorResponseBodyBuilder()


class ListIndicatorResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_indicator_response_body = ListIndicatorResponseBody()

    def items(self, items: List[Indicator]) -> "ListIndicatorResponseBodyBuilder":
        self._list_indicator_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListIndicatorResponseBodyBuilder":
        self._list_indicator_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListIndicatorResponseBodyBuilder":
        self._list_indicator_response_body.has_more = has_more
        return self

    def build(self) -> "ListIndicatorResponseBody":
        return self._list_indicator_response_body
