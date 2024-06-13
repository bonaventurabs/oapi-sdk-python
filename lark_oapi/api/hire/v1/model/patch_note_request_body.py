# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .mention_entity import MentionEntity


class PatchNoteRequestBody(object):
    _types = {
        "content": str,
        "operator_id": str,
        "notify_mentioned_user": bool,
        "mention_entity_list": List[MentionEntity],
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.notify_mentioned_user: Optional[bool] = None
        self.mention_entity_list: Optional[List[MentionEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchNoteRequestBodyBuilder":
        return PatchNoteRequestBodyBuilder()


class PatchNoteRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_note_request_body = PatchNoteRequestBody()

    def content(self, content: str) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.content = content
        return self

    def operator_id(self, operator_id: str) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.operator_id = operator_id
        return self

    def notify_mentioned_user(self, notify_mentioned_user: bool) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.notify_mentioned_user = notify_mentioned_user
        return self

    def mention_entity_list(self, mention_entity_list: List[MentionEntity]) -> "PatchNoteRequestBodyBuilder":
        self._patch_note_request_body.mention_entity_list = mention_entity_list
        return self

    def build(self) -> "PatchNoteRequestBody":
        return self._patch_note_request_body
