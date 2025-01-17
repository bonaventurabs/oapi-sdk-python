# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .field_variable_value_i18n import FieldVariableValueI18n
from .field_variable_value_to import FieldVariableValueTo
from .field_variable_sub_vlaue import FieldVariableSubVlaue


class FieldVariableValue(object):
    _types = {
        "variable_api_name": str,
        "variable_name": FieldVariableValueI18n,
        "variable_value": FieldVariableValueTo,
        "sub_values": List[FieldVariableSubVlaue],
    }

    def __init__(self, d=None):
        self.variable_api_name: Optional[str] = None
        self.variable_name: Optional[FieldVariableValueI18n] = None
        self.variable_value: Optional[FieldVariableValueTo] = None
        self.sub_values: Optional[List[FieldVariableSubVlaue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FieldVariableValueBuilder":
        return FieldVariableValueBuilder()


class FieldVariableValueBuilder(object):
    def __init__(self) -> None:
        self._field_variable_value = FieldVariableValue()

    def variable_api_name(self, variable_api_name: str) -> "FieldVariableValueBuilder":
        self._field_variable_value.variable_api_name = variable_api_name
        return self

    def variable_name(self, variable_name: FieldVariableValueI18n) -> "FieldVariableValueBuilder":
        self._field_variable_value.variable_name = variable_name
        return self

    def variable_value(self, variable_value: FieldVariableValueTo) -> "FieldVariableValueBuilder":
        self._field_variable_value.variable_value = variable_value
        return self

    def sub_values(self, sub_values: List[FieldVariableSubVlaue]) -> "FieldVariableValueBuilder":
        self._field_variable_value.sub_values = sub_values
        return self

    def build(self) -> "FieldVariableValue":
        return self._field_variable_value
