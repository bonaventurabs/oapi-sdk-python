from .resource import *


class V1(object):
    def __init__(self, config: Config) -> None:
        self.assigned_user: AssignedUser = AssignedUser(config)
        self.common_data_id: CommonDataId = CommonDataId(config)
        self.company: Company = Company(config)
        self.compensation_standard: CompensationStandard = CompensationStandard(config)
        self.contract: Contract = Contract(config)
        self.country_region: CountryRegion = CountryRegion(config)
        self.currency: Currency = Currency(config)
        self.custom_field: CustomField = CustomField(config)
        self.department: Department = Department(config)
        self.employee_type: EmployeeType = EmployeeType(config)
        self.employment: Employment = Employment(config)
        self.file: File = File(config)
        self.job: Job = Job(config)
        self.job_change: JobChange = JobChange(config)
        self.job_data: JobData = JobData(config)
        self.job_family: JobFamily = JobFamily(config)
        self.job_level: JobLevel = JobLevel(config)
        self.leave: Leave = Leave(config)
        self.leave_granting_record: LeaveGrantingRecord = LeaveGrantingRecord(config)
        self.location: Location = Location(config)
        self.national_id_type: NationalIdType = NationalIdType(config)
        self.offboarding: Offboarding = Offboarding(config)
        self.org_role_authorization: OrgRoleAuthorization = OrgRoleAuthorization(config)
        self.person: Person = Person(config)
        self.pre_hire: PreHire = PreHire(config)
        self.process_form_variable_data: ProcessFormVariableData = ProcessFormVariableData(config)
        self.security_group: SecurityGroup = SecurityGroup(config)
        self.subdivision: Subdivision = Subdivision(config)
        self.subregion: Subregion = Subregion(config)
        self.transfer_reason: TransferReason = TransferReason(config)
        self.transfer_type: TransferType = TransferType(config)
        self.working_hours_type: WorkingHoursType = WorkingHoursType(config)
