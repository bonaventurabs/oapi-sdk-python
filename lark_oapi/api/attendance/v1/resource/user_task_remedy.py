# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.attendance.v1.model.create_user_task_remedy_request import CreateUserTaskRemedyRequest
from lark_oapi.api.attendance.v1.model.create_user_task_remedy_response import CreateUserTaskRemedyResponse
from lark_oapi.api.attendance.v1.model.query_user_allowed_remedys_user_task_remedy_request import \
    QueryUserAllowedRemedysUserTaskRemedyRequest
from lark_oapi.api.attendance.v1.model.query_user_allowed_remedys_user_task_remedy_response import \
    QueryUserAllowedRemedysUserTaskRemedyResponse
from lark_oapi.api.attendance.v1.model.query_user_task_remedy_request import QueryUserTaskRemedyRequest
from lark_oapi.api.attendance.v1.model.query_user_task_remedy_response import QueryUserTaskRemedyResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class UserTaskRemedy(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateUserTaskRemedyRequest,
               option: RequestOption = RequestOption()) -> CreateUserTaskRemedyResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateUserTaskRemedyResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateUserTaskRemedyResponse)
        response.raw = resp

        return response

    def query(self, request: QueryUserTaskRemedyRequest,
              option: RequestOption = RequestOption()) -> QueryUserTaskRemedyResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserTaskRemedyResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserTaskRemedyResponse)
        response.raw = resp

        return response

    def query_user_allowed_remedys(self, request: QueryUserAllowedRemedysUserTaskRemedyRequest,
                                   option: RequestOption = RequestOption()) -> QueryUserAllowedRemedysUserTaskRemedyResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserAllowedRemedysUserTaskRemedyResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                                 QueryUserAllowedRemedysUserTaskRemedyResponse)
        response.raw = resp

        return response