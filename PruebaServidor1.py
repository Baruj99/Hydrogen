#Funciona con pymodbus 3.6.6 
#!/usr/bin/env python
#---------------------------------------------------------------------------# 
# the various server implementations
#---------------------------------------------------------------------------# 
from pymodbus.server import *

from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
#---------------------------------------------------------------------------# 
# configure the service logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------# 
# initialize your data store
#---------------------------------------------------------------------------# 
store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [17]*100),
    co = ModbusSequentialDataBlock(0, [17]*100),
    hr = ModbusSequentialDataBlock(0, [17]*100),
    ir = ModbusSequentialDataBlock(0, [17]*100))
context = ModbusServerContext(slaves=store, single=True)

#---------------------------------------------------------------------------# 
# run the server you want
#---------------------------------------------------------------------------# 
#StartTcpServer(context=context)
#StartUdpServer(context)
#StartSerialServer(context, port='/tmp/tty1')
StartTcpServer(context=context, address=("192.168.0.23", 5020))
