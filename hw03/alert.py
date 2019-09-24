#!/usr/bin/env python

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus


alert1 = "P8_7"
alert2 = "P8_8"

bus = smbus.SMBus(2)
address = 0x48



GPIO.setup(alert1,GPIO.IN)
GPIO.setup(alert1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(alert2,GPIO.IN)
GPIO.setup(alert2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
    temp = bus.read_byte_data(address, 0)
    #print (temp, end="\r")
    time.sleep(1)
    #print()
    
    time.sleep(1)
    bus.write_byte_data(address, 1,0x80)
    con = bus.read_byte_data(address, 1)
    print(temp,":",GPIO.input(alert1),":",con)
    
    
    # print(GPIO.input(alert1))
    # time.sleep(1)
    # if GPIO.input(alert1) == 1:
    #     print('Alert for sensor 1')
    #     time.sleep(0.1)
    # elif GPIO.input(alert2) == 1:
    #     print('Alert for sensor 2')
    #     time.sleep(0.1)