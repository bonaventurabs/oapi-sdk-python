# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class TimeSpan(object):
    _types = {
        "start_time": str,
        "end_time": str,
    }

    def __init__(self, d=None):
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TimeSpanBuilder":
        return TimeSpanBuilder()


class TimeSpanBuilder(object):
    def __init__(self) -> None:
        self._time_span = TimeSpan()

    def start_time(self, start_time: str) -> "TimeSpanBuilder":
        self._time_span.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "TimeSpanBuilder":
        self._time_span.end_time = end_time
        return self

    def build(self) -> "TimeSpan":
        return self._time_span