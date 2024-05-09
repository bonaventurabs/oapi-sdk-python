# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .failed_reason import FailedReason


class PatchFeedCardResponseBody(object):
    _types = {
        "failed_user_reasons": List[FailedReason],
    }

    def __init__(self, d=None):
        self.failed_user_reasons: Optional[List[FailedReason]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchFeedCardResponseBodyBuilder":
        return PatchFeedCardResponseBodyBuilder()


class PatchFeedCardResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_feed_card_response_body = PatchFeedCardResponseBody()

    def failed_user_reasons(self, failed_user_reasons: List[FailedReason]) -> "PatchFeedCardResponseBodyBuilder":
        self._patch_feed_card_response_body.failed_user_reasons = failed_user_reasons
        return self

    def build(self) -> "PatchFeedCardResponseBody":
        return self._patch_feed_card_response_body