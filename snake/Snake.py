import pygame
from cube.State import State


class Snake:
    # Screen could be in a service Locator
    def __init__(self, grid):
        self.grid = grid
        self.length = 1
        self.position = {'i': 1, 'j': 3}
        self.head = self.birth()
        self.head.draw()

    def birth(self):
        cube = self.grid.get_cube(self.position)
        return cube

    def eat(self):
        self.length = self.length + 1

    def movement(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: # Go left
                    print("Left")
                    self.position['i'] = self.position['i'] - 1
                if event.key == pygame.K_s: # Go down
                    print("Down")
                    self.position['j'] = self.position['j'] + 1
                if event.key == pygame.K_d: # Go right
                    print("Right")
                    self.position['i'] = self.position['i'] + 1
                if event.key == pygame.K_w: # Go up
                    print("Up")
                    self.position['j'] = self.position['j'] - 1
                self.update()

    def growth(self):
        self.length = self.length + 1
        print("Lenght ", self.length)

    def update(self):
        self.head.border()
        self.head.change_state(State.INACTIVE)

        next_cube = self.grid.get_cube(self.position)
        if next_cube.get_state() == State.FOOD:
            self.growth()

        self.head = next_cube
        self.head.fill()
        self.head.change_state(State.SNAKE)
