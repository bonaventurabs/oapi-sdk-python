# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .workforce_plan import WorkforcePlan


class ListWorkforcePlanResponseBody(object):
    _types = {
        "items": List[WorkforcePlan],
        "total": int,
    }

    def __init__(self, d=None):
        self.items: Optional[List[WorkforcePlan]] = None
        self.total: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListWorkforcePlanResponseBodyBuilder":
        return ListWorkforcePlanResponseBodyBuilder()


class ListWorkforcePlanResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_workforce_plan_response_body = ListWorkforcePlanResponseBody()

    def items(self, items: List[WorkforcePlan]) -> "ListWorkforcePlanResponseBodyBuilder":
        self._list_workforce_plan_response_body.items = items
        return self

    def total(self, total: int) -> "ListWorkforcePlanResponseBodyBuilder":
        self._list_workforce_plan_response_body.total = total
        return self

    def build(self) -> "ListWorkforcePlanResponseBody":
        return self._list_workforce_plan_response_body
