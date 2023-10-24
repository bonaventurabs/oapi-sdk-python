# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DocUser(object):
    _types = {
        "user_id": int,
    }

    def __init__(self, d=None):
        self.user_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocUserBuilder":
        return DocUserBuilder()


class DocUserBuilder(object):
    def __init__(self) -> None:
        self._doc_user = DocUser()

    def user_id(self, user_id: int) -> "DocUserBuilder":
        self._doc_user.user_id = user_id
        return self

    def build(self) -> "DocUser":
        return self._doc_user