import sys

import pygame
from pygame.locals import *
from UI.grid.GridFactory import GridFactory
from config.colors.Colors import *
from config.game.MapConfig import *
from game.map.MapFactory import MapFactory

pygame.init()

DISPLAYSURF = pygame.display.set_mode((GRID_WITH, GRID_HEIGHT), 0, 32)
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption("S4n7eB0x")
pygame.key.set_repeat(1, 75)

game_map = MapFactory.build_map()
grid = GridFactory.build_grid(DISPLAYSURF, game_map)
grid.draw()

while True:

    for i in range(0, 5):
        game_map.calculate_snake_position(i, 2)
        grid.render()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


