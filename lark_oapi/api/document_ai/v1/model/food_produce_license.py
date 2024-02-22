# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .food_produce_entity import FoodProduceEntity


class FoodProduceLicense(object):
    _types = {
        "entities": List[FoodProduceEntity],
    }

    def __init__(self, d=None):
        self.entities: Optional[List[FoodProduceEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FoodProduceLicenseBuilder":
        return FoodProduceLicenseBuilder()


class FoodProduceLicenseBuilder(object):
    def __init__(self) -> None:
        self._food_produce_license = FoodProduceLicense()

    def entities(self, entities: List[FoodProduceEntity]) -> "FoodProduceLicenseBuilder":
        self._food_produce_license.entities = entities
        return self

    def build(self) -> "FoodProduceLicense":
        return self._food_produce_license