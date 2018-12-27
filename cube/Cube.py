import pygame
from cube.State import State


class Cube:

    def __init__(self, screen, dimension, state, coords):
        self.screen = screen
        self.dimension = dimension
        self.state = state
        self.coords = coords
        self.color = BACKGROUND
        self.thickness = 1
        self.change_state(state)

    def get_state(self):
        return self.state

    def change_state(self, state):
        self.state = state
        self.change_color(state)
        self.draw()

    def change_color(self, state):
        state_options = {
            State.INACTIVE: FOREGROUND,
            State.ACTIVE: PRIMARY,
            State.FOOD: DANGER,
            State.SNAKE: SNAKE
        }

        self.color = state_options[state]

    def fill(self):
        self.thickness = 0
        self.draw()

    def border(self):
        self.thickness = 1
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.coords['i'], self.coords['j'], self.dimension, self.dimension), self.thickness)

    def __repr__(self):
        return "coords: ({0}, {1})  state: {2}".format(self.coords['i'], self.coords['j'],  self.state)

