# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .doc_chunk_position import DocChunkPosition
from .doc_chunk_table_detail import DocChunkTableDetail
from .llm_detail import LlmDetail
from .image_detail import ImageDetail


class DocChunkResult(object):
    _types = {
        "id": int,
        "type": str,
        "positions": DocChunkPosition,
        "text": str,
        "level": int,
        "parent": int,
        "children": List[int],
        "label": str,
        "block_id": str,
        "table_detail": DocChunkTableDetail,
        "llm_detail": LlmDetail,
        "image_detail": ImageDetail,
        "slide_index": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.type: Optional[str] = None
        self.positions: Optional[DocChunkPosition] = None
        self.text: Optional[str] = None
        self.level: Optional[int] = None
        self.parent: Optional[int] = None
        self.children: Optional[List[int]] = None
        self.label: Optional[str] = None
        self.block_id: Optional[str] = None
        self.table_detail: Optional[DocChunkTableDetail] = None
        self.llm_detail: Optional[LlmDetail] = None
        self.image_detail: Optional[ImageDetail] = None
        self.slide_index: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocChunkResultBuilder":
        return DocChunkResultBuilder()


class DocChunkResultBuilder(object):
    def __init__(self) -> None:
        self._doc_chunk_result = DocChunkResult()

    def id(self, id: int) -> "DocChunkResultBuilder":
        self._doc_chunk_result.id = id
        return self

    def type(self, type: str) -> "DocChunkResultBuilder":
        self._doc_chunk_result.type = type
        return self

    def positions(self, positions: DocChunkPosition) -> "DocChunkResultBuilder":
        self._doc_chunk_result.positions = positions
        return self

    def text(self, text: str) -> "DocChunkResultBuilder":
        self._doc_chunk_result.text = text
        return self

    def level(self, level: int) -> "DocChunkResultBuilder":
        self._doc_chunk_result.level = level
        return self

    def parent(self, parent: int) -> "DocChunkResultBuilder":
        self._doc_chunk_result.parent = parent
        return self

    def children(self, children: List[int]) -> "DocChunkResultBuilder":
        self._doc_chunk_result.children = children
        return self

    def label(self, label: str) -> "DocChunkResultBuilder":
        self._doc_chunk_result.label = label
        return self

    def block_id(self, block_id: str) -> "DocChunkResultBuilder":
        self._doc_chunk_result.block_id = block_id
        return self

    def table_detail(self, table_detail: DocChunkTableDetail) -> "DocChunkResultBuilder":
        self._doc_chunk_result.table_detail = table_detail
        return self

    def llm_detail(self, llm_detail: LlmDetail) -> "DocChunkResultBuilder":
        self._doc_chunk_result.llm_detail = llm_detail
        return self

    def image_detail(self, image_detail: ImageDetail) -> "DocChunkResultBuilder":
        self._doc_chunk_result.image_detail = image_detail
        return self

    def slide_index(self, slide_index: str) -> "DocChunkResultBuilder":
        self._doc_chunk_result.slide_index = slide_index
        return self

    def build(self) -> "DocChunkResult":
        return self._doc_chunk_result
