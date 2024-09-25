# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DelReportArchiveRuleRequestBody(object):
    _types = {
        "month": str,
        "operator_id": str,
        "archive_rule_id": str,
        "user_ids": List[str],
    }

    def __init__(self, d=None):
        self.month: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.archive_rule_id: Optional[str] = None
        self.user_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DelReportArchiveRuleRequestBodyBuilder":
        return DelReportArchiveRuleRequestBodyBuilder()


class DelReportArchiveRuleRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._del_report_archive_rule_request_body = DelReportArchiveRuleRequestBody()

    def month(self, month: str) -> "DelReportArchiveRuleRequestBodyBuilder":
        self._del_report_archive_rule_request_body.month = month
        return self

    def operator_id(self, operator_id: str) -> "DelReportArchiveRuleRequestBodyBuilder":
        self._del_report_archive_rule_request_body.operator_id = operator_id
        return self

    def archive_rule_id(self, archive_rule_id: str) -> "DelReportArchiveRuleRequestBodyBuilder":
        self._del_report_archive_rule_request_body.archive_rule_id = archive_rule_id
        return self

    def user_ids(self, user_ids: List[str]) -> "DelReportArchiveRuleRequestBodyBuilder":
        self._del_report_archive_rule_request_body.user_ids = user_ids
        return self

    def build(self) -> "DelReportArchiveRuleRequestBody":
        return self._del_report_archive_rule_request_body