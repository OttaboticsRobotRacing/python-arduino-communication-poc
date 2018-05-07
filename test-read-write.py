import python_serial_read_write
import time
import queue
import threading
import serial

def read_serial(q):
    connected = False
    port = '/dev/ttyUSB0'
    baud = 9600

    count = 0

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
                    if 'ACK: w' in data_str or 'ACK: a' in data_str or 'ACK: s' in data_str or 'ACK: d' in data_str or 'ACK: SPACE' in data_str:
                        count += 1
                    print('\r\t\t\tcount: ' + str(count), end='')
                stay_alive = True
                if not q.empty():
                    stay_alive = q.get()
                if not stay_alive:
                    return
            print('end')
    except serial.serialutil.SerialException:
        print('Serial port not found')
        return

def main():
    q = queue.Queue()

    reader = threading.Thread(target=read_serial, args=(q,))
    reader.start()

    for i in range(3, 0, -1):
        print('\r   \r' + str(i), end='')
        time.sleep(1)
    print('\r*** TEST STARTED ***')
    '''
    for i in range(10):
        python_serial_read_write.write_serial_message('w')
        time.sleep(0.1)
        python_serial_read_write.write_serial_message('a')
        time.sleep(0.1)
        python_serial_read_write.write_serial_message('s')
        time.sleep(0.1)
        python_serial_read_write.write_serial_message('d')
        time.sleep(0.1)
        python_serial_read_write.write_serial_message('SPACE')
        time.sleep(0.1)
    '''

    led_delay = 0.05
    num_test_per_cycle = 5
    num_cycles = 100

    ser = python_serial_read_write.serial_setup()
    for i in range(num_cycles):
        python_serial_read_write.write_serial_message_2(ser, 'w')
        time.sleep(led_delay)
        python_serial_read_write.write_serial_message_2(ser, 'a')
        time.sleep(led_delay)
        python_serial_read_write.write_serial_message_2(ser, 's')
        time.sleep(led_delay)
        python_serial_read_write.write_serial_message_2(ser, 'd')
        time.sleep(led_delay)
        python_serial_read_write.write_serial_message_2(ser, 'SPACE')
        time.sleep(led_delay)

    q.put(False)

    print('\nTotal writes: ' + str(num_cycles * num_test_per_cycle))

    print('*** END OF TEST ***')

if __name__ == '__main__':
    main()
