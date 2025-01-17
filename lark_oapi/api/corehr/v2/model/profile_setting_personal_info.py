# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_personal_basic_info import ProfileSettingPersonalBasicInfo
from .profile_setting_emergency_contact import ProfileSettingEmergencyContact
from .profile_setting_bank_account import ProfileSettingBankAccount
from .profile_setting_national import ProfileSettingNational
from .profile_setting_resident_tax import ProfileSettingResidentTax
from .profile_setting_dependent import ProfileSettingDependent
from .profile_setting_hukou import ProfileSettingHukou
from .profile_setting_address import ProfileSettingAddress
from .profile_setting_custom_group import ProfileSettingCustomGroup
from .profile_setting_citizenship_status import ProfileSettingCitizenshipStatus


class ProfileSettingPersonalInfo(object):
    _types = {
        "personal_basic_info": ProfileSettingPersonalBasicInfo,
        "emergency_contacts": List[ProfileSettingEmergencyContact],
        "bank_accounts": List[ProfileSettingBankAccount],
        "nationals": List[ProfileSettingNational],
        "resident_taxes": List[ProfileSettingResidentTax],
        "dependents": List[ProfileSettingDependent],
        "hukou": ProfileSettingHukou,
        "contact_addresses": List[ProfileSettingAddress],
        "custom_groups": List[ProfileSettingCustomGroup],
        "citizenship_statuses": List[ProfileSettingCitizenshipStatus],
    }

    def __init__(self, d=None):
        self.personal_basic_info: Optional[ProfileSettingPersonalBasicInfo] = None
        self.emergency_contacts: Optional[List[ProfileSettingEmergencyContact]] = None
        self.bank_accounts: Optional[List[ProfileSettingBankAccount]] = None
        self.nationals: Optional[List[ProfileSettingNational]] = None
        self.resident_taxes: Optional[List[ProfileSettingResidentTax]] = None
        self.dependents: Optional[List[ProfileSettingDependent]] = None
        self.hukou: Optional[ProfileSettingHukou] = None
        self.contact_addresses: Optional[List[ProfileSettingAddress]] = None
        self.custom_groups: Optional[List[ProfileSettingCustomGroup]] = None
        self.citizenship_statuses: Optional[List[ProfileSettingCitizenshipStatus]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingPersonalInfoBuilder":
        return ProfileSettingPersonalInfoBuilder()


class ProfileSettingPersonalInfoBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_personal_info = ProfileSettingPersonalInfo()

    def personal_basic_info(self,
                            personal_basic_info: ProfileSettingPersonalBasicInfo) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.personal_basic_info = personal_basic_info
        return self

    def emergency_contacts(self, emergency_contacts: List[
        ProfileSettingEmergencyContact]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.emergency_contacts = emergency_contacts
        return self

    def bank_accounts(self, bank_accounts: List[ProfileSettingBankAccount]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.bank_accounts = bank_accounts
        return self

    def nationals(self, nationals: List[ProfileSettingNational]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.nationals = nationals
        return self

    def resident_taxes(self, resident_taxes: List[ProfileSettingResidentTax]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.resident_taxes = resident_taxes
        return self

    def dependents(self, dependents: List[ProfileSettingDependent]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.dependents = dependents
        return self

    def hukou(self, hukou: ProfileSettingHukou) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.hukou = hukou
        return self

    def contact_addresses(self, contact_addresses: List[ProfileSettingAddress]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.contact_addresses = contact_addresses
        return self

    def custom_groups(self, custom_groups: List[ProfileSettingCustomGroup]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.custom_groups = custom_groups
        return self

    def citizenship_statuses(self, citizenship_statuses: List[
        ProfileSettingCitizenshipStatus]) -> "ProfileSettingPersonalInfoBuilder":
        self._profile_setting_personal_info.citizenship_statuses = citizenship_statuses
        return self

    def build(self) -> "ProfileSettingPersonalInfo":
        return self._profile_setting_personal_info
