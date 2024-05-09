# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .prehire_update import PrehireUpdate


class PatchPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.pre_hire_id: Optional[str] = None
        self.request_body: Optional[PrehireUpdate] = None

    @staticmethod
    def builder() -> "PatchPreHireRequestBuilder":
        return PatchPreHireRequestBuilder()


class PatchPreHireRequestBuilder(object):

    def __init__(self) -> None:
        patch_pre_hire_request = PatchPreHireRequest()
        patch_pre_hire_request.http_method = HttpMethod.PATCH
        patch_pre_hire_request.uri = "/open-apis/corehr/v2/pre_hires/:pre_hire_id"
        patch_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._patch_pre_hire_request: PatchPreHireRequest = patch_pre_hire_request

    def pre_hire_id(self, pre_hire_id: str) -> "PatchPreHireRequestBuilder":
        self._patch_pre_hire_request.pre_hire_id = pre_hire_id
        self._patch_pre_hire_request.paths["pre_hire_id"] = str(pre_hire_id)
        return self

    def request_body(self, request_body: PrehireUpdate) -> "PatchPreHireRequestBuilder":
        self._patch_pre_hire_request.request_body = request_body
        self._patch_pre_hire_request.body = request_body
        return self

    def build(self) -> PatchPreHireRequest:
        return self._patch_pre_hire_request
