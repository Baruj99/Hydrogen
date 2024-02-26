# Modbus server (TCP)
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

def run_async_server():
    nreg = 200
    # initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [15]*nreg),
        co=ModbusSequentialDataBlock(0, [16]*nreg),
        hr=ModbusSequentialDataBlock(0, [17]*nreg),
        ir=ModbusSequentialDataBlock(0, [18]*nreg))
    context = ModbusServerContext(slaves=store, single=True)

    # initialize the server information
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Servidor MODBUS'
    identity.ProductCode = 'Servidor de PLC'
    identity.VendorUrl = ''
    identity.ProductName = 'Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '1.0'

    # TCP Server
    StartTcpServer(context=context, identity=identity, address=("192.168.0.20", 502))

if __name__ == "__main__":
    print('Modbus server started on 192.168.0.20 port 502')
    run_async_server()