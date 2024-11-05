# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .dimension_entity import DimensionEntity
from .workforce_plan_eai_detail import WorkforcePlanEaiDetail


class WorkforcePlanDetailRow(object):
    _types = {
        "dimensions": List[DimensionEntity],
        "eai_detail": WorkforcePlanEaiDetail,
        "plan_value": str,
    }

    def __init__(self, d=None):
        self.dimensions: Optional[List[DimensionEntity]] = None
        self.eai_detail: Optional[WorkforcePlanEaiDetail] = None
        self.plan_value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkforcePlanDetailRowBuilder":
        return WorkforcePlanDetailRowBuilder()


class WorkforcePlanDetailRowBuilder(object):
    def __init__(self) -> None:
        self._workforce_plan_detail_row = WorkforcePlanDetailRow()

    def dimensions(self, dimensions: List[DimensionEntity]) -> "WorkforcePlanDetailRowBuilder":
        self._workforce_plan_detail_row.dimensions = dimensions
        return self

    def eai_detail(self, eai_detail: WorkforcePlanEaiDetail) -> "WorkforcePlanDetailRowBuilder":
        self._workforce_plan_detail_row.eai_detail = eai_detail
        return self

    def plan_value(self, plan_value: str) -> "WorkforcePlanDetailRowBuilder":
        self._workforce_plan_detail_row.plan_value = plan_value
        return self

    def build(self) -> "WorkforcePlanDetailRow":
        return self._workforce_plan_detail_row
