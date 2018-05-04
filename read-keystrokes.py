import keyboard
import time

while True:
    try:
        if keyboard.is_pressed('w'):
            print('w')
        if keyboard.is_pressed('a'):
            print('a')
        if keyboard.is_pressed('s'):
            print('s')
        if keyboard.is_pressed('d'):
            print('d')
        if keyboard.is_pressed('q'):
            break
    except Exception as e:
        print(e)
        break
    time.sleep(0.1)
