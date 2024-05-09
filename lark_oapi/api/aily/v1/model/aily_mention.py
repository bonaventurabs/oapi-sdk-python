# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AilyMention(object):
    _types = {
        "entity_id": str,
        "identity_provider": str,
        "key": str,
        "name": str,
        "aily_id": str,
    }

    def __init__(self, d=None):
        self.entity_id: Optional[str] = None
        self.identity_provider: Optional[str] = None
        self.key: Optional[str] = None
        self.name: Optional[str] = None
        self.aily_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyMentionBuilder":
        return AilyMentionBuilder()


class AilyMentionBuilder(object):
    def __init__(self) -> None:
        self._aily_mention = AilyMention()

    def entity_id(self, entity_id: str) -> "AilyMentionBuilder":
        self._aily_mention.entity_id = entity_id
        return self

    def identity_provider(self, identity_provider: str) -> "AilyMentionBuilder":
        self._aily_mention.identity_provider = identity_provider
        return self

    def key(self, key: str) -> "AilyMentionBuilder":
        self._aily_mention.key = key
        return self

    def name(self, name: str) -> "AilyMentionBuilder":
        self._aily_mention.name = name
        return self

    def aily_id(self, aily_id: str) -> "AilyMentionBuilder":
        self._aily_mention.aily_id = aily_id
        return self

    def build(self) -> "AilyMention":
        return self._aily_mention
