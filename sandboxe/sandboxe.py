import sys

import pygame
from pygame.locals import *
from UI.grid.GridFactory import GridFactory
from UI.config.grid.Grid import *
from UI.config.colors.Colors import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((GRID_WITH, GRID_HEIGHT), 0, 32)
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption("S4n7eB0x")
pygame.key.set_repeat(1, 75)

grid = GridFactory.build_grid(DISPLAYSURF)
grid.draw()

# width = GRID_WITH
# height = GRID_HEIGHT
# # cube_size = CUBE_SIZE
#
# col_step = math.floor(width / cube_size)
# row_step = math.floor(height / cube_size)

# for row in range(0, row_step):
#     pygame.draw.line(DISPLAYSURF, FOREGROUND, (0, row * cube_size), (width, row * cube_size), 1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


