import pygame,sys
from pygame.locals import *
pygame.init()
window_size = 500
screen = pygame.display.set_mode((window_size,window_size))

x = 250
y = 250
color_switch = 0

pointer_r = 255
pointer_g = 255
pointer_b = 255

clock = pygame.time.Clock()
screen.fill((0,0,0))

while 1:
	clock.tick(60)
	pygame.draw.circle(screen,(pointer_r,pointer_g,pointer_b),(x,y),5)
	pygame.display.update()
	key = pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:x+=5
	if x >= window_size: x = window_size
	if key[pygame.K_LEFT]: x-=5
	if x <= 0: x = 0
	if key[pygame.K_UP]: y-=5
	if y <= 0: y = 0
	if key[pygame.K_DOWN]: y+=5
	if y >= window_size: y = window_size

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exis()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_SPACE:
			screen.fill((0,0,0))

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

		elif event.type == KEYDOWN and event.key == K_m:
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


