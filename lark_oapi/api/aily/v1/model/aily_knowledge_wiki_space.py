# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .aily_knowledge_docs import AilyKnowledgeDocs


class AilyKnowledgeWikiSpace(object):
    _types = {
        "title": str,
        "space_id": str,
        "sub_docs": List[AilyKnowledgeDocs],
    }

    def __init__(self, d=None):
        self.title: Optional[str] = None
        self.space_id: Optional[str] = None
        self.sub_docs: Optional[List[AilyKnowledgeDocs]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyKnowledgeWikiSpaceBuilder":
        return AilyKnowledgeWikiSpaceBuilder()


class AilyKnowledgeWikiSpaceBuilder(object):
    def __init__(self) -> None:
        self._aily_knowledge_wiki_space = AilyKnowledgeWikiSpace()

    def title(self, title: str) -> "AilyKnowledgeWikiSpaceBuilder":
        self._aily_knowledge_wiki_space.title = title
        return self

    def space_id(self, space_id: str) -> "AilyKnowledgeWikiSpaceBuilder":
        self._aily_knowledge_wiki_space.space_id = space_id
        return self

    def sub_docs(self, sub_docs: List[AilyKnowledgeDocs]) -> "AilyKnowledgeWikiSpaceBuilder":
        self._aily_knowledge_wiki_space.sub_docs = sub_docs
        return self

    def build(self) -> "AilyKnowledgeWikiSpace":
        return self._aily_knowledge_wiki_space
