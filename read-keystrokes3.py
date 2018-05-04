# pip3 install curtsies
from curtsies import Input

def main():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print('\r' + repr(e) + '\r')
            if e == 'q':
                break

if __name__ == '__main__':
    main()
