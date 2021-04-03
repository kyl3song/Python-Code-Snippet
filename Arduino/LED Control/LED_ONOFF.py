# -*- coding: utf-8 -*-
# Author: Kyle Song
# Python Package Install: pip3 install pyfirmata2
# Need to upload StandardFirmata with Arduino IDE first.

from pyfirmata2 import Arduino
import time

COMPORT = Arduino.AUTODETECT
PIN_NUM = 4

board = Arduino(COMPORT)
#board = Arduino("COM16")

# Another way of control pin
#pin3 = board.get_pin('d:4:p')
#pin4 = board.get_pin('d:4:o')

while True:
    try:
        num = int(input("Enter Number(ON: 1, OFF: 2): "))

        if num == 1:
            #pin4.write(1)
            board.digital[PIN_NUM].write(1)
            print(PIN_NUM, "ON")

        elif num == 2:
            #pin4.write(0)
            board.digital[PIN_NUM].write(0)
            print(PIN_NUM, "OFF")

    except ValueError:
        print("Invalid Input")
        break
