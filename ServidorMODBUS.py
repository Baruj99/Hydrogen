import RPi.GPIO as GPIO
from pymodbus.server import *
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import logging
import time
import struct

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def read_sensor():
    GPIO.setmode(GPIO.BCM)
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    try:
        while True:
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)

            StartTime = time.time()
            StopTime = time.time()

            while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()

            while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()

            TimeElapsed = StopTime - StartTime
            distance = (TimeElapsed * 34300) / 2
            dist = distance

            # Convertir el número real a bytes y luego a partes alta y baja
            float_bytes = struct.pack('f', dist)
            high_bytes = struct.unpack('>HH', float_bytes)[:2]

            # Almacenar las partes alta y baja en dos registros consecutivos
            context[0].setValues(3, 0, [high_bytes[0]])
            context[0].setValues(3, 1, [high_bytes[1]])

            print("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

# Inicializa tu almacén de datos Modbus
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17] * 100),
    co=ModbusSequentialDataBlock(0, [17] * 100),
    hr=ModbusSequentialDataBlock(0, [0] * 200),  # 2 registros consecutivos
    ir=ModbusSequentialDataBlock(0, [17] * 100))
context = ModbusServerContext(slaves=store, single=True)

# Inicia el servidor TCP
server = StartTcpServer(context=context, address=("192.168.0.23", 5020))

if __name__ == '__main__':
    read_sensor()
