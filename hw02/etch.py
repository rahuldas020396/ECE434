#!/usr/bin/env python

# Rahul Das
# ECE 434
# Homework 1
# Etch a sketch game

import curses
import time
import Adafruit_BBIO.GPIO as GPIO

#Buttons setup
btn1 = "P8_7"
btn2 = "P8_8"
btn3 = "P8_10"
btn4 = "P8_9"



height = 10 #input("Height: ")
width = 10 #input("Width: ")



        
    
    
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
    
    
def main(stdscr):
    
    x = 0
    y = 0
    curses.curs_set(0)
    stdscr.refresh()
    #time.sleep(3)
    
        
    
    while(1):
        
        
        #Moving the cursor
        if GPIO.input(btn1): 
            #key == curses.KEY_UP :
            y = y - 1
            if y <=0: y = 0
            stdscr.addstr(y,x, "X")
            
        
        if GPIO.input(btn2): 
            #key == curses.KEY_DOWN or GPIO.input(btn2):
            y= y + 1
            if y>= height: y = height-1
            stdscr.addstr(y,x, "X")
        
        if GPIO.input(btn3):
            #key == curses.KEY_LEFT or GPIO.input(btn3):
            x = x - 1
            if x <=0: x = 0
            stdscr.addstr(y,x, "X")
        
        if GPIO.input(btn4): 
            #key == curses.KEY_RIGHT or GPIO.input(btn4):
            x = x + 1
            if x>= width: x = width-1
            stdscr.addstr(y,x, "X")
        if GPIO.input(btn1) and GPIO.input(btn2) and GPIO.input(btn3) and GPIO.input(btn4):
            stdscr.clear()
        
        stdscr.refresh()
        time.sleep(0.1)
        # key = stdscr.getch()#        
        # if key == curses.KEY_DC:
        #     curses.endwin()
        # if key == curses.KEY_ENTER or key in [10, 13]:
        #     stdscr.clear()
        # stdscr.refresh()
    
curses.wrapper(main)





