# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class EcoBackgroundCheckPackageAdditionalItem(object):
    _types = {
        "id": str,
        "name": str,
        "description": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoBackgroundCheckPackageAdditionalItemBuilder":
        return EcoBackgroundCheckPackageAdditionalItemBuilder()


class EcoBackgroundCheckPackageAdditionalItemBuilder(object):
    def __init__(self,
                 eco_background_check_package_additional_item: EcoBackgroundCheckPackageAdditionalItem = EcoBackgroundCheckPackageAdditionalItem(
                     {})) -> None:
        self._eco_background_check_package_additional_item: EcoBackgroundCheckPackageAdditionalItem = eco_background_check_package_additional_item

    def id(self, id: str) -> "EcoBackgroundCheckPackageAdditionalItemBuilder":
        self._eco_background_check_package_additional_item.id = id
        return self

    def name(self, name: str) -> "EcoBackgroundCheckPackageAdditionalItemBuilder":
        self._eco_background_check_package_additional_item.name = name
        return self

    def description(self, description: str) -> "EcoBackgroundCheckPackageAdditionalItemBuilder":
        self._eco_background_check_package_additional_item.description = description
        return self

    def build(self) -> "EcoBackgroundCheckPackageAdditionalItem":
        return self._eco_background_check_package_additional_item