# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetAilySessionRunRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.aily_session_id: Optional[str] = None
        self.run_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAilySessionRunRequestBuilder":
        return GetAilySessionRunRequestBuilder()


class GetAilySessionRunRequestBuilder(object):

    def __init__(self) -> None:
        get_aily_session_run_request = GetAilySessionRunRequest()
        get_aily_session_run_request.http_method = HttpMethod.GET
        get_aily_session_run_request.uri = "/open-apis/aily/v1/sessions/:aily_session_id/runs/:run_id"
        get_aily_session_run_request.token_types = {AccessTokenType.USER}
        self._get_aily_session_run_request: GetAilySessionRunRequest = get_aily_session_run_request

    def aily_session_id(self, aily_session_id: str) -> "GetAilySessionRunRequestBuilder":
        self._get_aily_session_run_request.aily_session_id = aily_session_id
        self._get_aily_session_run_request.paths["aily_session_id"] = str(aily_session_id)
        return self

    def run_id(self, run_id: str) -> "GetAilySessionRunRequestBuilder":
        self._get_aily_session_run_request.run_id = run_id
        self._get_aily_session_run_request.paths["run_id"] = str(run_id)
        return self

    def build(self) -> GetAilySessionRunRequest:
        return self._get_aily_session_run_request
