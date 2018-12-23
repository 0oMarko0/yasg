import pygame, sys
from pygame.locals import *
from colors.Colors import *
from grid.Grid import Grid
from cube.State import State
from snake.Snake import Snake

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
DISPLAYSURF.fill(BACKGROUND)
pygame.display.set_caption("S4n7eB0x")
pygame.key.set_repeat(1, 75)

grid = Grid(DISPLAYSURF, 20)
grid.build()
grid.draw()

grid.change_cube_state({'i': 1, 'j': 2}, State.FOOD)
snake = Snake(grid)

while True:
    snake.movement()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


