# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AilyMessageFilter(object):
    _types = {
        "run_id": str,
        "with_partial_message": bool,
    }

    def __init__(self, d=None):
        self.run_id: Optional[str] = None
        self.with_partial_message: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyMessageFilterBuilder":
        return AilyMessageFilterBuilder()


class AilyMessageFilterBuilder(object):
    def __init__(self) -> None:
        self._aily_message_filter = AilyMessageFilter()

    def run_id(self, run_id: str) -> "AilyMessageFilterBuilder":
        self._aily_message_filter.run_id = run_id
        return self

    def with_partial_message(self, with_partial_message: bool) -> "AilyMessageFilterBuilder":
        self._aily_message_filter.with_partial_message = with_partial_message
        return self

    def build(self) -> "AilyMessageFilter":
        return self._aily_message_filter
