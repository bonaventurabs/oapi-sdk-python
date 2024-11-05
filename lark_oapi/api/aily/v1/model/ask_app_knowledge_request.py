# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .ask_app_knowledge_request_body import AskAppKnowledgeRequestBody


class AskAppKnowledgeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_id: Optional[str] = None
        self.request_body: Optional[AskAppKnowledgeRequestBody] = None

    @staticmethod
    def builder() -> "AskAppKnowledgeRequestBuilder":
        return AskAppKnowledgeRequestBuilder()


class AskAppKnowledgeRequestBuilder(object):

    def __init__(self) -> None:
        ask_app_knowledge_request = AskAppKnowledgeRequest()
        ask_app_knowledge_request.http_method = HttpMethod.POST
        ask_app_knowledge_request.uri = "/open-apis/aily/v1/apps/:app_id/knowledges/ask"
        ask_app_knowledge_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._ask_app_knowledge_request: AskAppKnowledgeRequest = ask_app_knowledge_request

    def app_id(self, app_id: str) -> "AskAppKnowledgeRequestBuilder":
        self._ask_app_knowledge_request.app_id = app_id
        self._ask_app_knowledge_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self, request_body: AskAppKnowledgeRequestBody) -> "AskAppKnowledgeRequestBuilder":
        self._ask_app_knowledge_request.request_body = request_body
        self._ask_app_knowledge_request.body = request_body
        return self

    def build(self) -> AskAppKnowledgeRequest:
        return self._ask_app_knowledge_request
