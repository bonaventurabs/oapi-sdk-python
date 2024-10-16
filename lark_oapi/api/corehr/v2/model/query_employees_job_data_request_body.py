# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryEmployeesJobDataRequestBody(object):
    _types = {
        "get_all_version": bool,
        "data_date": str,
        "effective_date_start": str,
        "effective_date_end": str,
        "department_id": str,
        "employment_ids": List[str],
    }

    def __init__(self, d=None):
        self.get_all_version: Optional[bool] = None
        self.data_date: Optional[str] = None
        self.effective_date_start: Optional[str] = None
        self.effective_date_end: Optional[str] = None
        self.department_id: Optional[str] = None
        self.employment_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryEmployeesJobDataRequestBodyBuilder":
        return QueryEmployeesJobDataRequestBodyBuilder()


class QueryEmployeesJobDataRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_employees_job_data_request_body = QueryEmployeesJobDataRequestBody()

    def get_all_version(self, get_all_version: bool) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.get_all_version = get_all_version
        return self

    def data_date(self, data_date: str) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.data_date = data_date
        return self

    def effective_date_start(self, effective_date_start: str) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.effective_date_start = effective_date_start
        return self

    def effective_date_end(self, effective_date_end: str) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.effective_date_end = effective_date_end
        return self

    def department_id(self, department_id: str) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.department_id = department_id
        return self

    def employment_ids(self, employment_ids: List[str]) -> "QueryEmployeesJobDataRequestBodyBuilder":
        self._query_employees_job_data_request_body.employment_ids = employment_ids
        return self

    def build(self) -> "QueryEmployeesJobDataRequestBody":
        return self._query_employees_job_data_request_body
