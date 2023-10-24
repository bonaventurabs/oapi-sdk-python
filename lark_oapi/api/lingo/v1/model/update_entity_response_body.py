# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .entity import Entity


class UpdateEntityResponseBody(object):
    _types = {
        "entity": Entity,
    }

    def __init__(self, d=None):
        self.entity: Optional[Entity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateEntityResponseBodyBuilder":
        return UpdateEntityResponseBodyBuilder()


class UpdateEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_entity_response_body = UpdateEntityResponseBody()

    def entity(self, entity: Entity) -> "UpdateEntityResponseBodyBuilder":
        self._update_entity_response_body.entity = entity
        return self

    def build(self) -> "UpdateEntityResponseBody":
        return self._update_entity_response_body