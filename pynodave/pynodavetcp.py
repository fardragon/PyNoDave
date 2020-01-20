from .common import _DaveOSSerialType
from .pynodave import PyNoDave
import ctypes


class PyNoDaveTCP(PyNoDave):

    def __init__(self):
        super().__init__()

        self.__protocolType = ctypes.c_int(122) # ISO TCP
        self.__connectionName = ctypes.c_char_p(b'LibNoDave TCP connection')
        self.__placeHolder = ctypes.c_int(0)  # placeholder for unused values

    def connect(self, address: str = "127.0.0.1", port: int = 102, rack: int = 0, slot: int = 2, **kwargs):

        # open socket
        socket = self._libnodave.openSocket(port, ctypes.c_char_p(address.encode()))
        if socket <= 0:
            self.disconnect()
            raise RuntimeError("openSocket returned {}".format(socket))

        self._fds = _DaveOSSerialType(rfd=socket, wfd=socket)

        # create interface
        self._interface = self._libnodave.daveNewInterface(self._fds, self.__connectionName, self.__placeHolder,
                                                           self.__protocolType, self.__placeHolder)
        if not self._interface:
            self.disconnect()
            raise RuntimeError("daveNewInterface returned nullptr")

        # initialize adapter
        result = self._libnodave.daveInitAdapter(self._interface)
        if result != 0:
            self.disconnect()
            raise RuntimeError("openSocket returned {}".format(result))
        else:
            self._adapterInitialized = True

        # create connection
        self._connection = self._libnodave.daveNewConnection(self._interface, self.__placeHolder, ctypes.c_int(rack),
                                                             ctypes.c_int(slot))
        if not self._connection:
            self.disconnect()
            raise RuntimeError("daveNewConnection returned nullptr")
        else:
            self._connected = True

        # connect
        result = self._libnodave.daveConnectPLC(self._connection)
        if result != 0:
            self.disconnect()
            raise RuntimeError("daveConnectPLC returned {}".format(result))

    def disconnect(self, **kwargs):

        if self._connected:
            self._libnodave.daveDisconnectPLC(self._connection)
            self._connected = False

        if self._connection:
            self._libnodave.daveFree(self._connection)
            self._connection = None

        if self._adapterInitialized:
            self._libnodave.daveDisconnectAdapter(self._interface)
            self._adapterInitialized = False

        if self._interface:
            self._libnodave.daveFree(self._interface)
            self._interface = None

        if self._fds and self._fds.rfd > 0:
            self._libnodave.closeSocket(self._fds.rfd)
            self._fds = _DaveOSSerialType(rfd=ctypes.c_int(0), wfd=ctypes.c_int(0))