import pygame
import random
from pygame.locals import *

#define ids
BYE          = -1

#0 to 15 reserved

TITLE_SCREEN = 100
LEVEL_SELECT = 101
CONTROLS     = 102
PLAY         = 103
GAME_OVER    = 104
SCORES       = 105
WIN          = 106
LOSE         = 107

#constantes
MAXLVL       = 16
MAXWIDTH     = 900
MAXHEIGHT    = 900

class button:
	def __init__(self,x,y,w,h,value = "",id=0, textSize = 40,color = (255,255,255,100),textColor = (0,0,0)):
		self.value = value
		self.id = id
		self.position = (x,y)
		self.size = (w,h)
		self.color = color
		self.textColor = textColor
		self.textSize = textSize
		self.hovered = False
		self.big = False
		self.padding = 0
		self.textPadding = 0
		self.disabled = False

	def draw(self,window):
		s = pygame.Surface((self.size[0],self.size[1]))
		s.set_alpha(self.color[3])
		s.fill(self.color)
		window.blit(s, (self.position[0],self.position[1]))
		self.renderValue(window)

	def mouseContact(self,pos):
		if not self.disabled and self.position[0] < pos[0] < self.position[0] + self.size[0]:
			if self.position[1] < pos[1] < self.position[1] + self.size[1]:
				return True
		return False

	def hoveredAnimation(self,pos,padding = 10,textPadding = 10):
		if self.big:
			self.big = False
			self.grow(-self.padding, -self.textPadding)
		if self.mouseContact(pos) and not self.disabled:
			self.grow(padding, textPadding)
			self.big = True

	def renderValue(self,window):
		font = pygame.font.SysFont('PrStart.ttf', self.textSize)
		text = font.render(self.value, False, self.textColor)
		width, height = text.get_size()
		window.blit(text, (self.position[0] + (self.size[0] - width) / 2,self.position[1] + (self.size[1] - height) / 2))

	def grow(self,padding, textPadding):
		self.position = (self.position[0] - padding,self.position[1] - padding * self.size[1] / self.size[0])
		self.size = (self.size[0] + padding * 2, self.size[1] + 2 * padding * self.size[1] / self.size[0])
		self.padding = padding
		self.textPadding = textPadding
		self.textSize += textPadding


#functions

def checkpos(x,y,array):
	freeTiles = []
	for i in [(0,1),(0,-1),(0,0),(1,0),(-1,0)]:
		if  array[(x+i[0])%len(array)][(y+i[1])%len(array[x])][0] in ["b","v","p"]:
			freeTiles.append(i)
	return freeTiles

def enemyCanMove(e,moveCounter):
	if e[2] == "0" and moveCounter % 3 != 0:
		return False
	if e[2] == "1" and moveCounter %2 != 0:
		return False
	return True

# def move(speed, levelMap,moveCounter):
# 	points = 0
# 	playerpos = (-1,-1)
# 	entitiesDone = []
# 	x1,y1 = speed #direction du mouvement
# 	irange = range(len(levelMap))
# 	if x1 < 0:
# 		irange = range(len(levelMap)-1,-1,-1)

# 	for i in irange: #on parcour le niveau

# 		jrange = range(len(levelMap[i]))
# 		if y1 < 0:
# 			jrange = range(len(levelMap[i])-1,-1,-1)
# 		for j in jrange:
# 			if levelMap[i][j][0] == "p" and levelMap[i][j] not in entitiesDone:
# 				entitiesDone.append(levelMap[i][j])
# 				playerpos = (i,j)
# 				#la case est une bille on peut y aller et on renvoi 1
# 				if  levelMap[(i+x1)%len(levelMap)][(j+y1)%len(levelMap[i])][0] == "b":
# 					levelMap[(i+x1)%len(levelMap)][(j+y1)%len(levelMap[i])] = levelMap[i][j]
# 					levelMap[i][j] = "v"
# 					points = 1

# 				#la case est vide on peut y aller
# 				if  levelMap[(i+x1)%len(levelMap)][(j+y1)%len(levelMap[i])][0] == "v":
# 					levelMap[(i+x1)%len(levelMap)][(j+y1)%len(levelMap[i])] = levelMap[i][j]
# 					levelMap[i][j] = "v"

# 				if  levelMap[(i+x1)%len(levelMap)][(j+y1)%len(levelMap[i])][0] == "e":
# 					levelMap[i][j] = "v"

# 			if levelMap[i][j][0] == "e" and levelMap[i][j] not in entitiesDone and speed != (0,0):
# 				if enemyCanMove(levelMap[i][j],moveCounter):
# 					entitiesDone.append(levelMap[i][j])
# 					if levelMap[i][j][2] != 3: 
# 						possibleSpeeds = checkpos(i,j,levelMap)
# 						try:
# 							x2, y2 = random.choice(possibleSpeeds)
# 						except:
# 							x2, y2 = 0, 0
# 					else:
# 						x2, y2 = x1, y1
# 					levelMap[(i+x2)%len(levelMap)][(j+y2)%len(levelMap[i])] = levelMap[i][j]
# 					levelMap[i][j] = "v"

# 	if playerpos == (-1,-1):
# 		return -1, levelMap

# 	#on ne peut pas aller sur la case
# 	return points, levelMap


def move(speed,levelMap,moveCounter):
	rows = len(levelMap)
	columns = len(levelMap[0])
	for row in rows:
		for column in columns:
			elements = levelMap[row][column].split("/")
			destination = levelMap[(row+speed[0])%rows][(column+speed[1])%columns]
			if elements[-1][0] == "p" and destination[0] != "m":
				levelMap[(row+speed[0])%rows][(column+speed[1])%columns] = elements[-1] + "/" + destination
				if len(elements) == 1:
					levelMap[row][column] = "v"
				else:
					levelMap[row][column] = elements[:-1]
	
	for row in rows:
		for column in columns:
			elements = levelMap[row][column].split("/")
			items = (elements[0][0],elements[1][0])
			levelMap[row][column] = elements[0]
			if len(elements) > 1:
				if items == ("p","b"):
					pass #+1 point
				if 






#affiche a l'ecran l'image contenue dans path, au coordonées (x,y) et de taille (w,h)
def renderSprite(window,path, x, y, w, h):
	try:
		sprite = pygame.image.load("assets/"+str(path)+".png").convert_alpha()
		sprite = pygame.transform.scale(sprite, (w, h))
		window.blit(sprite,(x,y))
	except:
		print("error loading texture of " + str(path) + ".png")
		exit()
		