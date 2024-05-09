# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .aily_mention import AilyMention


class CreateAilySessionAilyMessageRequestBody(object):
    _types = {
        "idempotent_id": str,
        "content_type": str,
        "content": str,
        "file_ids": List[str],
        "quote_message_id": str,
        "mentions": List[AilyMention],
    }

    def __init__(self, d=None):
        self.idempotent_id: Optional[str] = None
        self.content_type: Optional[str] = None
        self.content: Optional[str] = None
        self.file_ids: Optional[List[str]] = None
        self.quote_message_id: Optional[str] = None
        self.mentions: Optional[List[AilyMention]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        return CreateAilySessionAilyMessageRequestBodyBuilder()


class CreateAilySessionAilyMessageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_aily_session_aily_message_request_body = CreateAilySessionAilyMessageRequestBody()

    def idempotent_id(self, idempotent_id: str) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.idempotent_id = idempotent_id
        return self

    def content_type(self, content_type: str) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.content_type = content_type
        return self

    def content(self, content: str) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.content = content
        return self

    def file_ids(self, file_ids: List[str]) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.file_ids = file_ids
        return self

    def quote_message_id(self, quote_message_id: str) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.quote_message_id = quote_message_id
        return self

    def mentions(self, mentions: List[AilyMention]) -> "CreateAilySessionAilyMessageRequestBodyBuilder":
        self._create_aily_session_aily_message_request_body.mentions = mentions
        return self

    def build(self) -> "CreateAilySessionAilyMessageRequestBody":
        return self._create_aily_session_aily_message_request_body
