# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .approval_daily_detail import ApprovalDailyDetail


class OvertimeApproval(object):
    _types = {
        "user_id": str,
        "start_time": str,
        "end_time": str,
        "create_time": int,
        "approval_daily_details": List[ApprovalDailyDetail],
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.create_time: Optional[int] = None
        self.approval_daily_details: Optional[List[ApprovalDailyDetail]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OvertimeApprovalBuilder":
        return OvertimeApprovalBuilder()


class OvertimeApprovalBuilder(object):
    def __init__(self) -> None:
        self._overtime_approval = OvertimeApproval()

    def user_id(self, user_id: str) -> "OvertimeApprovalBuilder":
        self._overtime_approval.user_id = user_id
        return self

    def start_time(self, start_time: str) -> "OvertimeApprovalBuilder":
        self._overtime_approval.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "OvertimeApprovalBuilder":
        self._overtime_approval.end_time = end_time
        return self

    def create_time(self, create_time: int) -> "OvertimeApprovalBuilder":
        self._overtime_approval.create_time = create_time
        return self

    def approval_daily_details(self, approval_daily_details: List[ApprovalDailyDetail]) -> "OvertimeApprovalBuilder":
        self._overtime_approval.approval_daily_details = approval_daily_details
        return self

    def build(self) -> "OvertimeApproval":
        return self._overtime_approval
