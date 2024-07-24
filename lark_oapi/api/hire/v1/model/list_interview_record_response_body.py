# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .interview_record import InterviewRecord


class ListInterviewRecordResponseBody(object):
    _types = {
        "items": List[InterviewRecord],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[InterviewRecord]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListInterviewRecordResponseBodyBuilder":
        return ListInterviewRecordResponseBodyBuilder()


class ListInterviewRecordResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_interview_record_response_body = ListInterviewRecordResponseBody()

    def items(self, items: List[InterviewRecord]) -> "ListInterviewRecordResponseBodyBuilder":
        self._list_interview_record_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListInterviewRecordResponseBodyBuilder":
        self._list_interview_record_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListInterviewRecordResponseBodyBuilder":
        self._list_interview_record_response_body.has_more = has_more
        return self

    def build(self) -> "ListInterviewRecordResponseBody":
        return self._list_interview_record_response_body