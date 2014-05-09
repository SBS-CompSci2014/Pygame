# Char

x=0,0
movex = 0,0

def moveLeft():
	if event.key == K_LEFT:
		movex = -1

def moveRight():
	if event.key==K_RIGHT:
		movex = +1
