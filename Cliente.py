# Funciona con pymodbus 1.5.2
from pymodbus.client.sync import ModbusTcpClient

# Dirección IP y puerto del servidor Modbus
SERVER_IP = "192.168.0.23"
#SERVER_PORT = 502
SERVER_PORT = 5020

# Crear una instancia del cliente Modbus
client = ModbusTcpClient(SERVER_IP, SERVER_PORT)

# Intentar conectar al servidor
if client.connect():
    print("Conexión exitosa al servidor Modbus.")
    
    # Leer el valor del holding register 8
    register_address = 8
    response = client.read_holding_registers(register_address, 1)
    
    if response.isError():
        print("Error al leer el holding register.")
    else:
        register_value = response.registers[0]
        print(f"Valor leído del holding register 8: {register_value}")

    # Modificar el valor del holding register 8 a 11
    new_value = 13
    response = client.write_register(register_address, new_value)
    
    if response.isError():
        print("Error al escribir en el holding register.")
    else:
        print(f"Valor modificado del holding register {register_address} a {new_value}")
    
    response = client.read_holding_registers(register_address, 1)
    
    if response.isError():
        print("Error al leer el holding register.")
    else:
        register_value = response.registers[0]
        print(f"Valor leído del holding register 8: {register_value}")

    
else:
    print("No se pudo conectar al servidor Modbus.")

# No olvides cerrar la conexión cuando hayas terminado
client.close()