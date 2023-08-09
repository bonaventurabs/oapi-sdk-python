# Code generated by Lark OpenAPI.

import io
from typing import *

from requests_toolbelt import MultipartEncoder

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.create_image_request import CreateImageRequest
from ..model.create_image_response import CreateImageResponse
from ..model.get_image_request import GetImageRequest
from ..model.get_image_response import GetImageResponse


class Image(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateImageRequest, option: Optional[RequestOption] = None) -> CreateImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 处理 form-data
        if request.body is not None:
            form_data = MultipartEncoder(Files.parse_form_data(request.body))
            option.headers[CONTENT_TYPE] = form_data.content_type
            request.body = form_data

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateImageResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateImageResponse)
        response.raw = resp

        return response

    def get(self, request: GetImageRequest, option: Optional[RequestOption] = None) -> GetImageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        if 200 <= resp.status_code < 300:
            response: GetImageResponse = GetImageResponse({})
            response.code = 0
            response.raw = resp
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(response.raw.headers)
            return response

        # 反序列化
        response: GetImageResponse = JSON.unmarshal(str(resp.content, UTF_8), GetImageResponse)
        response.raw = resp

        return response
