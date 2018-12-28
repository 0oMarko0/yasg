import sys

import pygame
from pygame.locals import *
from UI.grid.GridFactory import GridFactory
from game.config.MapConfig import *
from UI.config.colors.Colors import *
from game.map.Map import Map
from game.map.MapFactory import MapFactory

pygame.init()

DISPLAYSURF = pygame.display.set_mode((GRID_WITH, GRID_HEIGHT), 0, 32)
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption("S4n7eB0x")
pygame.key.set_repeat(1, 75)

pygame.draw.rect(DISPLAYSURF, DANGER, (20, 0, 100, 50))

game_map = MapFactory.build_map()
grid = GridFactory.build_grid(DISPLAYSURF, game_map)
grid.draw()
grid.fill(2, 2, WARNING)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


