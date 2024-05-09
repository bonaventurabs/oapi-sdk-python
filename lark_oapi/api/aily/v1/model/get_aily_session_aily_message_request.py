# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetAilySessionAilyMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.aily_session_id: Optional[str] = None
        self.aily_message_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAilySessionAilyMessageRequestBuilder":
        return GetAilySessionAilyMessageRequestBuilder()


class GetAilySessionAilyMessageRequestBuilder(object):

    def __init__(self) -> None:
        get_aily_session_aily_message_request = GetAilySessionAilyMessageRequest()
        get_aily_session_aily_message_request.http_method = HttpMethod.GET
        get_aily_session_aily_message_request.uri = "/open-apis/aily/v1/sessions/:aily_session_id/messages/:aily_message_id"
        get_aily_session_aily_message_request.token_types = {AccessTokenType.USER}
        self._get_aily_session_aily_message_request: GetAilySessionAilyMessageRequest = get_aily_session_aily_message_request

    def aily_session_id(self, aily_session_id: str) -> "GetAilySessionAilyMessageRequestBuilder":
        self._get_aily_session_aily_message_request.aily_session_id = aily_session_id
        self._get_aily_session_aily_message_request.paths["aily_session_id"] = str(aily_session_id)
        return self

    def aily_message_id(self, aily_message_id: str) -> "GetAilySessionAilyMessageRequestBuilder":
        self._get_aily_session_aily_message_request.aily_message_id = aily_message_id
        self._get_aily_session_aily_message_request.paths["aily_message_id"] = str(aily_message_id)
        return self

    def build(self) -> GetAilySessionAilyMessageRequest:
        return self._get_aily_session_aily_message_request
