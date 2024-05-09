# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class PatchPreHireResponseBody(object):
    _types = {
        "pre_hire_id": str,
    }

    def __init__(self, d=None):
        self.pre_hire_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchPreHireResponseBodyBuilder":
        return PatchPreHireResponseBodyBuilder()


class PatchPreHireResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_pre_hire_response_body = PatchPreHireResponseBody()

    def pre_hire_id(self, pre_hire_id: str) -> "PatchPreHireResponseBodyBuilder":
        self._patch_pre_hire_response_body.pre_hire_id = pre_hire_id
        return self

    def build(self) -> "PatchPreHireResponseBody":
        return self._patch_pre_hire_response_body
