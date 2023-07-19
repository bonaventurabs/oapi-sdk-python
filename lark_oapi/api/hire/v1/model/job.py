# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .code_name_object import CodeNameObject
from .id_name_object import IdNameObject
from .job_category import JobCategory
from .job_city import JobCity
from .job_customized_data import JobCustomizedData
from .job_department import JobDepartment
from .job_highlight import JobHighlight
from .job_level import JobLevel
from .job_recruitment_type import JobRecruitmentType
from .job_type import JobType


class Job(object):
    _types = {
        "id": str,
        "title": str,
        "description": str,
        "code": str,
        "requirement": str,
        "recruitment_type": JobRecruitmentType,
        "department": JobDepartment,
        "city": JobCity,
        "min_job_level": JobLevel,
        "max_job_level": JobLevel,
        "highlight_list": List[JobHighlight],
        "job_category": JobCategory,
        "job_type": JobType,
        "active_status": int,
        "create_user_id": str,
        "create_time": int,
        "update_time": int,
        "process_type": int,
        "process_id": str,
        "process_name": str,
        "process_en_name": str,
        "customized_data_list": List[JobCustomizedData],
        "job_function": IdNameObject,
        "subject": IdNameObject,
        "head_count": int,
        "experience": int,
        "expiry_time": int,
        "min_salary": int,
        "max_salary": int,
        "required_degree": int,
        "city_list": List[CodeNameObject],
        "job_attribute": int,
        "create_timestamp": str,
        "update_timestamp": str,
        "expiry_timestamp": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        self.code: Optional[str] = None
        self.requirement: Optional[str] = None
        self.recruitment_type: Optional[JobRecruitmentType] = None
        self.department: Optional[JobDepartment] = None
        self.city: Optional[JobCity] = None
        self.min_job_level: Optional[JobLevel] = None
        self.max_job_level: Optional[JobLevel] = None
        self.highlight_list: Optional[List[JobHighlight]] = None
        self.job_category: Optional[JobCategory] = None
        self.job_type: Optional[JobType] = None
        self.active_status: Optional[int] = None
        self.create_user_id: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.process_type: Optional[int] = None
        self.process_id: Optional[str] = None
        self.process_name: Optional[str] = None
        self.process_en_name: Optional[str] = None
        self.customized_data_list: Optional[List[JobCustomizedData]] = None
        self.job_function: Optional[IdNameObject] = None
        self.subject: Optional[IdNameObject] = None
        self.head_count: Optional[int] = None
        self.experience: Optional[int] = None
        self.expiry_time: Optional[int] = None
        self.min_salary: Optional[int] = None
        self.max_salary: Optional[int] = None
        self.required_degree: Optional[int] = None
        self.city_list: Optional[List[CodeNameObject]] = None
        self.job_attribute: Optional[int] = None
        self.create_timestamp: Optional[str] = None
        self.update_timestamp: Optional[str] = None
        self.expiry_timestamp: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobBuilder":
        return JobBuilder()


class JobBuilder(object):
    def __init__(self, job: Job = Job({})) -> None:
        self._job: Job = job

    def id(self, id: str) -> "JobBuilder":
        self._job.id = id
        return self

    def title(self, title: str) -> "JobBuilder":
        self._job.title = title
        return self

    def description(self, description: str) -> "JobBuilder":
        self._job.description = description
        return self

    def code(self, code: str) -> "JobBuilder":
        self._job.code = code
        return self

    def requirement(self, requirement: str) -> "JobBuilder":
        self._job.requirement = requirement
        return self

    def recruitment_type(self, recruitment_type: JobRecruitmentType) -> "JobBuilder":
        self._job.recruitment_type = recruitment_type
        return self

    def department(self, department: JobDepartment) -> "JobBuilder":
        self._job.department = department
        return self

    def city(self, city: JobCity) -> "JobBuilder":
        self._job.city = city
        return self

    def min_job_level(self, min_job_level: JobLevel) -> "JobBuilder":
        self._job.min_job_level = min_job_level
        return self

    def max_job_level(self, max_job_level: JobLevel) -> "JobBuilder":
        self._job.max_job_level = max_job_level
        return self

    def highlight_list(self, highlight_list: List[JobHighlight]) -> "JobBuilder":
        self._job.highlight_list = highlight_list
        return self

    def job_category(self, job_category: JobCategory) -> "JobBuilder":
        self._job.job_category = job_category
        return self

    def job_type(self, job_type: JobType) -> "JobBuilder":
        self._job.job_type = job_type
        return self

    def active_status(self, active_status: int) -> "JobBuilder":
        self._job.active_status = active_status
        return self

    def create_user_id(self, create_user_id: str) -> "JobBuilder":
        self._job.create_user_id = create_user_id
        return self

    def create_time(self, create_time: int) -> "JobBuilder":
        self._job.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "JobBuilder":
        self._job.update_time = update_time
        return self

    def process_type(self, process_type: int) -> "JobBuilder":
        self._job.process_type = process_type
        return self

    def process_id(self, process_id: str) -> "JobBuilder":
        self._job.process_id = process_id
        return self

    def process_name(self, process_name: str) -> "JobBuilder":
        self._job.process_name = process_name
        return self

    def process_en_name(self, process_en_name: str) -> "JobBuilder":
        self._job.process_en_name = process_en_name
        return self

    def customized_data_list(self, customized_data_list: List[JobCustomizedData]) -> "JobBuilder":
        self._job.customized_data_list = customized_data_list
        return self

    def job_function(self, job_function: IdNameObject) -> "JobBuilder":
        self._job.job_function = job_function
        return self

    def subject(self, subject: IdNameObject) -> "JobBuilder":
        self._job.subject = subject
        return self

    def head_count(self, head_count: int) -> "JobBuilder":
        self._job.head_count = head_count
        return self

    def experience(self, experience: int) -> "JobBuilder":
        self._job.experience = experience
        return self

    def expiry_time(self, expiry_time: int) -> "JobBuilder":
        self._job.expiry_time = expiry_time
        return self

    def min_salary(self, min_salary: int) -> "JobBuilder":
        self._job.min_salary = min_salary
        return self

    def max_salary(self, max_salary: int) -> "JobBuilder":
        self._job.max_salary = max_salary
        return self

    def required_degree(self, required_degree: int) -> "JobBuilder":
        self._job.required_degree = required_degree
        return self

    def city_list(self, city_list: List[CodeNameObject]) -> "JobBuilder":
        self._job.city_list = city_list
        return self

    def job_attribute(self, job_attribute: int) -> "JobBuilder":
        self._job.job_attribute = job_attribute
        return self

    def create_timestamp(self, create_timestamp: str) -> "JobBuilder":
        self._job.create_timestamp = create_timestamp
        return self

    def update_timestamp(self, update_timestamp: str) -> "JobBuilder":
        self._job.update_timestamp = update_timestamp
        return self

    def expiry_timestamp(self, expiry_timestamp: str) -> "JobBuilder":
        self._job.expiry_timestamp = expiry_timestamp
        return self

    def build(self) -> "Job":
        return self._job