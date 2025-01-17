# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .assigned_organization_with_code import AssignedOrganizationWithCode


class AddRoleAssignAuthorizationRequestBody(object):
    _types = {
        "assigned_organization_items": List[list],
    }

    def __init__(self, d=None):
        self.assigned_organization_items: Optional[List[list]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddRoleAssignAuthorizationRequestBodyBuilder":
        return AddRoleAssignAuthorizationRequestBodyBuilder()


class AddRoleAssignAuthorizationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_role_assign_authorization_request_body = AddRoleAssignAuthorizationRequestBody()

    def assigned_organization_items(self, assigned_organization_items: List[
        list]) -> "AddRoleAssignAuthorizationRequestBodyBuilder":
        self._add_role_assign_authorization_request_body.assigned_organization_items = assigned_organization_items
        return self

    def build(self) -> "AddRoleAssignAuthorizationRequestBody":
        return self._add_role_assign_authorization_request_body
