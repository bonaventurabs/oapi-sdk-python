# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FindReplaceResult(object):
    _types = {
        "matched_cells": List[str],
        "matched_formula_cells": List[str],
        "rows_count": int,
    }

    def __init__(self, d):
        self.matched_cells: Optional[List[str]] = None
        self.matched_formula_cells: Optional[List[str]] = None
        self.rows_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FindReplaceResultBuilder":
        return FindReplaceResultBuilder()


class FindReplaceResultBuilder(object):
    def __init__(self, find_replace_result: FindReplaceResult = FindReplaceResult({})) -> None:
        self._find_replace_result: FindReplaceResult = find_replace_result

    def matched_cells(self, matched_cells: List[str]) -> "FindReplaceResultBuilder":
        self._find_replace_result.matched_cells = matched_cells
        return self

    def matched_formula_cells(self, matched_formula_cells: List[str]) -> "FindReplaceResultBuilder":
        self._find_replace_result.matched_formula_cells = matched_formula_cells
        return self

    def rows_count(self, rows_count: int) -> "FindReplaceResultBuilder":
        self._find_replace_result.rows_count = rows_count
        return self

    def build(self) -> "FindReplaceResult":
        return self._find_replace_result