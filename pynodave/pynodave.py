from abc import ABC, abstractmethod
import ctypes

from .libnodave import _LibNoDave
from .common import DaveArea
from .buffer import DaveBuffer


class PyNoDave(ABC):

    def __init__(self):
        super().__init__()

        self._libnodave_c = _LibNoDave()
        self._libnodave = _LibNoDave().libnodave

        self._fds = None
        self._interface = None
        self._connection = None
        self._connected = False
        self._adapterInitialized = False

    @abstractmethod
    def connect(self, **kwargs):
        pass

    @abstractmethod
    def disconnect(self, **kwargs):
        pass

    def read_bytes(self, area: DaveArea, db: int, start: int, length: int, buffer: DaveBuffer = None):

        if buffer:
            if length > buffer.get_length():
                raise ValueError("Buffer to small")
            result = self._libnodave.daveReadBytes(self._connection, ctypes.c_int(area.value), ctypes.c_int(db),
                                                   ctypes.c_int(start), ctypes.c_int(length), buffer.get_buffer())
        else:
            result = self._libnodave.daveReadBytes(self._connection, ctypes.c_int(area.value), ctypes.c_int(db),
                                                   ctypes.c_int(start), ctypes.c_int(length), None)

        if result != 0:
            raise RuntimeError("daveReadBytes returned {}".format(result))

    def get_u8(self, buffer: DaveBuffer = None) -> int:

        if buffer:
            return self._libnodave.daveGetS8from(buffer.get_buffer())
        else:
            return self._libnodave.daveGetS8(self._connection)

