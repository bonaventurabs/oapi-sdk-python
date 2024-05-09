# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteAilySessionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.aily_session_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAilySessionRequestBuilder":
        return DeleteAilySessionRequestBuilder()


class DeleteAilySessionRequestBuilder(object):

    def __init__(self) -> None:
        delete_aily_session_request = DeleteAilySessionRequest()
        delete_aily_session_request.http_method = HttpMethod.DELETE
        delete_aily_session_request.uri = "/open-apis/aily/v1/sessions/:aily_session_id"
        delete_aily_session_request.token_types = {AccessTokenType.USER}
        self._delete_aily_session_request: DeleteAilySessionRequest = delete_aily_session_request

    def aily_session_id(self, aily_session_id: str) -> "DeleteAilySessionRequestBuilder":
        self._delete_aily_session_request.aily_session_id = aily_session_id
        self._delete_aily_session_request.paths["aily_session_id"] = str(aily_session_id)
        return self

    def build(self) -> DeleteAilySessionRequest:
        return self._delete_aily_session_request