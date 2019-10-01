Device Name         |   Start Address   |       End Address
-----------         |   -------------   |       -----------
External Memory     |   0x0000_0000     |       0x1FFF_FFFF
GPIO0               |   0x44E0_7000     |       0x44E0_7FFF
UART Registers      |   0x44E0_9000     |       0x44E0_9FFF
I2C0                |   0x44E0_B000     |       0x44E0_BFFF
UART1               |   0x4802_2000     |       0x4802_2FFF
UART2               |   0x4802_4000     |       0x4802_4FFF
I2C1                |   0x4802_A000     |       0x4802_AFFF
GPIO1               |   0x4804_C000     |       0x4804_CFFF
I2C2                |   0x4819_C000     |       0x4819_CFFF
UART3               |   0x481A_6000     |       0x481A_6FFF
UART4               |   0x481A_8000     |       0x481A_8FFF
UART5               |   0x481A_A000     |       0x481A_AFFF
GPIO2               |   0x481A_C000     |       0X481A_CFFF
GPIO3               |   0x481A_E000     |       0x481A_EFFF
LCD controller      |   0x4830_E000     |       0x4830_EFFF
SRAM internal       |   0x402F_0400     |       0x402F_FFFF
SDRAM               |   0X8000_0000     |       0X8FFF_FFFF

Buttons connected to P9_12 and P9_25
Files included:
1. btnLED.c
    This file uses the switches on GPIO1 and GPIO3 
2. backlight.python
    Sets up the backlight for the LCD display
3. textWriter.sh
    Sets up the text I want to display on the LCD
4. textondisplay.sh
    Turns on the LCD and then runs textWriter.sh so that the display works correctly
5. toggle.c
    Toggles the gpio pin. When period is set to 0, it toggles the fastest
6. tux.png
    This is the image to be displayed on the LCD
7. SPI_go.sh
    This script turns on the LCD, displays the image of tux and then turns off.
    The  second time it turns on, it displays the image of tux rotated by 90 degrees
8. ohSheep.mp4
    This is a dark animated video I found on youtube that I attempted to play on the LCD
9. videoplayer.sh
    Turns on the lcd and then uses mplayer to play ohSheep.mp4

Trying pygame:
I had a lot of fun playing with the LCD. I also found an install.sh for pygame inside
exercises/displays/ili9341/fb/pygame. After a lengthy install, it finally gets to creating 
the wheel, it fails. After this, the pygame package is still unavailable on the bone :(

I wonder if there is a way to light up individual pixels on the LCD so we could 
technically recreate the etch-a-sketch game. By changing the number of pixels 
perpendicilar to the direction of motion, we could increase the thickness of the LCD
and even make it user defined. We could also change the rgb values on the LCD and make
it colorful. All this without pygame.