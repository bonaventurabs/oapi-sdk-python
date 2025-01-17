# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ShiftAttendanceTimeConfig(object):
    _types = {
        "attendance_time": float,
        "on_attendance_time": float,
        "off_attendance_time": float,
    }

    def __init__(self, d=None):
        self.attendance_time: Optional[float] = None
        self.on_attendance_time: Optional[float] = None
        self.off_attendance_time: Optional[float] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ShiftAttendanceTimeConfigBuilder":
        return ShiftAttendanceTimeConfigBuilder()


class ShiftAttendanceTimeConfigBuilder(object):
    def __init__(self) -> None:
        self._shift_attendance_time_config = ShiftAttendanceTimeConfig()

    def attendance_time(self, attendance_time: float) -> "ShiftAttendanceTimeConfigBuilder":
        self._shift_attendance_time_config.attendance_time = attendance_time
        return self

    def on_attendance_time(self, on_attendance_time: float) -> "ShiftAttendanceTimeConfigBuilder":
        self._shift_attendance_time_config.on_attendance_time = on_attendance_time
        return self

    def off_attendance_time(self, off_attendance_time: float) -> "ShiftAttendanceTimeConfigBuilder":
        self._shift_attendance_time_config.off_attendance_time = off_attendance_time
        return self

    def build(self) -> "ShiftAttendanceTimeConfig":
        return self._shift_attendance_time_config
