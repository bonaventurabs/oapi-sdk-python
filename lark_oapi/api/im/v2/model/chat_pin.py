# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .message_pin import MessagePin
from .url_pin import UrlPin


class ChatPin(object):
    _types = {
        "chat_pin_id": int,
        "chat_id": str,
        "chat_pin_type": str,
        "create_time": int,
        "chatter_id": str,
        "is_fixed": bool,
        "operate_fix_chatter_id": str,
        "message_pin_data": MessagePin,
        "url_pin_data": UrlPin,
    }

    def __init__(self, d=None):
        self.chat_pin_id: Optional[int] = None
        self.chat_id: Optional[str] = None
        self.chat_pin_type: Optional[str] = None
        self.create_time: Optional[int] = None
        self.chatter_id: Optional[str] = None
        self.is_fixed: Optional[bool] = None
        self.operate_fix_chatter_id: Optional[str] = None
        self.message_pin_data: Optional[MessagePin] = None
        self.url_pin_data: Optional[UrlPin] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatPinBuilder":
        return ChatPinBuilder()


class ChatPinBuilder(object):
    def __init__(self) -> None:
        self._chat_pin = ChatPin()

    def chat_pin_id(self, chat_pin_id: int) -> "ChatPinBuilder":
        self._chat_pin.chat_pin_id = chat_pin_id
        return self

    def chat_id(self, chat_id: str) -> "ChatPinBuilder":
        self._chat_pin.chat_id = chat_id
        return self

    def chat_pin_type(self, chat_pin_type: str) -> "ChatPinBuilder":
        self._chat_pin.chat_pin_type = chat_pin_type
        return self

    def create_time(self, create_time: int) -> "ChatPinBuilder":
        self._chat_pin.create_time = create_time
        return self

    def chatter_id(self, chatter_id: str) -> "ChatPinBuilder":
        self._chat_pin.chatter_id = chatter_id
        return self

    def is_fixed(self, is_fixed: bool) -> "ChatPinBuilder":
        self._chat_pin.is_fixed = is_fixed
        return self

    def operate_fix_chatter_id(self, operate_fix_chatter_id: str) -> "ChatPinBuilder":
        self._chat_pin.operate_fix_chatter_id = operate_fix_chatter_id
        return self

    def message_pin_data(self, message_pin_data: MessagePin) -> "ChatPinBuilder":
        self._chat_pin.message_pin_data = message_pin_data
        return self

    def url_pin_data(self, url_pin_data: UrlPin) -> "ChatPinBuilder":
        self._chat_pin.url_pin_data = url_pin_data
        return self

    def build(self) -> "ChatPin":
        return self._chat_pin