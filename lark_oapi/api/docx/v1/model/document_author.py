# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DocumentAuthor(object):
    _types = {
        "user_id": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocumentAuthorBuilder":
        return DocumentAuthorBuilder()


class DocumentAuthorBuilder(object):
    def __init__(self) -> None:
        self._document_author = DocumentAuthor()

    def user_id(self, user_id: str) -> "DocumentAuthorBuilder":
        self._document_author.user_id = user_id
        return self

    def build(self) -> "DocumentAuthor":
        return self._document_author