# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class PlanCondition(object):
    _types = {
        "left_type": int,
        "operator": int,
        "right_value": List[str],
    }

    def __init__(self, d=None):
        self.left_type: Optional[int] = None
        self.operator: Optional[int] = None
        self.right_value: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PlanConditionBuilder":
        return PlanConditionBuilder()


class PlanConditionBuilder(object):
    def __init__(self) -> None:
        self._plan_condition = PlanCondition()

    def left_type(self, left_type: int) -> "PlanConditionBuilder":
        self._plan_condition.left_type = left_type
        return self

    def operator(self, operator: int) -> "PlanConditionBuilder":
        self._plan_condition.operator = operator
        return self

    def right_value(self, right_value: List[str]) -> "PlanConditionBuilder":
        self._plan_condition.right_value = right_value
        return self

    def build(self) -> "PlanCondition":
        return self._plan_condition
