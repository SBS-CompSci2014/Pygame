# [ Python Game for ComputerScience ]
# [ MAIN FILE ]
# Copyright (C) SBS-CompSci-2014
# DISTRIBUTION OF THIS FILE BY A THIRD PARTY IS NOT AUTHORIZED

# File writen by Sir_Mr_Bman
# This file is owned by MORE THAN ONE PERSON, and as such can be distributed by these people.
# If you do not own my file, or have not been authorized to distribute this file, do not distribute it
# - SBS-CompSci-2014 and Sir_Mr_Bman have the right to DEATHORIZE USE OF THIS FILE

# Code is owned by Sir_Mr_Bman
# Please see his copyright terms on distributing this file.
# <-- START CODE -->



# Import code from pygame and system.
import pygame, sys, pixel, char

# This line should explain itself...?
from pygame.locals import *

# Init pygame
pygame.init()


# Call the background files and mouse files.
robbieBG = "res/background.JPEG"
fatalBG = "res/fatal.JPEG"
charFile = "res/char.png"
pixelFile = "res/pixel.png"

# Display 
screen = pygame.display.set_mode((700, 700), 0, 32)

# Load in the background file.
robbieBG = pygame.image.load(backgroundFile).convert()

charImg = pygame.image.load(mouseFile).convert_alpha()

# Update loop. Redisplays images, redraws character, etc. 
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(robbieBG, (0,0))
	pygame.display.update()

	# CODE TO MAKE THE CHARACTER MOVE

	if event.type == KEYDOWN:
		if event.key == K_LEFT
			char.moveLeft()
		elif event.key == K_RIGHT
			char.moveRight()
	



