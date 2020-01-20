import pynodave.pynodavetcp
import pynodave.common
import pynodave.buffer


test = pynodave.pynodavetcp.PyNoDaveTCP()

test.connect("192.168.1.2", 102, 0, 2)

test.read_bytes(pynodave.common.DaveArea.daveDB, 21, 0, 1)
print(test.get_u8())

buffer = pynodave.buffer.DaveBuffer(10)

test.read_bytes(pynodave.common.DaveArea.daveDB, 21, 0, 1, buffer)
print(test.get_u8(buffer))

test.disconnect()






