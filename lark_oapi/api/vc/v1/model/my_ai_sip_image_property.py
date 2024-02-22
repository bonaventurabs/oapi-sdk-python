# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MyAiSipImageProperty(object):
    _types = {
        "theme": str,
        "number": int,
        "size": str,
    }

    def __init__(self, d=None):
        self.theme: Optional[str] = None
        self.number: Optional[int] = None
        self.size: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MyAiSipImagePropertyBuilder":
        return MyAiSipImagePropertyBuilder()


class MyAiSipImagePropertyBuilder(object):
    def __init__(self) -> None:
        self._my_ai_sip_image_property = MyAiSipImageProperty()

    def theme(self, theme: str) -> "MyAiSipImagePropertyBuilder":
        self._my_ai_sip_image_property.theme = theme
        return self

    def number(self, number: int) -> "MyAiSipImagePropertyBuilder":
        self._my_ai_sip_image_property.number = number
        return self

    def size(self, size: str) -> "MyAiSipImagePropertyBuilder":
        self._my_ai_sip_image_property.size = size
        return self

    def build(self) -> "MyAiSipImageProperty":
        return self._my_ai_sip_image_property