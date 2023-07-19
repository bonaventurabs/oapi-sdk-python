# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .invite_meeting_response_body import InviteMeetingResponseBody


class InviteMeetingResponse(BaseResponse):
    _types = {
        "data": InviteMeetingResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[InviteMeetingResponseBody] = None
        init(self, d, self._types)