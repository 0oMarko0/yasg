import sys

import pygame
from pygame.locals import *
from UI.grid.GridFactory import GridFactory
from config.colors.Colors import *
from config.game.MapConfig import *
from game.Game import Game

pygame.init()

DISPLAYSURF = pygame.display.set_mode((GRID_WITH, GRID_HEIGHT), 0, 32)
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption("S4n7eB0x")
pygame.key.set_repeat(1, 75)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

game = Game()
game.start()
grid = GridFactory.build_grid(DISPLAYSURF, game.game_map)
grid.draw()

while True:
    game.update()
    grid.render()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                game.movement(UP)
            elif event.key == K_s:
                game.movement(DOWN)
            elif event.key == K_a:
                game.movement(LEFT)
            elif event.key == K_d:
                game.movement(RIGHT)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


