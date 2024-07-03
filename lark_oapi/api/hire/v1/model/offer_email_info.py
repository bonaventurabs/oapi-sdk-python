# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OfferEmailInfo(object):
    _types = {
        "sender_email": str,
        "cc_email_list": List[str],
        "receiver_email_list": List[str],
        "content": str,
    }

    def __init__(self, d=None):
        self.sender_email: Optional[str] = None
        self.cc_email_list: Optional[List[str]] = None
        self.receiver_email_list: Optional[List[str]] = None
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OfferEmailInfoBuilder":
        return OfferEmailInfoBuilder()


class OfferEmailInfoBuilder(object):
    def __init__(self) -> None:
        self._offer_email_info = OfferEmailInfo()

    def sender_email(self, sender_email: str) -> "OfferEmailInfoBuilder":
        self._offer_email_info.sender_email = sender_email
        return self

    def cc_email_list(self, cc_email_list: List[str]) -> "OfferEmailInfoBuilder":
        self._offer_email_info.cc_email_list = cc_email_list
        return self

    def receiver_email_list(self, receiver_email_list: List[str]) -> "OfferEmailInfoBuilder":
        self._offer_email_info.receiver_email_list = receiver_email_list
        return self

    def content(self, content: str) -> "OfferEmailInfoBuilder":
        self._offer_email_info.content = content
        return self

    def build(self) -> "OfferEmailInfo":
        return self._offer_email_info
