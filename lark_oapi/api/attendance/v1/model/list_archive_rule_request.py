# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListArchiveRuleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListArchiveRuleRequestBuilder":
        return ListArchiveRuleRequestBuilder()


class ListArchiveRuleRequestBuilder(object):

    def __init__(self) -> None:
        list_archive_rule_request = ListArchiveRuleRequest()
        list_archive_rule_request.http_method = HttpMethod.GET
        list_archive_rule_request.uri = "/open-apis/attendance/v1/archive_rule"
        list_archive_rule_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_archive_rule_request: ListArchiveRuleRequest = list_archive_rule_request

    def page_size(self, page_size: int) -> "ListArchiveRuleRequestBuilder":
        self._list_archive_rule_request.page_size = page_size
        self._list_archive_rule_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListArchiveRuleRequestBuilder":
        self._list_archive_rule_request.page_token = page_token
        self._list_archive_rule_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListArchiveRuleRequest:
        return self._list_archive_rule_request