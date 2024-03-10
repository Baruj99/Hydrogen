import asyncio
import logging
from pymodbus.server.async import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification

_logger = logging.getLogger(__file__)
_logger.setLevel(logging.INFO)

def setup_server():
    # Configura un único almacén de datos Modbus
    datablock = lambda: ModbusSequentialDataBlock(0x00, [17] * 100)
    context = ModbusSlaveContext(di=datablock(), co=datablock(), hr=datablock(), ir=datablock())
    return ModbusServerContext(slaves={0x01: context}, single=False)

async def run_async_server():
    context = setup_server()
    server = await StartAsyncTcpServer(context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    asyncio.run(run_async_server(), debug=True)
