import ctypes
from enum import Enum


class _DaveOSSerialType(ctypes.Structure):
    _fields_ = [("rfd", ctypes.c_int), ("wfd", ctypes.c_int)]


class _DaveInterface(ctypes.Structure):
    pass


class _DaveConnection(ctypes.Structure):
    pass


class DaveArea(Enum):
    daveSysInfo = 0x3       # System info of 200 family
    daveSysFlags = 0x5      # System flags of 200 family
    daveAnaIn = 0x6         # analog inputs of 200 family
    daveAnaOut = 0x7        # analog outputs of 200 family
    daveP = 0x80            # direct peripheral access
    daveInputs = 0x81       # inputs
    daveOutputs = 0x82      # outputs
    daveFlags = 0x83        # flags \ markers
    daveDB = 0x84           # data blocks
    daveDI = 0x85           # instance data blocks
    daveLocal = 0x86        # not tested
    daveV = 0x87            # don't know what it is
    daveCounter = 28        # S7 counters
    daveTimer = 29          # S7 timers
    daveCounter200 = 30     # IEC counters (200 family)
    daveTimer200 = 31       # IEC timers (200 family)
    daveSysDataS5 = 0x86    # system data area ?
    daveRawMemoryS5 = 0     # just the raw memory
