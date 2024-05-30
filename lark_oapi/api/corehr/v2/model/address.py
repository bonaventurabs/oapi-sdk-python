# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .custom_field_data import CustomFieldData


class Address(object):
    _types = {
        "full_address_local_script": str,
        "full_address_western_script": str,
        "address_id": str,
        "country_region_id": str,
        "region_id": str,
        "address_line1": str,
        "address_line2": str,
        "address_line3": str,
        "address_line4": str,
        "address_line5": str,
        "address_line6": str,
        "address_line7": str,
        "address_line8": str,
        "address_line9": str,
        "local_address_line1": str,
        "local_address_line2": str,
        "local_address_line3": str,
        "local_address_line4": str,
        "local_address_line5": str,
        "local_address_line6": str,
        "local_address_line7": str,
        "local_address_line8": str,
        "local_address_line9": str,
        "postal_code": str,
        "address_type_list": List[Enum],
        "is_primary": bool,
        "is_public": bool,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d=None):
        self.full_address_local_script: Optional[str] = None
        self.full_address_western_script: Optional[str] = None
        self.address_id: Optional[str] = None
        self.country_region_id: Optional[str] = None
        self.region_id: Optional[str] = None
        self.address_line1: Optional[str] = None
        self.address_line2: Optional[str] = None
        self.address_line3: Optional[str] = None
        self.address_line4: Optional[str] = None
        self.address_line5: Optional[str] = None
        self.address_line6: Optional[str] = None
        self.address_line7: Optional[str] = None
        self.address_line8: Optional[str] = None
        self.address_line9: Optional[str] = None
        self.local_address_line1: Optional[str] = None
        self.local_address_line2: Optional[str] = None
        self.local_address_line3: Optional[str] = None
        self.local_address_line4: Optional[str] = None
        self.local_address_line5: Optional[str] = None
        self.local_address_line6: Optional[str] = None
        self.local_address_line7: Optional[str] = None
        self.local_address_line8: Optional[str] = None
        self.local_address_line9: Optional[str] = None
        self.postal_code: Optional[str] = None
        self.address_type_list: Optional[List[Enum]] = None
        self.is_primary: Optional[bool] = None
        self.is_public: Optional[bool] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddressBuilder":
        return AddressBuilder()


class AddressBuilder(object):
    def __init__(self) -> None:
        self._address = Address()

    def full_address_local_script(self, full_address_local_script: str) -> "AddressBuilder":
        self._address.full_address_local_script = full_address_local_script
        return self

    def full_address_western_script(self, full_address_western_script: str) -> "AddressBuilder":
        self._address.full_address_western_script = full_address_western_script
        return self

    def address_id(self, address_id: str) -> "AddressBuilder":
        self._address.address_id = address_id
        return self

    def country_region_id(self, country_region_id: str) -> "AddressBuilder":
        self._address.country_region_id = country_region_id
        return self

    def region_id(self, region_id: str) -> "AddressBuilder":
        self._address.region_id = region_id
        return self

    def address_line1(self, address_line1: str) -> "AddressBuilder":
        self._address.address_line1 = address_line1
        return self

    def address_line2(self, address_line2: str) -> "AddressBuilder":
        self._address.address_line2 = address_line2
        return self

    def address_line3(self, address_line3: str) -> "AddressBuilder":
        self._address.address_line3 = address_line3
        return self

    def address_line4(self, address_line4: str) -> "AddressBuilder":
        self._address.address_line4 = address_line4
        return self

    def address_line5(self, address_line5: str) -> "AddressBuilder":
        self._address.address_line5 = address_line5
        return self

    def address_line6(self, address_line6: str) -> "AddressBuilder":
        self._address.address_line6 = address_line6
        return self

    def address_line7(self, address_line7: str) -> "AddressBuilder":
        self._address.address_line7 = address_line7
        return self

    def address_line8(self, address_line8: str) -> "AddressBuilder":
        self._address.address_line8 = address_line8
        return self

    def address_line9(self, address_line9: str) -> "AddressBuilder":
        self._address.address_line9 = address_line9
        return self

    def local_address_line1(self, local_address_line1: str) -> "AddressBuilder":
        self._address.local_address_line1 = local_address_line1
        return self

    def local_address_line2(self, local_address_line2: str) -> "AddressBuilder":
        self._address.local_address_line2 = local_address_line2
        return self

    def local_address_line3(self, local_address_line3: str) -> "AddressBuilder":
        self._address.local_address_line3 = local_address_line3
        return self

    def local_address_line4(self, local_address_line4: str) -> "AddressBuilder":
        self._address.local_address_line4 = local_address_line4
        return self

    def local_address_line5(self, local_address_line5: str) -> "AddressBuilder":
        self._address.local_address_line5 = local_address_line5
        return self

    def local_address_line6(self, local_address_line6: str) -> "AddressBuilder":
        self._address.local_address_line6 = local_address_line6
        return self

    def local_address_line7(self, local_address_line7: str) -> "AddressBuilder":
        self._address.local_address_line7 = local_address_line7
        return self

    def local_address_line8(self, local_address_line8: str) -> "AddressBuilder":
        self._address.local_address_line8 = local_address_line8
        return self

    def local_address_line9(self, local_address_line9: str) -> "AddressBuilder":
        self._address.local_address_line9 = local_address_line9
        return self

    def postal_code(self, postal_code: str) -> "AddressBuilder":
        self._address.postal_code = postal_code
        return self

    def address_type_list(self, address_type_list: List[Enum]) -> "AddressBuilder":
        self._address.address_type_list = address_type_list
        return self

    def is_primary(self, is_primary: bool) -> "AddressBuilder":
        self._address.is_primary = is_primary
        return self

    def is_public(self, is_public: bool) -> "AddressBuilder":
        self._address.is_public = is_public
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "AddressBuilder":
        self._address.custom_fields = custom_fields
        return self

    def build(self) -> "Address":
        return self._address
