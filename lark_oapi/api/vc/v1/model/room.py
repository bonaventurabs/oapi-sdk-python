# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .device import Device
from .room_status import RoomStatus


class Room(object):
    _types = {
        "room_id": str,
        "name": str,
        "capacity": int,
        "description": str,
        "display_id": str,
        "custom_room_id": str,
        "room_level_id": str,
        "path": List[str],
        "room_status": RoomStatus,
        "device": List[Device],
    }

    def __init__(self, d):
        self.room_id: Optional[str] = None
        self.name: Optional[str] = None
        self.capacity: Optional[int] = None
        self.description: Optional[str] = None
        self.display_id: Optional[str] = None
        self.custom_room_id: Optional[str] = None
        self.room_level_id: Optional[str] = None
        self.path: Optional[List[str]] = None
        self.room_status: Optional[RoomStatus] = None
        self.device: Optional[List[Device]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RoomBuilder":
        return RoomBuilder()


class RoomBuilder(object):
    def __init__(self, room: Room = Room({})) -> None:
        self._room: Room = room

    def room_id(self, room_id: str) -> "RoomBuilder":
        self._room.room_id = room_id
        return self

    def name(self, name: str) -> "RoomBuilder":
        self._room.name = name
        return self

    def capacity(self, capacity: int) -> "RoomBuilder":
        self._room.capacity = capacity
        return self

    def description(self, description: str) -> "RoomBuilder":
        self._room.description = description
        return self

    def display_id(self, display_id: str) -> "RoomBuilder":
        self._room.display_id = display_id
        return self

    def custom_room_id(self, custom_room_id: str) -> "RoomBuilder":
        self._room.custom_room_id = custom_room_id
        return self

    def room_level_id(self, room_level_id: str) -> "RoomBuilder":
        self._room.room_level_id = room_level_id
        return self

    def path(self, path: List[str]) -> "RoomBuilder":
        self._room.path = path
        return self

    def room_status(self, room_status: RoomStatus) -> "RoomBuilder":
        self._room.room_status = room_status
        return self

    def device(self, device: List[Device]) -> "RoomBuilder":
        self._room.device = device
        return self

    def build(self) -> "Room":
        return self._room