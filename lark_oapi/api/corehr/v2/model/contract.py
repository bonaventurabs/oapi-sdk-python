# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum
from .enum import Enum
from .enum import Enum
from .enum import Enum


class Contract(object):
    _types = {
        "id": str,
        "effective_time": str,
        "contract_end_date": str,
        "expiration_time": str,
        "employment_id": str,
        "contract_type": Enum,
        "first_party_company_id": str,
        "person_id": str,
        "duration_type": Enum,
        "contract_number": str,
        "signing_type": Enum,
        "contract_status": Enum,
        "renewal_status": Enum,
        "signing_times": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.contract_end_date: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.contract_type: Optional[Enum] = None
        self.first_party_company_id: Optional[str] = None
        self.person_id: Optional[str] = None
        self.duration_type: Optional[Enum] = None
        self.contract_number: Optional[str] = None
        self.signing_type: Optional[Enum] = None
        self.contract_status: Optional[Enum] = None
        self.renewal_status: Optional[Enum] = None
        self.signing_times: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContractBuilder":
        return ContractBuilder()


class ContractBuilder(object):
    def __init__(self) -> None:
        self._contract = Contract()

    def id(self, id: str) -> "ContractBuilder":
        self._contract.id = id
        return self

    def effective_time(self, effective_time: str) -> "ContractBuilder":
        self._contract.effective_time = effective_time
        return self

    def contract_end_date(self, contract_end_date: str) -> "ContractBuilder":
        self._contract.contract_end_date = contract_end_date
        return self

    def expiration_time(self, expiration_time: str) -> "ContractBuilder":
        self._contract.expiration_time = expiration_time
        return self

    def employment_id(self, employment_id: str) -> "ContractBuilder":
        self._contract.employment_id = employment_id
        return self

    def contract_type(self, contract_type: Enum) -> "ContractBuilder":
        self._contract.contract_type = contract_type
        return self

    def first_party_company_id(self, first_party_company_id: str) -> "ContractBuilder":
        self._contract.first_party_company_id = first_party_company_id
        return self

    def person_id(self, person_id: str) -> "ContractBuilder":
        self._contract.person_id = person_id
        return self

    def duration_type(self, duration_type: Enum) -> "ContractBuilder":
        self._contract.duration_type = duration_type
        return self

    def contract_number(self, contract_number: str) -> "ContractBuilder":
        self._contract.contract_number = contract_number
        return self

    def signing_type(self, signing_type: Enum) -> "ContractBuilder":
        self._contract.signing_type = signing_type
        return self

    def contract_status(self, contract_status: Enum) -> "ContractBuilder":
        self._contract.contract_status = contract_status
        return self

    def renewal_status(self, renewal_status: Enum) -> "ContractBuilder":
        self._contract.renewal_status = renewal_status
        return self

    def signing_times(self, signing_times: int) -> "ContractBuilder":
        self._contract.signing_times = signing_times
        return self

    def build(self) -> "Contract":
        return self._contract
