# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_aily_session_aily_message_response_body import GetAilySessionAilyMessageResponseBody


class GetAilySessionAilyMessageResponse(BaseResponse):
    _types = {
        "data": GetAilySessionAilyMessageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetAilySessionAilyMessageResponseBody] = None
        init(self, d, self._types)
