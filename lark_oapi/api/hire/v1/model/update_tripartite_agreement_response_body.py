# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .tripartite_agreement_info import TripartiteAgreementInfo


class UpdateTripartiteAgreementResponseBody(object):
    _types = {
        "tripartite_agreement": TripartiteAgreementInfo,
    }

    def __init__(self, d=None):
        self.tripartite_agreement: Optional[TripartiteAgreementInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTripartiteAgreementResponseBodyBuilder":
        return UpdateTripartiteAgreementResponseBodyBuilder()


class UpdateTripartiteAgreementResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_tripartite_agreement_response_body = UpdateTripartiteAgreementResponseBody()

    def tripartite_agreement(self,
                             tripartite_agreement: TripartiteAgreementInfo) -> "UpdateTripartiteAgreementResponseBodyBuilder":
        self._update_tripartite_agreement_response_body.tripartite_agreement = tripartite_agreement
        return self

    def build(self) -> "UpdateTripartiteAgreementResponseBody":
        return self._update_tripartite_agreement_response_body