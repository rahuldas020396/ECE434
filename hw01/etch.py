# Rahul Das
# ECE 434
# Homework 1
# Etch a sketch game

# In order for this progem to run correctly, pygame needs to be installed
# Type in command prompt:
# 	$host sudo apt install python3-pip
#  	$host pip3 install pygame

#Importing pygame
import pygame,sys
from pygame.locals import *

#Initialize pygame
pygame.init()

# Setup window for etch a sketch game
window_size = 500
screen = pygame.display.set_mode((window_size,window_size))

#Initial position of cursor
x = 250
y = 250

# Setting up boolean two color palettes for the game
color_switch = 0

#Initial color for the cursor
pointer_r = 255
pointer_g = 255
pointer_b = 255

# setting up timer for game
clock = pygame.time.Clock()

# Initially black background
screen.fill((0,0,0))

while 1:
	clock.tick(60)

	#Creating the cursor and drawing the lines
	pygame.draw.circle(screen,(pointer_r,pointer_g,pointer_b),(x,y),5)
	pygame.display.update()

	#Getting key presses and setting up boundaries for movement
	key = pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:x+=5
	if x >= window_size: x = window_size
	if key[pygame.K_LEFT]: x-=5
	if x <= 0: x = 0
	if key[pygame.K_UP]: y-=5
	if y <= 0: y = 0
	if key[pygame.K_DOWN]: y+=5
	if y >= window_size: y = window_size

	#Setting up what different key presses do
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE: # esc = quit
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_SPACE: # space = clear
			screen.fill((0,0,0))
			#Preserving current color palette
			if color_switch == 0:
				screen.fill((0,0,0))
				pointer_r = 255
				pointer_g = 255
				pointer_b = 255
			else:
				screen.fill((255,255,255))
				pointer_r = 0
				pointer_g = 0
				pointer_b = 0

		elif event.type == KEYDOWN and event.key == K_m: # m = switch color palette
			if color_switch == 0:
				screen.fill((255,255,255))

				pointer_r = 0
				pointer_g = 0
				pointer_b = 0

				color_switch = 1
			else:
				screen.fill((0,0,0))

				pointer_r = 255
				pointer_g = 255
				pointer_b = 255

				color_switch = 0
