from enum import Enum
from abc import ABC, abstractmethod
class EventKind(Enum):
    OutOfMemory = 1
    NoSpaceLeftOnDevice = 2

class Event(ABC):
    def __init__(self):
        ...
    def __str__(self):
        ...

class OutOfMemoryEvent(Event):
    def __init__(self, data=None):
        self.kind = EventKind.OutOfMemory
        self.data = data

    def __str__(self):
        return f"""Event(kind:{self.kind})"""


class NoSpaceLeftOnDeviceEvent(Event):
    def __init__(self, data=None):
        self.kind = EventKind.NoSpaceLeftOnDevice
        self.data = data

    def __str__(self):
        return f"""Event(kind:{self.kind})"""

