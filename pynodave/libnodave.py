import ctypes
from .common import _DaveInterface, _DaveConnection, _DaveOSSerialType


class _LibNoDave:

    def __init__(self):
        super().__init__()

        self.libnodave = ctypes.cdll.LoadLibrary('libnodave.so')

        self.libnodave.openSocket.restype = ctypes.c_int
        self.libnodave.openSocket.argtypes = [
            ctypes.c_int,
            ctypes.c_char_p,
        ]

        self.libnodave.daveNewInterface.restype = ctypes.POINTER(_DaveInterface)
        self.libnodave.daveNewInterface.argtypes = [
            _DaveOSSerialType,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int
        ]

        self.libnodave.daveInitAdapter.restype = ctypes.c_int
        self.libnodave.daveInitAdapter.argtypes = [
            ctypes.POINTER(_DaveInterface)
        ]

        self.libnodave.daveNewConnection.restype = ctypes.POINTER(_DaveConnection)
        self.libnodave.daveNewConnection.argtypes = [
            ctypes.POINTER(_DaveInterface),  # daveInterface
            ctypes.c_int,  # MPI
            ctypes.c_int,  # rack
            ctypes.c_int   # slot
        ]
        self.libnodave.daveConnectPLC.restype = ctypes.c_int
        self.libnodave.daveConnectPLC.argtypes = [
            ctypes.POINTER(_DaveConnection)
        ]

        self.libnodave.daveDisconnectPLC.restype = ctypes.c_int
        self.libnodave.daveDisconnectPLC.argtypes = [
            ctypes.POINTER(_DaveConnection)
        ]

        self.libnodave.daveDisconnectAdapter.restype = ctypes.c_int
        self.libnodave.daveDisconnectAdapter.argtypes = [ctypes.POINTER(_DaveInterface)]

        self.libnodave.closeSocket.restype = ctypes.c_int
        self.libnodave.closeSocket.argtypes = [
            ctypes.c_int  # fd
        ]

        self.libnodave.daveFree.restype = None
        self.libnodave.daveFree.argtypes = [
            ctypes.c_void_p  # pointer
        ]

        self.libnodave.daveReadBytes.restype = ctypes.c_int
        self.libnodave.daveReadBytes.argtypes = [
            ctypes.POINTER(_DaveConnection),    # dc
            ctypes.c_int,                       # area
            ctypes.c_int,                       # DB
            ctypes.c_int,                       # start
            ctypes.c_int,                       # len
            ctypes.c_void_p                     # buffer
        ]

        self.libnodave.daveGetS8.restype = ctypes.c_int
        self.libnodave.daveGetS8.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetU8.restype = ctypes.c_int
        self.libnodave.daveGetU8.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetS16.restype = ctypes.c_int
        self.libnodave.daveGetS16.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetU16.restype = ctypes.c_int
        self.libnodave.daveGetU16.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetS32.restype = ctypes.c_int
        self.libnodave.daveGetS32.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetU32.restype = ctypes.c_uint
        self.libnodave.daveGetU32.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetFloat.restype = ctypes.c_float
        self.libnodave.daveGetFloat.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetKG.restype = ctypes.c_float
        self.libnodave.daveGetKG.argtypes = [
            ctypes.POINTER(_DaveConnection)  # dc
        ]

        self.libnodave.daveGetS8from.restype = ctypes.c_int
        self.libnodave.daveGetS8from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetU8from.restype = ctypes.c_int
        self.libnodave.daveGetU8from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetS16from.restype = ctypes.c_int
        self.libnodave.daveGetS16from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetU16from.restype = ctypes.c_int
        self.libnodave.daveGetU16from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetS32from.restype = ctypes.c_int
        self.libnodave.daveGetS32from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetU32from.restype = ctypes.c_uint
        self.libnodave.daveGetU32from.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        self.libnodave.daveGetFloatfrom.restype = ctypes.c_float
        self.libnodave.daveGetFloatfrom.argtypes = [
            ctypes.POINTER(ctypes.c_char)           # buffer
        ]

        # self.libnodave.daveGetKGfrom.restype = ctypes.c_float
        # self.libnodave.daveGetKGfrom.argtypes = [
        #     ctypes.POINTER(ctypes.c_char)           # buffer
        # ]
