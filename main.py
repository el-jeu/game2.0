from pygame.locals import *
from levels import *
from header import *

import pygame
import random
import titleScreen

pygame.init()
pygame.font.init()
scoreFont = pygame.font.SysFont('PrStart.ttf', 30)

running = starting = True
screen = TITLE_SCREEN
level = 0
points = 0
finishedLevel = -1
reason = None

while running:
    if screen == TITLE_SCREEN:
        if starting:
            window = titleScreen.start(finishedLevel,reason)
            starting = False
        else:
            screen, buttonPressed = titleScreen.update(window)
            if screen == PLAY:
                level = buttonPressed
                starting = True

    if screen == CONTROLS:
        print("controls wip")
        screen = TITLE_SCREEN

    if screen == PLAY:
        if starting:
            frameTime = 100
            timer = 60
            pygame.time.set_timer(USEREVENT+1,frameTime)
            FLOOR, levelMap = levels[level]
            levelMap = [row[:] for row in levelMap]
            ROWS= len(levelMap)
            COLUMNS = len(levelMap[0])
            WIDTH = round(MAXWIDTH/len(levelMap))
            HEIGHT = round(MAXHEIGHT/len(levelMap[0]))
            window = pygame.display.set_mode((ROWS*WIDTH,COLUMNS*HEIGHT))
            pointsLeft = 1
            moveCounter = 0
            speed = (0,0)
            starting = False
            unpaused = True

        elif timer <= 0 or pointsLeft <= 0:
            screen = GAME_OVER
        else:
            for event in pygame.event.get():
                if event.type == QUIT: #bouton fermer
                    screen = BYE
                if event.type == KEYDOWN and event.key == K_UP: #"up"
                    speed = (0,-1)
                if event.type == KEYDOWN and event.key == K_DOWN: #"down"
                    speed = (0,1)
                if event.type == KEYDOWN and event.key == K_RIGHT: #"right"
                    speed = (1,0)
                if event.type == KEYDOWN and event.key == K_LEFT: #"left"
                    speed = (-1,0)
                if event.type == KEYDOWN and event.key == K_SPACE: #espace
                    unpaused = not unpaused
                    speed = (0,0)

                if event.type == USEREVENT+1 and unpaused:

                    #le joueur et l'enemi se deplacent
                    value, levelMap = move(speed,levelMap,moveCounter)
                    if value != -1:
                        points += value
                    else :
                        screen = GAME_OVER
                    if speed != (0,0):
                        moveCounter += 1

                    renderSprite(window, FLOOR, 0, 0, WIDTH * ROWS, HEIGHT * COLUMNS)

                    pointsLeft = 0
                    for x in range(len(levelMap)):
                        for y in range(len(levelMap[x])):
                            if levelMap[x][y][0] != "v":
                                renderSprite(window, levelMap[x][y][3:], x*WIDTH, y*HEIGHT, WIDTH, HEIGHT)
                            if levelMap[x][y][0] == "b":
                                pointsLeft += 1

                    #reinitialisation du veteur vitesse
                    speed = (0,0)

                    time = scoreFont.render("Time left : "+str(int(timer)), False, (255, 255, 255))
                    window.blit(time,(WIDTH * COLUMNS - 255,5))

                    timer -= frameTime / 1000

    if screen == GAME_OVER:
        print("game over")
        starting = True
        finishedLevel = level
        reason = WIN if pointsLeft == 0 else LOSE
        screen = TITLE_SCREEN

    if screen == SCORES:
        print("scores wip")
        screen = TITLE_SCREEN

    if screen == BYE:
        running = False

    score = scoreFont.render("Points : "+str(points), False, (255, 255, 255))
    window.blit(score,(10,5))

    pygame.display.update()
pygame.quit()