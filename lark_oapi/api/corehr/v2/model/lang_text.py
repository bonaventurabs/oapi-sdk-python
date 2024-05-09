# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LangText(object):
    _types = {
        "lang": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.lang: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LangTextBuilder":
        return LangTextBuilder()


class LangTextBuilder(object):
    def __init__(self) -> None:
        self._lang_text = LangText()

    def lang(self, lang: str) -> "LangTextBuilder":
        self._lang_text.lang = lang
        return self

    def value(self, value: str) -> "LangTextBuilder":
        self._lang_text.value = value
        return self

    def build(self) -> "LangText":
        return self._lang_text
