# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FormFieldVariableNumberValue(object):
    _types = {
        "value": int,
    }

    def __init__(self, d=None):
        self.value: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FormFieldVariableNumberValueBuilder":
        return FormFieldVariableNumberValueBuilder()


class FormFieldVariableNumberValueBuilder(object):
    def __init__(self) -> None:
        self._form_field_variable_number_value = FormFieldVariableNumberValue()

    def value(self, value: int) -> "FormFieldVariableNumberValueBuilder":
        self._form_field_variable_number_value.value = value
        return self

    def build(self) -> "FormFieldVariableNumberValue":
        return self._form_field_variable_number_value