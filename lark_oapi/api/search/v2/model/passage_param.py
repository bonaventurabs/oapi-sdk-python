# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .doc_passage_param import DocPassageParam
from .wiki_passage_param import WikiPassageParam
from .web_passage_param import WebPassageParam
from .helpdesk_passage_param import HelpdeskPassageParam
from .lingo_passage_param import LingoPassageParam
from .message_passage_param import MessagePassageParam


class PassageParam(object):
    _types = {
        "doc_param": DocPassageParam,
        "wiki_param": WikiPassageParam,
        "web_param": WebPassageParam,
        "helpdesk_param": HelpdeskPassageParam,
        "lingo_param": LingoPassageParam,
        "message_param": MessagePassageParam,
    }

    def __init__(self, d=None):
        self.doc_param: Optional[DocPassageParam] = None
        self.wiki_param: Optional[WikiPassageParam] = None
        self.web_param: Optional[WebPassageParam] = None
        self.helpdesk_param: Optional[HelpdeskPassageParam] = None
        self.lingo_param: Optional[LingoPassageParam] = None
        self.message_param: Optional[MessagePassageParam] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PassageParamBuilder":
        return PassageParamBuilder()


class PassageParamBuilder(object):
    def __init__(self) -> None:
        self._passage_param = PassageParam()

    def doc_param(self, doc_param: DocPassageParam) -> "PassageParamBuilder":
        self._passage_param.doc_param = doc_param
        return self

    def wiki_param(self, wiki_param: WikiPassageParam) -> "PassageParamBuilder":
        self._passage_param.wiki_param = wiki_param
        return self

    def web_param(self, web_param: WebPassageParam) -> "PassageParamBuilder":
        self._passage_param.web_param = web_param
        return self

    def helpdesk_param(self, helpdesk_param: HelpdeskPassageParam) -> "PassageParamBuilder":
        self._passage_param.helpdesk_param = helpdesk_param
        return self

    def lingo_param(self, lingo_param: LingoPassageParam) -> "PassageParamBuilder":
        self._passage_param.lingo_param = lingo_param
        return self

    def message_param(self, message_param: MessagePassageParam) -> "PassageParamBuilder":
        self._passage_param.message_param = message_param
        return self

    def build(self) -> "PassageParam":
        return self._passage_param
