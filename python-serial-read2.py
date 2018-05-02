import serial
import time

connected = False
port = '/dev/ttyUSB0'
baud = 9600

ser = serial.Serial(port, baud, timeout=0)

while not connected:
    #serin = ser.read()
    connected = True

    while ser.isOpen():
        if (ser.inWaiting() > 0):
            data_str = ser.read(ser.inWaiting()).decode('ascii')
            print(data_str, end='')
    print('end')
