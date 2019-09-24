#!/usr/bin/env python
# From: https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/Encoder.html
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2b, eQEP1

 
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

myEncoder1 = RotaryEncoder(eQEP1)
myEncoder1.setAbsolute()
myEncoder1.enable()

myEncoder2 = RotaryEncoder(eQEP2b)
myEncoder2.setAbsolute()
myEncoder2.enable()

encoder1_position = myEncoder1.position
encoder2_position = myEncoder2.position
new_position1 = encoder1_position
new_position2 = encoder2_position
 
 
# Setting up buttons
btn1 = "P8_16" #up
btn4 = "P8_17" #
btn2 = "P8_18" #
btn3 = "P8_15" # up

reset = "P8_8" #

#Bus 2 at address 0x70
bus = smbus.SMBus(2)
matrix = 0x70
 
# Setting up LED matrix
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)
 
# Setting up inputs and outputs
GPIO.setup(btn1, GPIO.IN)
GPIO.setup("P8_11", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup(btn2, GPIO.IN)
GPIO.setup(btn3, GPIO.IN)
GPIO.setup(btn4, GPIO.IN)
GPIO.setup(reset, GPIO.IN)
 
# # Setting up internal pulldown
# GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(btn4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
# Grid setup
width = 7   
height = 7  

x = 4
y = 4
 
path  = [0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF]
 
# Empty Array for matrix manipulation
empty = [0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF,
        0x00, 0xFF]

turn_off = [0x00,0x00,
            0x00,0x00,
            0x00,0x00,
            0x00,0x00,
            0x00,0x00,
            0x00,0x00,
            0x00,0x00,
            0x00,0x00]       
# Inital Write to LED Matrix
bus.write_i2c_block_data(matrix, 0, path)
   
while(1):
    new_position1 = myEncoder1.position
    new_position2 = myEncoder2.position
    print(new_position1, ":", new_position2)
    if new_position1<encoder1_position:
        if x >= (width):
            x = x - 1
        x = x + 1
        time.sleep(0.08)
    
    if new_position1>encoder1_position:
        if x <= 0:
            x = x + 1
        x = x - 1
        time.sleep(0.08)
        
    if new_position2<encoder2_position:
        if y <= 0:
            y = y + 1
        y = y - 1
        time.sleep(0.08)
    #button 3
    if new_position2>encoder2_position:
        if y >= height:
            y = y - 1
        y = y + 1
        time.sleep(0.08)
    
    #reset button which clears terminal and sets the cursor back to position (0,0)
    # if GPIO.input(reset):
    #     x=4
    #     y=4
    #     for i in range(0, 15):
    #         leds[i] = 0x00
    
    encoder1_position=new_position1
    encoder2_position=new_position2
       
    path[2*x] = path[2*x]|(0x80>>y)
    bus.write_i2c_block_data(matrix, 0, path)
 
    time.sleep(0.08)
# # The first byte is GREEN, the second is RED.
# smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85, 0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c]
# frown = [0x3c, 0x00, 0x42, 0x00, 0x85, 0x20, 0x89, 0x00, 0x89, 0x00, 0x85, 0x20, 0x42, 0x00, 0x3c, 0x00]
# neutral = [0x3c, 0x3c, 0x42, 0x42, 0xa9, 0xa9, 0x89, 0x89, 0x89, 0x89, 0xa9, 0xa9, 0x42, 0x42, 0x3c, 0x3c]
# # Start oscillator (p10)
# bus.write_byte_data(matrix, 0x21, 0)
# # Dispon, blink off (p11)
# bus.write_byte_data(matrix, 0x81, 0)
# # Full brightness (page 15)
# bus.write_byte_data(matrix, 0xe7, 0)
# bus.write_i2c_block_data(matrix, 0, frown)
# time.sleep(1)
