# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAilySessionRunRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.aily_session_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListAilySessionRunRequestBuilder":
        return ListAilySessionRunRequestBuilder()


class ListAilySessionRunRequestBuilder(object):

    def __init__(self) -> None:
        list_aily_session_run_request = ListAilySessionRunRequest()
        list_aily_session_run_request.http_method = HttpMethod.GET
        list_aily_session_run_request.uri = "/open-apis/aily/v1/sessions/:aily_session_id/runs"
        list_aily_session_run_request.token_types = {AccessTokenType.USER}
        self._list_aily_session_run_request: ListAilySessionRunRequest = list_aily_session_run_request

    def page_size(self, page_size: int) -> "ListAilySessionRunRequestBuilder":
        self._list_aily_session_run_request.page_size = page_size
        self._list_aily_session_run_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAilySessionRunRequestBuilder":
        self._list_aily_session_run_request.page_token = page_token
        self._list_aily_session_run_request.add_query("page_token", page_token)
        return self

    def aily_session_id(self, aily_session_id: str) -> "ListAilySessionRunRequestBuilder":
        self._list_aily_session_run_request.aily_session_id = aily_session_id
        self._list_aily_session_run_request.paths["aily_session_id"] = str(aily_session_id)
        return self

    def build(self) -> ListAilySessionRunRequest:
        return self._list_aily_session_run_request
