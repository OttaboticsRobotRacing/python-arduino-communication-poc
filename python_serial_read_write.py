import serial
import time
import threading
import queue
from curtsies import Input # pip3 install curtsies

def read_serial(q):
    connected = False
    port = '/dev/ttyUSB0'
    baud = 9600

    try:
        ser = serial.Serial(port, baud, timeout=0)

        while not connected:
            #serin = ser.read()
            connected = True

            while ser.isOpen():
                if (ser.inWaiting() > 0):
                    data_str = ser.read(ser.inWaiting()).decode('ascii')
                    print('\r                                                     <\r', end='')
                    print(str(data_str).replace('\n',''), end='')
                stay_alive = True
                if not q.empty():
                    stay_alive = q.get()
                if not stay_alive:
                    return
            print('end')
    except serial.serialutil.SerialException:
        print('Serial port not found')
        return

def write_serial_message(message):
    connected = False
    port = '/dev/ttyUSB0'
    baud = 9600

    try:
        ser = serial.Serial(port, baud, timeout=0)
    except serial.serialutil.SerialException:
        print('Serial port not found')
        return

    ser.close()
    ser.open()

    ser.write(message.encode('ascii'))

    ser.close()

def write_serial_message_2(ser, message):
    ser.write(message.encode('ascii'))

def serial_setup():
    connected = False
    port = '/dev/ttyUSB0'
    baud = 9600

    try:
        ser = serial.Serial(port, baud, timeout=0)
    except serial.serialutil.SerialException:
        print('Serial port not found')
        return

    ser.close()
    ser.open()

    return ser

def write_serial_interactive():
    connected = False
    port = '/dev/ttyUSB0'
    baud = 9600

    try:
        ser = serial.Serial(port, baud, timeout=0)
    except serial.serialutil.SerialException:
        print('Serial port not found')
        return

    ser.close()
    ser.open()

    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == 'w':
                message = 'w'
                ser.write(message.encode('ascii'))
            if e == 'a':
                message = 'a'
                ser.write(message.encode('ascii'))
            if e == 's':
                message = 's'
                ser.write(message.encode('ascii'))
            if e == 'd':
                message = 'd'
                ser.write(message.encode('ascii'))
            if e == ' ':
                message = 'SPACE'
                ser.write(message.encode('ascii'))

            # print('\r' + repr(e) + '\r')
            print('\r\t\t\t\t\t\r', end='')

            if e == 'q':
                print('Exiting...')
                return

def main():
    q = queue.Queue()

    reader = threading.Thread(target=read_serial, args=(q,))
    reader.start()

    print('Please wait...')
    time.sleep(5)
    print('\r*** Ready to read keystrokes ***')

    write_serial_interactive()

    q.put(False)

if __name__ == '__main__':
    main()
