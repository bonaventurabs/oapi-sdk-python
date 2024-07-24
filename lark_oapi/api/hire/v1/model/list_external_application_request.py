# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListExternalApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.talent_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListExternalApplicationRequestBuilder":
        return ListExternalApplicationRequestBuilder()


class ListExternalApplicationRequestBuilder(object):

    def __init__(self) -> None:
        list_external_application_request = ListExternalApplicationRequest()
        list_external_application_request.http_method = HttpMethod.GET
        list_external_application_request.uri = "/open-apis/hire/v1/external_applications"
        list_external_application_request.token_types = {AccessTokenType.TENANT}
        self._list_external_application_request: ListExternalApplicationRequest = list_external_application_request

    def talent_id(self, talent_id: str) -> "ListExternalApplicationRequestBuilder":
        self._list_external_application_request.talent_id = talent_id
        self._list_external_application_request.add_query("talent_id", talent_id)
        return self

    def page_size(self, page_size: int) -> "ListExternalApplicationRequestBuilder":
        self._list_external_application_request.page_size = page_size
        self._list_external_application_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListExternalApplicationRequestBuilder":
        self._list_external_application_request.page_token = page_token
        self._list_external_application_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListExternalApplicationRequest:
        return self._list_external_application_request