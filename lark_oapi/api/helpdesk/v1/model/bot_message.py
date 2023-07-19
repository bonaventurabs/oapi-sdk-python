# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BotMessage(object):
    _types = {
        "msg_type": str,
        "content": str,
        "receiver_id": str,
        "receive_type": str,
    }

    def __init__(self, d):
        self.msg_type: Optional[str] = None
        self.content: Optional[str] = None
        self.receiver_id: Optional[str] = None
        self.receive_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BotMessageBuilder":
        return BotMessageBuilder()


class BotMessageBuilder(object):
    def __init__(self, bot_message: BotMessage = BotMessage({})) -> None:
        self._bot_message: BotMessage = bot_message

    def msg_type(self, msg_type: str) -> "BotMessageBuilder":
        self._bot_message.msg_type = msg_type
        return self

    def content(self, content: str) -> "BotMessageBuilder":
        self._bot_message.content = content
        return self

    def receiver_id(self, receiver_id: str) -> "BotMessageBuilder":
        self._bot_message.receiver_id = receiver_id
        return self

    def receive_type(self, receive_type: str) -> "BotMessageBuilder":
        self._bot_message.receive_type = receive_type
        return self

    def build(self) -> "BotMessage":
        return self._bot_message