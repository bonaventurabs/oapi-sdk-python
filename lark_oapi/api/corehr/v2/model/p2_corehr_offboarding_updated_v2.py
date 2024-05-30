# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2CorehrOffboardingUpdatedV2Data(object):
    _types = {
        "tenant_id": str,
        "offboarding_info_id": str,
        "process_id": str,
        "checklist_process_id": str,
        "employment_id": str,
        "operator": str,
        "status": int,
        "checklist_status": int,
        "updated_time": str,
        "updated_fields": List[str],
        "target_user_id": UserId,
    }

    def __init__(self, d=None):
        self.tenant_id: Optional[str] = None
        self.offboarding_info_id: Optional[str] = None
        self.process_id: Optional[str] = None
        self.checklist_process_id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.operator: Optional[str] = None
        self.status: Optional[int] = None
        self.checklist_status: Optional[int] = None
        self.updated_time: Optional[str] = None
        self.updated_fields: Optional[List[str]] = None
        self.target_user_id: Optional[UserId] = None
        init(self, d, self._types)


class P2CorehrOffboardingUpdatedV2(EventContext):
    _types = {
        "event": P2CorehrOffboardingUpdatedV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrOffboardingUpdatedV2Data] = None
        init(self, d, self._types)
