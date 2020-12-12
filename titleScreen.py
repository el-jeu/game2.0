import pygame
from pygame.locals import *
from header import *

levelsX,levelsY = 110,115

buttons = [ button(280, 430, 200,50,"Controls",102),
            button(20, 430, 200,50,"Scores",105),

            button(levelsX+10, levelsY+10, 50,50,"1-1",0),
            button(levelsX+80, levelsY+10, 50,50,"1-2",1),
            button(levelsX+150,levelsY+10, 50,50,"1-3",2),
            button(levelsX+220,levelsY+10, 50,50,"?-?",12),
            button(levelsX+10, levelsY+80, 50,50,"2-1",3),
            button(levelsX+80, levelsY+80, 50,50,"2-2",4),
            button(levelsX+150,levelsY+80, 50,50,"2-3",5),
            button(levelsX+220,levelsY+80, 50,50,"?-?",13),
            button(levelsX+10, levelsY+150,50,50,"3-1",6),
            button(levelsX+80, levelsY+150,50,50,"3-2",7),
            button(levelsX+150,levelsY+150,50,50,"3-3",8),
            button(levelsX+220,levelsY+150,50,50,"?-?",14),
            button(levelsX+10, levelsY+220,50,50,"4-1",9),
            button(levelsX+80, levelsY+220,50,50,"4-2",10),
            button(levelsX+150,levelsY+220,50,50,"4-3",11),
            button(levelsX+220,levelsY+220,50,50,"?-?",15)]

def start(finishedLevel,reason):
    if finishedLevel != -1:
        disabledButton = next(filter(lambda button: button.id == finishedLevel, buttons))
        disabledButton.disabled = True
        if reason == WIN:
            disabledButton.color = (55,255,55,100)
        else:
            disabledButton.color = (255,55,55,100)
    return pygame.display.set_mode((500,500))

def update(window):
    renderSprite(window, "f1", 0, 0, window.get_size()[0], window.get_size()[1])

    for button in buttons:
        button.draw(window)

    for event in pygame.event.get():
        if event.type == QUIT:
            return BYE, -1
        if event.type == MOUSEMOTION:
            for button in buttons:
                button.hoveredAnimation(event.pos)

        if event.type == MOUSEBUTTONUP:
            for button in buttons:
                if button.mouseContact(event.pos):
                    if button.id < MAXLVL:
                        return PLAY, button.id
                    return button.id, -1
    return TITLE_SCREEN, -1