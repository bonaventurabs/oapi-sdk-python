# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.drive.v1.model.get_file_statistics_request import GetFileStatisticsRequest
from lark_oapi.api.drive.v1.model.get_file_statistics_response import GetFileStatisticsResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class FileStatistics(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetFileStatisticsRequest,
            option: RequestOption = RequestOption()) -> GetFileStatisticsResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetFileStatisticsResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFileStatisticsResponse)
        response.raw = resp

        return response