# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum
from .basic_job_data import BasicJobData
from .basic_job_data import BasicJobData
from .basic_job_data import BasicJobData
from .job_data_cost_center import JobDataCostCenter
from .enum import Enum
from .enum import Enum
from .custom_field_data import CustomFieldData


class JobData(object):
    _types = {
        "job_data_id": str,
        "version_id": str,
        "employee_type_id": str,
        "working_hours_type_id": str,
        "work_location_id": str,
        "department_id": str,
        "position_id": str,
        "job_id": str,
        "job_level_id": str,
        "job_grade_id": str,
        "job_family_id": str,
        "probation_start_date": str,
        "probation_end_date": str,
        "primary_job_data": bool,
        "employment_id": str,
        "effective_time": str,
        "expiration_time": str,
        "assignment_start_reason": Enum,
        "probation_expected_end_date": str,
        "probation_outcome": Enum,
        "direct_manager": BasicJobData,
        "dotted_line_managers": List[BasicJobData],
        "second_direct_manager": BasicJobData,
        "cost_center_rates": List[JobDataCostCenter],
        "work_shift": Enum,
        "compensation_type": Enum,
        "service_company": str,
        "created_at": str,
        "weekly_working_hours_v2": str,
        "employee_subtype_id": str,
    }

    def __init__(self, d=None):
        self.job_data_id: Optional[str] = None
        self.version_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.working_hours_type_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.position_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.job_grade_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.probation_start_date: Optional[str] = None
        self.probation_end_date: Optional[str] = None
        self.primary_job_data: Optional[bool] = None
        self.employment_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.assignment_start_reason: Optional[Enum] = None
        self.probation_expected_end_date: Optional[str] = None
        self.probation_outcome: Optional[Enum] = None
        self.direct_manager: Optional[BasicJobData] = None
        self.dotted_line_managers: Optional[List[BasicJobData]] = None
        self.second_direct_manager: Optional[BasicJobData] = None
        self.cost_center_rates: Optional[List[JobDataCostCenter]] = None
        self.work_shift: Optional[Enum] = None
        self.compensation_type: Optional[Enum] = None
        self.service_company: Optional[str] = None
        self.created_at: Optional[str] = None
        self.weekly_working_hours_v2: Optional[str] = None
        self.employee_subtype_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDataBuilder":
        return JobDataBuilder()


class JobDataBuilder(object):
    def __init__(self) -> None:
        self._job_data = JobData()

    def job_data_id(self, job_data_id: str) -> "JobDataBuilder":
        self._job_data.job_data_id = job_data_id
        return self

    def version_id(self, version_id: str) -> "JobDataBuilder":
        self._job_data.version_id = version_id
        return self

    def employee_type_id(self, employee_type_id: str) -> "JobDataBuilder":
        self._job_data.employee_type_id = employee_type_id
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "JobDataBuilder":
        self._job_data.working_hours_type_id = working_hours_type_id
        return self

    def work_location_id(self, work_location_id: str) -> "JobDataBuilder":
        self._job_data.work_location_id = work_location_id
        return self

    def department_id(self, department_id: str) -> "JobDataBuilder":
        self._job_data.department_id = department_id
        return self

    def position_id(self, position_id: str) -> "JobDataBuilder":
        self._job_data.position_id = position_id
        return self

    def job_id(self, job_id: str) -> "JobDataBuilder":
        self._job_data.job_id = job_id
        return self

    def job_level_id(self, job_level_id: str) -> "JobDataBuilder":
        self._job_data.job_level_id = job_level_id
        return self

    def job_grade_id(self, job_grade_id: str) -> "JobDataBuilder":
        self._job_data.job_grade_id = job_grade_id
        return self

    def job_family_id(self, job_family_id: str) -> "JobDataBuilder":
        self._job_data.job_family_id = job_family_id
        return self

    def probation_start_date(self, probation_start_date: str) -> "JobDataBuilder":
        self._job_data.probation_start_date = probation_start_date
        return self

    def probation_end_date(self, probation_end_date: str) -> "JobDataBuilder":
        self._job_data.probation_end_date = probation_end_date
        return self

    def primary_job_data(self, primary_job_data: bool) -> "JobDataBuilder":
        self._job_data.primary_job_data = primary_job_data
        return self

    def employment_id(self, employment_id: str) -> "JobDataBuilder":
        self._job_data.employment_id = employment_id
        return self

    def effective_time(self, effective_time: str) -> "JobDataBuilder":
        self._job_data.effective_time = effective_time
        return self

    def expiration_time(self, expiration_time: str) -> "JobDataBuilder":
        self._job_data.expiration_time = expiration_time
        return self

    def assignment_start_reason(self, assignment_start_reason: Enum) -> "JobDataBuilder":
        self._job_data.assignment_start_reason = assignment_start_reason
        return self

    def probation_expected_end_date(self, probation_expected_end_date: str) -> "JobDataBuilder":
        self._job_data.probation_expected_end_date = probation_expected_end_date
        return self

    def probation_outcome(self, probation_outcome: Enum) -> "JobDataBuilder":
        self._job_data.probation_outcome = probation_outcome
        return self

    def direct_manager(self, direct_manager: BasicJobData) -> "JobDataBuilder":
        self._job_data.direct_manager = direct_manager
        return self

    def dotted_line_managers(self, dotted_line_managers: List[BasicJobData]) -> "JobDataBuilder":
        self._job_data.dotted_line_managers = dotted_line_managers
        return self

    def second_direct_manager(self, second_direct_manager: BasicJobData) -> "JobDataBuilder":
        self._job_data.second_direct_manager = second_direct_manager
        return self

    def cost_center_rates(self, cost_center_rates: List[JobDataCostCenter]) -> "JobDataBuilder":
        self._job_data.cost_center_rates = cost_center_rates
        return self

    def work_shift(self, work_shift: Enum) -> "JobDataBuilder":
        self._job_data.work_shift = work_shift
        return self

    def compensation_type(self, compensation_type: Enum) -> "JobDataBuilder":
        self._job_data.compensation_type = compensation_type
        return self

    def service_company(self, service_company: str) -> "JobDataBuilder":
        self._job_data.service_company = service_company
        return self

    def created_at(self, created_at: str) -> "JobDataBuilder":
        self._job_data.created_at = created_at
        return self

    def weekly_working_hours_v2(self, weekly_working_hours_v2: str) -> "JobDataBuilder":
        self._job_data.weekly_working_hours_v2 = weekly_working_hours_v2
        return self

    def employee_subtype_id(self, employee_subtype_id: str) -> "JobDataBuilder":
        self._job_data.employee_subtype_id = employee_subtype_id
        return self

    def build(self) -> "JobData":
        return self._job_data
