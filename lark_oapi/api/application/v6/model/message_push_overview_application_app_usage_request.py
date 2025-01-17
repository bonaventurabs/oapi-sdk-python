# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .message_push_overview_application_app_usage_request_body import MessagePushOverviewApplicationAppUsageRequestBody


class MessagePushOverviewApplicationAppUsageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[MessagePushOverviewApplicationAppUsageRequestBody] = None

    @staticmethod
    def builder() -> "MessagePushOverviewApplicationAppUsageRequestBuilder":
        return MessagePushOverviewApplicationAppUsageRequestBuilder()


class MessagePushOverviewApplicationAppUsageRequestBuilder(object):

    def __init__(self) -> None:
        message_push_overview_application_app_usage_request = MessagePushOverviewApplicationAppUsageRequest()
        message_push_overview_application_app_usage_request.http_method = HttpMethod.POST
        message_push_overview_application_app_usage_request.uri = "/open-apis/application/v6/applications/:app_id/app_usage/message_push_overview"
        message_push_overview_application_app_usage_request.token_types = {AccessTokenType.TENANT}
        self._message_push_overview_application_app_usage_request: MessagePushOverviewApplicationAppUsageRequest = message_push_overview_application_app_usage_request

    def department_id_type(self, department_id_type: str) -> "MessagePushOverviewApplicationAppUsageRequestBuilder":
        self._message_push_overview_application_app_usage_request.department_id_type = department_id_type
        self._message_push_overview_application_app_usage_request.add_query("department_id_type", department_id_type)
        return self

    def app_id(self, app_id: str) -> "MessagePushOverviewApplicationAppUsageRequestBuilder":
        self._message_push_overview_application_app_usage_request.app_id = app_id
        self._message_push_overview_application_app_usage_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self,
                     request_body: MessagePushOverviewApplicationAppUsageRequestBody) -> "MessagePushOverviewApplicationAppUsageRequestBuilder":
        self._message_push_overview_application_app_usage_request.request_body = request_body
        self._message_push_overview_application_app_usage_request.body = request_body
        return self

    def build(self) -> MessagePushOverviewApplicationAppUsageRequest:
        return self._message_push_overview_application_app_usage_request
