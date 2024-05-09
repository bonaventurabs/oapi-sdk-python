# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .patch_reserve_config_disable_inform_request_body import PatchReserveConfigDisableInformRequestBody


class PatchReserveConfigDisableInformRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.reserve_config_id: Optional[str] = None
        self.request_body: Optional[PatchReserveConfigDisableInformRequestBody] = None

    @staticmethod
    def builder() -> "PatchReserveConfigDisableInformRequestBuilder":
        return PatchReserveConfigDisableInformRequestBuilder()


class PatchReserveConfigDisableInformRequestBuilder(object):

    def __init__(self) -> None:
        patch_reserve_config_disable_inform_request = PatchReserveConfigDisableInformRequest()
        patch_reserve_config_disable_inform_request.http_method = HttpMethod.PATCH
        patch_reserve_config_disable_inform_request.uri = "/open-apis/vc/v1/reserve_configs/:reserve_config_id/disable_inform"
        patch_reserve_config_disable_inform_request.token_types = {AccessTokenType.TENANT}
        self._patch_reserve_config_disable_inform_request: PatchReserveConfigDisableInformRequest = patch_reserve_config_disable_inform_request

    def user_id_type(self, user_id_type: str) -> "PatchReserveConfigDisableInformRequestBuilder":
        self._patch_reserve_config_disable_inform_request.user_id_type = user_id_type
        self._patch_reserve_config_disable_inform_request.add_query("user_id_type", user_id_type)
        return self

    def reserve_config_id(self, reserve_config_id: str) -> "PatchReserveConfigDisableInformRequestBuilder":
        self._patch_reserve_config_disable_inform_request.reserve_config_id = reserve_config_id
        self._patch_reserve_config_disable_inform_request.paths["reserve_config_id"] = str(reserve_config_id)
        return self

    def request_body(self,
                     request_body: PatchReserveConfigDisableInformRequestBody) -> "PatchReserveConfigDisableInformRequestBuilder":
        self._patch_reserve_config_disable_inform_request.request_body = request_body
        self._patch_reserve_config_disable_inform_request.body = request_body
        return self

    def build(self) -> PatchReserveConfigDisableInformRequest:
        return self._patch_reserve_config_disable_inform_request
