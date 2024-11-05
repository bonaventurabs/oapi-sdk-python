# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .employee_job_level import EmployeeJobLevel
from .employee_job_family import EmployeeJobFamily
from .position import Position
from .job import Job
from .enum import Enum
from .enum import Enum
from .enum import Enum
from .work_email import WorkEmail
from .job_data_cost_center import JobDataCostCenter
from .enum import Enum
from .person_info import PersonInfo
from .custom_field_data import CustomFieldData
from .enum import Enum
from .enum import Enum
from .basic_department import BasicDepartment
from .basic_employee import BasicEmployee
from .basic_employee import BasicEmployee
from .international_assignment import InternationalAssignment
from .enum import Enum
from .enum import Enum


class Employee(object):
    _types = {
        "employment_id": str,
        "employment_id_v2": str,
        "ats_application_id": str,
        "prehire_id": str,
        "employee_number": str,
        "employee_type_id": str,
        "employee_subtype_id": str,
        "department_id": str,
        "department_id_v2": str,
        "job_level_id": str,
        "job_level": EmployeeJobLevel,
        "job_grade_id": str,
        "work_location_id": str,
        "job_family_id": str,
        "job_family": EmployeeJobFamily,
        "position_id": str,
        "position": Position,
        "job_id": str,
        "job": Job,
        "company_id": str,
        "working_hours_type_id": str,
        "tenure": str,
        "seniority_date": str,
        "effective_date": str,
        "primary_employment": bool,
        "probation_period": int,
        "on_probation": bool,
        "probation_end_date": str,
        "direct_manager_id": str,
        "dotted_line_manager_id": str,
        "direct_manager_id_v2": str,
        "dotted_line_manager_id_v2": str,
        "employment_type": Enum,
        "employment_status": Enum,
        "expiration_date": str,
        "reason_for_offboarding": Enum,
        "email_address": str,
        "work_email_list": List[WorkEmail],
        "cost_center_list": List[JobDataCostCenter],
        "rehire": Enum,
        "rehire_employment_id": str,
        "person_info": PersonInfo,
        "custom_fields": List[CustomFieldData],
        "noncompete_status": Enum,
        "past_offboarding": bool,
        "regular_employee_start_date": str,
        "external_id": str,
        "times_employed": int,
        "recruitment_type": Enum,
        "avatar_url": str,
        "primary_contract_id": str,
        "contract_start_date": str,
        "contract_end_date": str,
        "contract_expected_end_date": str,
        "pay_group_id": str,
        "international_assignment": bool,
        "work_calendar_id": str,
        "department": BasicDepartment,
        "direct_manager": BasicEmployee,
        "dotted_line_manager": BasicEmployee,
        "time_zone": str,
        "service_company": str,
        "compensation_type": Enum,
        "work_shift": Enum,
        "custom_org": str,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.employment_id_v2: Optional[str] = None
        self.ats_application_id: Optional[str] = None
        self.prehire_id: Optional[str] = None
        self.employee_number: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.employee_subtype_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.department_id_v2: Optional[str] = None
        self.job_level_id: Optional[str] = None
        self.job_level: Optional[EmployeeJobLevel] = None
        self.job_grade_id: Optional[str] = None
        self.work_location_id: Optional[str] = None
        self.job_family_id: Optional[str] = None
        self.job_family: Optional[EmployeeJobFamily] = None
        self.position_id: Optional[str] = None
        self.position: Optional[Position] = None
        self.job_id: Optional[str] = None
        self.job: Optional[Job] = None
        self.company_id: Optional[str] = None
        self.working_hours_type_id: Optional[str] = None
        self.tenure: Optional[str] = None
        self.seniority_date: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.primary_employment: Optional[bool] = None
        self.probation_period: Optional[int] = None
        self.on_probation: Optional[bool] = None
        self.probation_end_date: Optional[str] = None
        self.direct_manager_id: Optional[str] = None
        self.dotted_line_manager_id: Optional[str] = None
        self.direct_manager_id_v2: Optional[str] = None
        self.dotted_line_manager_id_v2: Optional[str] = None
        self.employment_type: Optional[Enum] = None
        self.employment_status: Optional[Enum] = None
        self.expiration_date: Optional[str] = None
        self.reason_for_offboarding: Optional[Enum] = None
        self.email_address: Optional[str] = None
        self.work_email_list: Optional[List[WorkEmail]] = None
        self.cost_center_list: Optional[List[JobDataCostCenter]] = None
        self.rehire: Optional[Enum] = None
        self.rehire_employment_id: Optional[str] = None
        self.person_info: Optional[PersonInfo] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        self.noncompete_status: Optional[Enum] = None
        self.past_offboarding: Optional[bool] = None
        self.regular_employee_start_date: Optional[str] = None
        self.external_id: Optional[str] = None
        self.times_employed: Optional[int] = None
        self.recruitment_type: Optional[Enum] = None
        self.avatar_url: Optional[str] = None
        self.primary_contract_id: Optional[str] = None
        self.contract_start_date: Optional[str] = None
        self.contract_end_date: Optional[str] = None
        self.contract_expected_end_date: Optional[str] = None
        self.pay_group_id: Optional[str] = None
        self.international_assignment: Optional[bool] = None
        self.work_calendar_id: Optional[str] = None
        self.department: Optional[BasicDepartment] = None
        self.direct_manager: Optional[BasicEmployee] = None
        self.dotted_line_manager: Optional[BasicEmployee] = None
        self.time_zone: Optional[str] = None
        self.service_company: Optional[str] = None
        self.compensation_type: Optional[Enum] = None
        self.work_shift: Optional[Enum] = None
        self.custom_org: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeBuilder":
        return EmployeeBuilder()


class EmployeeBuilder(object):
    def __init__(self) -> None:
        self._employee = Employee()

    def employment_id(self, employment_id: str) -> "EmployeeBuilder":
        self._employee.employment_id = employment_id
        return self

    def employment_id_v2(self, employment_id_v2: str) -> "EmployeeBuilder":
        self._employee.employment_id_v2 = employment_id_v2
        return self

    def ats_application_id(self, ats_application_id: str) -> "EmployeeBuilder":
        self._employee.ats_application_id = ats_application_id
        return self

    def prehire_id(self, prehire_id: str) -> "EmployeeBuilder":
        self._employee.prehire_id = prehire_id
        return self

    def employee_number(self, employee_number: str) -> "EmployeeBuilder":
        self._employee.employee_number = employee_number
        return self

    def employee_type_id(self, employee_type_id: str) -> "EmployeeBuilder":
        self._employee.employee_type_id = employee_type_id
        return self

    def employee_subtype_id(self, employee_subtype_id: str) -> "EmployeeBuilder":
        self._employee.employee_subtype_id = employee_subtype_id
        return self

    def department_id(self, department_id: str) -> "EmployeeBuilder":
        self._employee.department_id = department_id
        return self

    def department_id_v2(self, department_id_v2: str) -> "EmployeeBuilder":
        self._employee.department_id_v2 = department_id_v2
        return self

    def job_level_id(self, job_level_id: str) -> "EmployeeBuilder":
        self._employee.job_level_id = job_level_id
        return self

    def job_level(self, job_level: EmployeeJobLevel) -> "EmployeeBuilder":
        self._employee.job_level = job_level
        return self

    def job_grade_id(self, job_grade_id: str) -> "EmployeeBuilder":
        self._employee.job_grade_id = job_grade_id
        return self

    def work_location_id(self, work_location_id: str) -> "EmployeeBuilder":
        self._employee.work_location_id = work_location_id
        return self

    def job_family_id(self, job_family_id: str) -> "EmployeeBuilder":
        self._employee.job_family_id = job_family_id
        return self

    def job_family(self, job_family: EmployeeJobFamily) -> "EmployeeBuilder":
        self._employee.job_family = job_family
        return self

    def position_id(self, position_id: str) -> "EmployeeBuilder":
        self._employee.position_id = position_id
        return self

    def position(self, position: Position) -> "EmployeeBuilder":
        self._employee.position = position
        return self

    def job_id(self, job_id: str) -> "EmployeeBuilder":
        self._employee.job_id = job_id
        return self

    def job(self, job: Job) -> "EmployeeBuilder":
        self._employee.job = job
        return self

    def company_id(self, company_id: str) -> "EmployeeBuilder":
        self._employee.company_id = company_id
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "EmployeeBuilder":
        self._employee.working_hours_type_id = working_hours_type_id
        return self

    def tenure(self, tenure: str) -> "EmployeeBuilder":
        self._employee.tenure = tenure
        return self

    def seniority_date(self, seniority_date: str) -> "EmployeeBuilder":
        self._employee.seniority_date = seniority_date
        return self

    def effective_date(self, effective_date: str) -> "EmployeeBuilder":
        self._employee.effective_date = effective_date
        return self

    def primary_employment(self, primary_employment: bool) -> "EmployeeBuilder":
        self._employee.primary_employment = primary_employment
        return self

    def probation_period(self, probation_period: int) -> "EmployeeBuilder":
        self._employee.probation_period = probation_period
        return self

    def on_probation(self, on_probation: bool) -> "EmployeeBuilder":
        self._employee.on_probation = on_probation
        return self

    def probation_end_date(self, probation_end_date: str) -> "EmployeeBuilder":
        self._employee.probation_end_date = probation_end_date
        return self

    def direct_manager_id(self, direct_manager_id: str) -> "EmployeeBuilder":
        self._employee.direct_manager_id = direct_manager_id
        return self

    def dotted_line_manager_id(self, dotted_line_manager_id: str) -> "EmployeeBuilder":
        self._employee.dotted_line_manager_id = dotted_line_manager_id
        return self

    def direct_manager_id_v2(self, direct_manager_id_v2: str) -> "EmployeeBuilder":
        self._employee.direct_manager_id_v2 = direct_manager_id_v2
        return self

    def dotted_line_manager_id_v2(self, dotted_line_manager_id_v2: str) -> "EmployeeBuilder":
        self._employee.dotted_line_manager_id_v2 = dotted_line_manager_id_v2
        return self

    def employment_type(self, employment_type: Enum) -> "EmployeeBuilder":
        self._employee.employment_type = employment_type
        return self

    def employment_status(self, employment_status: Enum) -> "EmployeeBuilder":
        self._employee.employment_status = employment_status
        return self

    def expiration_date(self, expiration_date: str) -> "EmployeeBuilder":
        self._employee.expiration_date = expiration_date
        return self

    def reason_for_offboarding(self, reason_for_offboarding: Enum) -> "EmployeeBuilder":
        self._employee.reason_for_offboarding = reason_for_offboarding
        return self

    def email_address(self, email_address: str) -> "EmployeeBuilder":
        self._employee.email_address = email_address
        return self

    def work_email_list(self, work_email_list: List[WorkEmail]) -> "EmployeeBuilder":
        self._employee.work_email_list = work_email_list
        return self

    def cost_center_list(self, cost_center_list: List[JobDataCostCenter]) -> "EmployeeBuilder":
        self._employee.cost_center_list = cost_center_list
        return self

    def rehire(self, rehire: Enum) -> "EmployeeBuilder":
        self._employee.rehire = rehire
        return self

    def rehire_employment_id(self, rehire_employment_id: str) -> "EmployeeBuilder":
        self._employee.rehire_employment_id = rehire_employment_id
        return self

    def person_info(self, person_info: PersonInfo) -> "EmployeeBuilder":
        self._employee.person_info = person_info
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "EmployeeBuilder":
        self._employee.custom_fields = custom_fields
        return self

    def noncompete_status(self, noncompete_status: Enum) -> "EmployeeBuilder":
        self._employee.noncompete_status = noncompete_status
        return self

    def past_offboarding(self, past_offboarding: bool) -> "EmployeeBuilder":
        self._employee.past_offboarding = past_offboarding
        return self

    def regular_employee_start_date(self, regular_employee_start_date: str) -> "EmployeeBuilder":
        self._employee.regular_employee_start_date = regular_employee_start_date
        return self

    def external_id(self, external_id: str) -> "EmployeeBuilder":
        self._employee.external_id = external_id
        return self

    def times_employed(self, times_employed: int) -> "EmployeeBuilder":
        self._employee.times_employed = times_employed
        return self

    def recruitment_type(self, recruitment_type: Enum) -> "EmployeeBuilder":
        self._employee.recruitment_type = recruitment_type
        return self

    def avatar_url(self, avatar_url: str) -> "EmployeeBuilder":
        self._employee.avatar_url = avatar_url
        return self

    def primary_contract_id(self, primary_contract_id: str) -> "EmployeeBuilder":
        self._employee.primary_contract_id = primary_contract_id
        return self

    def contract_start_date(self, contract_start_date: str) -> "EmployeeBuilder":
        self._employee.contract_start_date = contract_start_date
        return self

    def contract_end_date(self, contract_end_date: str) -> "EmployeeBuilder":
        self._employee.contract_end_date = contract_end_date
        return self

    def contract_expected_end_date(self, contract_expected_end_date: str) -> "EmployeeBuilder":
        self._employee.contract_expected_end_date = contract_expected_end_date
        return self

    def pay_group_id(self, pay_group_id: str) -> "EmployeeBuilder":
        self._employee.pay_group_id = pay_group_id
        return self

    def international_assignment(self, international_assignment: bool) -> "EmployeeBuilder":
        self._employee.international_assignment = international_assignment
        return self

    def work_calendar_id(self, work_calendar_id: str) -> "EmployeeBuilder":
        self._employee.work_calendar_id = work_calendar_id
        return self

    def department(self, department: BasicDepartment) -> "EmployeeBuilder":
        self._employee.department = department
        return self

    def direct_manager(self, direct_manager: BasicEmployee) -> "EmployeeBuilder":
        self._employee.direct_manager = direct_manager
        return self

    def dotted_line_manager(self, dotted_line_manager: BasicEmployee) -> "EmployeeBuilder":
        self._employee.dotted_line_manager = dotted_line_manager
        return self

    def time_zone(self, time_zone: str) -> "EmployeeBuilder":
        self._employee.time_zone = time_zone
        return self

    def service_company(self, service_company: str) -> "EmployeeBuilder":
        self._employee.service_company = service_company
        return self

    def compensation_type(self, compensation_type: Enum) -> "EmployeeBuilder":
        self._employee.compensation_type = compensation_type
        return self

    def work_shift(self, work_shift: Enum) -> "EmployeeBuilder":
        self._employee.work_shift = work_shift
        return self

    def custom_org(self, custom_org: str) -> "EmployeeBuilder":
        self._employee.custom_org = custom_org
        return self

    def build(self) -> "Employee":
        return self._employee
