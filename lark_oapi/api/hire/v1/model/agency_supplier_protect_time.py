# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AgencySupplierProtectTime(object):
    _types = {
        "day": int,
        "use_default": bool,
    }

    def __init__(self, d=None):
        self.day: Optional[int] = None
        self.use_default: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgencySupplierProtectTimeBuilder":
        return AgencySupplierProtectTimeBuilder()


class AgencySupplierProtectTimeBuilder(object):
    def __init__(self) -> None:
        self._agency_supplier_protect_time = AgencySupplierProtectTime()

    def day(self, day: int) -> "AgencySupplierProtectTimeBuilder":
        self._agency_supplier_protect_time.day = day
        return self

    def use_default(self, use_default: bool) -> "AgencySupplierProtectTimeBuilder":
        self._agency_supplier_protect_time.use_default = use_default
        return self

    def build(self) -> "AgencySupplierProtectTime":
        return self._agency_supplier_protect_time