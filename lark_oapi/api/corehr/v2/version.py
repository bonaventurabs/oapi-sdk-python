from .resource import *


class V2(object):
    def __init__(self, config: Config) -> None:
        self.basic_info_bank: BasicInfoBank = BasicInfoBank(config)
        self.basic_info_bank_branch: BasicInfoBankBranch = BasicInfoBankBranch(config)
        self.basic_info_city: BasicInfoCity = BasicInfoCity(config)
        self.basic_info_country_region: BasicInfoCountryRegion = BasicInfoCountryRegion(config)
        self.basic_info_country_region_subdivision: BasicInfoCountryRegionSubdivision = BasicInfoCountryRegionSubdivision(
            config)
        self.basic_info_currency: BasicInfoCurrency = BasicInfoCurrency(config)
        self.basic_info_district: BasicInfoDistrict = BasicInfoDistrict(config)
        self.basic_info_language: BasicInfoLanguage = BasicInfoLanguage(config)
        self.basic_info_nationality: BasicInfoNationality = BasicInfoNationality(config)
        self.basic_info_time_zone: BasicInfoTimeZone = BasicInfoTimeZone(config)
        self.bp: Bp = Bp(config)
        self.company: Company = Company(config)
        self.contract: Contract = Contract(config)
        self.cost_center: CostCenter = CostCenter(config)
        self.cost_center_version: CostCenterVersion = CostCenterVersion(config)
        self.department: Department = Department(config)
        self.employee: Employee = Employee(config)
        self.employees_bp: EmployeesBp = EmployeesBp(config)
        self.employees_job_data: EmployeesJobData = EmployeesJobData(config)
        self.job: Job = Job(config)
        self.job_change: JobChange = JobChange(config)
        self.job_family: JobFamily = JobFamily(config)
        self.job_grade: JobGrade = JobGrade(config)
        self.job_level: JobLevel = JobLevel(config)
        self.location: Location = Location(config)
        self.offboarding: Offboarding = Offboarding(config)
        self.person: Person = Person(config)
        self.pre_hire: PreHire = PreHire(config)
        self.probation: Probation = Probation(config)
        self.probation_assessment: ProbationAssessment = ProbationAssessment(config)
        self.process: Process = Process(config)
        self.process_approver: ProcessApprover = ProcessApprover(config)
        self.process_cc: ProcessCc = ProcessCc(config)
        self.process_form_variable_data: ProcessFormVariableData = ProcessFormVariableData(config)
        self.process_node: ProcessNode = ProcessNode(config)
        self.process_status: ProcessStatus = ProcessStatus(config)
        self.workforce_plan_detail: WorkforcePlanDetail = WorkforcePlanDetail(config)
