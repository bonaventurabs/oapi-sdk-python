# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ObjectiveCheckOutput(object):
    _types = {
        "failed_lists": List[int],
        "status_code": int,
    }

    def __init__(self, d=None):
        self.failed_lists: Optional[List[int]] = None
        self.status_code: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectiveCheckOutputBuilder":
        return ObjectiveCheckOutputBuilder()


class ObjectiveCheckOutputBuilder(object):
    def __init__(self) -> None:
        self._objective_check_output = ObjectiveCheckOutput()

    def failed_lists(self, failed_lists: List[int]) -> "ObjectiveCheckOutputBuilder":
        self._objective_check_output.failed_lists = failed_lists
        return self

    def status_code(self, status_code: int) -> "ObjectiveCheckOutputBuilder":
        self._objective_check_output.status_code = status_code
        return self

    def build(self) -> "ObjectiveCheckOutput":
        return self._objective_check_output
