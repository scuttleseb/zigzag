import serial
import time

ser = serial.Serial(
    port="/dev/tty.SLAB_USBtoUART",
    baudrate=19200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

openned = ser.isOpen
print ser.portstr 


print(openned)