# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class SchemaFieldAnswerOption(object):
    _types = {
        "is_searchable": bool,
        "is_returnable": bool,
    }

    def __init__(self, d=None):
        self.is_searchable: Optional[bool] = None
        self.is_returnable: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SchemaFieldAnswerOptionBuilder":
        return SchemaFieldAnswerOptionBuilder()


class SchemaFieldAnswerOptionBuilder(object):
    def __init__(self) -> None:
        self._schema_field_answer_option = SchemaFieldAnswerOption()

    def is_searchable(self, is_searchable: bool) -> "SchemaFieldAnswerOptionBuilder":
        self._schema_field_answer_option.is_searchable = is_searchable
        return self

    def is_returnable(self, is_returnable: bool) -> "SchemaFieldAnswerOptionBuilder":
        self._schema_field_answer_option.is_returnable = is_returnable
        return self

    def build(self) -> "SchemaFieldAnswerOption":
        return self._schema_field_answer_option