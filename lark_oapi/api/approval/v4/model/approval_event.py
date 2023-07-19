# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApprovalEvent(object):
    _types = {
        "approval_id": str,
        "approval_code": str,
        "version_id": str,
        "widget_group_type": int,
        "form_definition_id": str,
        "process_obj": str,
        "timestamp": str,
        "extra": str,
    }

    def __init__(self, d):
        self.approval_id: Optional[str] = None
        self.approval_code: Optional[str] = None
        self.version_id: Optional[str] = None
        self.widget_group_type: Optional[int] = None
        self.form_definition_id: Optional[str] = None
        self.process_obj: Optional[str] = None
        self.timestamp: Optional[str] = None
        self.extra: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalEventBuilder":
        return ApprovalEventBuilder()


class ApprovalEventBuilder(object):
    def __init__(self, approval_event: ApprovalEvent = ApprovalEvent({})) -> None:
        self._approval_event: ApprovalEvent = approval_event

    def approval_id(self, approval_id: str) -> "ApprovalEventBuilder":
        self._approval_event.approval_id = approval_id
        return self

    def approval_code(self, approval_code: str) -> "ApprovalEventBuilder":
        self._approval_event.approval_code = approval_code
        return self

    def version_id(self, version_id: str) -> "ApprovalEventBuilder":
        self._approval_event.version_id = version_id
        return self

    def widget_group_type(self, widget_group_type: int) -> "ApprovalEventBuilder":
        self._approval_event.widget_group_type = widget_group_type
        return self

    def form_definition_id(self, form_definition_id: str) -> "ApprovalEventBuilder":
        self._approval_event.form_definition_id = form_definition_id
        return self

    def process_obj(self, process_obj: str) -> "ApprovalEventBuilder":
        self._approval_event.process_obj = process_obj
        return self

    def timestamp(self, timestamp: str) -> "ApprovalEventBuilder":
        self._approval_event.timestamp = timestamp
        return self

    def extra(self, extra: str) -> "ApprovalEventBuilder":
        self._approval_event.extra = extra
        return self

    def build(self) -> "ApprovalEvent":
        return self._approval_event