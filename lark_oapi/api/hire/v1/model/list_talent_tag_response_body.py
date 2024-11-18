# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .talent_tag import TalentTag


class ListTalentTagResponseBody(object):
    _types = {
        "items": List[TalentTag],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[TalentTag]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTalentTagResponseBodyBuilder":
        return ListTalentTagResponseBodyBuilder()


class ListTalentTagResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_talent_tag_response_body = ListTalentTagResponseBody()

    def items(self, items: List[TalentTag]) -> "ListTalentTagResponseBodyBuilder":
        self._list_talent_tag_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListTalentTagResponseBodyBuilder":
        self._list_talent_tag_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListTalentTagResponseBodyBuilder":
        self._list_talent_tag_response_body.page_token = page_token
        return self

    def build(self) -> "ListTalentTagResponseBody":
        return self._list_talent_tag_response_body