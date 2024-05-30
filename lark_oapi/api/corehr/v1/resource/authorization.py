# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.get_by_param_authorization_request import GetByParamAuthorizationRequest
from ..model.get_by_param_authorization_response import GetByParamAuthorizationResponse
from ..model.query_authorization_request import QueryAuthorizationRequest
from ..model.query_authorization_response import QueryAuthorizationResponse


class Authorization(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get_by_param(self, request: GetByParamAuthorizationRequest,
                     option: Optional[RequestOption] = None) -> GetByParamAuthorizationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetByParamAuthorizationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetByParamAuthorizationResponse)
        response.raw = resp

        return response

    async def aget_by_param(self, request: GetByParamAuthorizationRequest,
                            option: Optional[RequestOption] = None) -> GetByParamAuthorizationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetByParamAuthorizationResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetByParamAuthorizationResponse)
        response.raw = resp

        return response

    def query(self, request: QueryAuthorizationRequest,
              option: Optional[RequestOption] = None) -> QueryAuthorizationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryAuthorizationResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryAuthorizationResponse)
        response.raw = resp

        return response

    async def aquery(self, request: QueryAuthorizationRequest,
                     option: Optional[RequestOption] = None) -> QueryAuthorizationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: QueryAuthorizationResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryAuthorizationResponse)
        response.raw = resp

        return response
