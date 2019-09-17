#!/usr/bin/env python

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_12", GPIO.OUT)
period = 0.0001

state = 0
while(1):
    if state == 0:
        GPIO.output("P9_12", GPIO.HIGH)
        state = 1
        time.sleep(period/2)
    else:
        GPIO.output("P9_12", GPIO.LOW)
        state = 0
        time.sleep(period/2)