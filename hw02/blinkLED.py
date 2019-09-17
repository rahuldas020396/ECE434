#!/usr/bin/env python

# Rahul Das
# ECE 434
# Homework 2
# Blinking LEDs with push buttons

# Importing the GPIO pins
import Adafruit_BBIO.GPIO as GPIO

# Setting up names for pins
btn1 = "P8_7"
btn2 = "P8_8"
btn3 = "P8_10"
btn4 = "P8_9"

led1 = "P8_12"
led2 = "P8_11"
led3 = "P8_15"
led4 = "P8_16"


# Setting up LEDs as outputs

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

# Setting up buttons as inputs

GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(btn3, GPIO.IN)
GPIO.setup(btn4, GPIO.IN)

# Enabling internal pull up resistors
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while(1):
    if GPIO.input(btn1):
        GPIO.output(led1, GPIO.HIGH)
    elif GPIO.input(btn2):
        GPIO.output(led2, GPIO.HIGH)
    elif GPIO.input(btn3):
        GPIO.output(led3, GPIO.HIGH)
    elif GPIO.input(btn4):
        GPIO.output(led4, GPIO.HIGH)
    else:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)