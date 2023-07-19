# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .subdivision import Subdivision


class GetSubdivisionResponseBody(object):
    _types = {
        "subdivision": Subdivision,
    }

    def __init__(self, d):
        self.subdivision: Optional[Subdivision] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSubdivisionResponseBodyBuilder":
        return GetSubdivisionResponseBodyBuilder()


class GetSubdivisionResponseBodyBuilder(object):
    def __init__(self,
                 get_subdivision_response_body: GetSubdivisionResponseBody = GetSubdivisionResponseBody({})) -> None:
        self._get_subdivision_response_body: GetSubdivisionResponseBody = get_subdivision_response_body

    def subdivision(self, subdivision: Subdivision) -> "GetSubdivisionResponseBodyBuilder":
        self._get_subdivision_response_body.subdivision = subdivision
        return self

    def build(self) -> "GetSubdivisionResponseBody":
        return self._get_subdivision_response_body