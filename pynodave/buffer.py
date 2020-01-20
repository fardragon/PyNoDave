import ctypes


class DaveBuffer:

    def __init__(self, size: int):
        self.__buffer = ctypes.create_string_buffer(size)
        self.__size = size

    def get_length(self) -> int:
        return self.__size

    def get_buffer(self, offset: int = 0) -> ctypes.POINTER(ctypes.c_char):
        return ctypes.cast(ctypes.byref(self.__buffer, offset), ctypes.POINTER(ctypes.c_char))
