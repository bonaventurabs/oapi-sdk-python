# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LinkPreview(object):
    _types = {
        "url": str,
        "url_type": str,
    }

    def __init__(self, d=None):
        self.url: Optional[str] = None
        self.url_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LinkPreviewBuilder":
        return LinkPreviewBuilder()


class LinkPreviewBuilder(object):
    def __init__(self) -> None:
        self._link_preview = LinkPreview()

    def url(self, url: str) -> "LinkPreviewBuilder":
        self._link_preview.url = url
        return self

    def url_type(self, url_type: str) -> "LinkPreviewBuilder":
        self._link_preview.url_type = url_type
        return self

    def build(self) -> "LinkPreview":
        return self._link_preview
