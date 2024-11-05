# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AuditWebContext(object):
    _types = {
        "user_agent": str,
        "i_p": str,
    }

    def __init__(self, d=None):
        self.user_agent: Optional[str] = None
        self.i_p: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditWebContextBuilder":
        return AuditWebContextBuilder()


class AuditWebContextBuilder(object):
    def __init__(self) -> None:
        self._audit_web_context = AuditWebContext()

    def user_agent(self, user_agent: str) -> "AuditWebContextBuilder":
        self._audit_web_context.user_agent = user_agent
        return self

    def i_p(self, i_p: str) -> "AuditWebContextBuilder":
        self._audit_web_context.i_p = i_p
        return self

    def build(self) -> "AuditWebContext":
        return self._audit_web_context
