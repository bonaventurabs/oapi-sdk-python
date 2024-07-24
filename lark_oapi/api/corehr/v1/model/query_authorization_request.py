# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class QueryAuthorizationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employment_id_list: Optional[List[str]] = None
        self.role_id_list: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "QueryAuthorizationRequestBuilder":
        return QueryAuthorizationRequestBuilder()


class QueryAuthorizationRequestBuilder(object):

    def __init__(self) -> None:
        query_authorization_request = QueryAuthorizationRequest()
        query_authorization_request.http_method = HttpMethod.GET
        query_authorization_request.uri = "/open-apis/corehr/v1/authorizations/query"
        query_authorization_request.token_types = {AccessTokenType.TENANT}
        self._query_authorization_request: QueryAuthorizationRequest = query_authorization_request

    def employment_id_list(self, employment_id_list: List[str]) -> "QueryAuthorizationRequestBuilder":
        self._query_authorization_request.employment_id_list = employment_id_list
        self._query_authorization_request.add_query("employment_id_list", employment_id_list)
        return self

    def role_id_list(self, role_id_list: List[str]) -> "QueryAuthorizationRequestBuilder":
        self._query_authorization_request.role_id_list = role_id_list
        self._query_authorization_request.add_query("role_id_list", role_id_list)
        return self

    def page_token(self, page_token: str) -> "QueryAuthorizationRequestBuilder":
        self._query_authorization_request.page_token = page_token
        self._query_authorization_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "QueryAuthorizationRequestBuilder":
        self._query_authorization_request.page_size = page_size
        self._query_authorization_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "QueryAuthorizationRequestBuilder":
        self._query_authorization_request.user_id_type = user_id_type
        self._query_authorization_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> QueryAuthorizationRequest:
        return self._query_authorization_request