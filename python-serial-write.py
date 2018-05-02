import serial
import time

connected = False
port = '/dev/ttyUSB0'
baud = 9600

ser = serial.Serial(port, baud, timeout=0)

ser.close()
ser.open()

while True:
    input_message = input('Input message: ')
    if input_message == 'exit':
        break
    ser.write(input_message.encode('ascii'))
