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
from ..model.get_offer_application_form_request import GetOfferApplicationFormRequest
from ..model.get_offer_application_form_response import GetOfferApplicationFormResponse
from ..model.list_offer_application_form_request import ListOfferApplicationFormRequest
from ..model.list_offer_application_form_response import ListOfferApplicationFormResponse


class OfferApplicationForm(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetOfferApplicationFormRequest,
            option: Optional[RequestOption] = None) -> GetOfferApplicationFormResponse:
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
        response: GetOfferApplicationFormResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetOfferApplicationFormResponse)
        response.raw = resp

        return response

    async def aget(self, request: GetOfferApplicationFormRequest,
                   option: Optional[RequestOption] = None) -> GetOfferApplicationFormResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: GetOfferApplicationFormResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetOfferApplicationFormResponse)
        response.raw = resp

        return response

    def list(self, request: ListOfferApplicationFormRequest,
             option: Optional[RequestOption] = None) -> ListOfferApplicationFormResponse:
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
        response: ListOfferApplicationFormResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    ListOfferApplicationFormResponse)
        response.raw = resp

        return response

    async def alist(self, request: ListOfferApplicationFormRequest,
                    option: Optional[RequestOption] = None) -> ListOfferApplicationFormResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: ListOfferApplicationFormResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    ListOfferApplicationFormResponse)
        response.raw = resp

        return response
