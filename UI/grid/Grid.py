import math
import pygame

from UI.config.colors.Colors import *
from game.map.State import State


class Grid:

    def __init__(self, screen, game_map, cube_size, grid_width, grid_height, show_grid,
                 margin_l=0, margin_r=0, margin_t=0, margin_b=0):
        self.grid = game_map
        self.screen = screen
        self.cube_size = cube_size
        self.height = grid_height
        self.width = grid_width
        self.margin_l = margin_l
        self.margin_r = margin_r
        self.margin_t = margin_t
        self.margin_b = margin_b
        self.color = FOREGROUND if show_grid else BACKGROUND
        self.validate_dimension()
        self.render()

    def get_cube(self, coords):
        i = coords['i'] % self.height
        j = coords['j'] % self.width

        return self.grid[i][j]

    def draw(self):
        self.draw_row()
        self.draw_col()

    def draw_row(self):
        row_step = math.floor(self.calculate_grid_height() / self.cube_size)

        for row in range(0, row_step + 1):
            left = (self.margin_l, self.margin_t + row*self.cube_size)
            right = (self.grid_right(), self.margin_t + row*self.cube_size)
            pygame.draw.line(self.screen, self.color, left, right, 1)

    def draw_col(self):
        col_step = math.floor(self.calculate_grid_width() / self.cube_size)

        for col in range(0, col_step + 1):
            left = (self.margin_l + col*self.cube_size, self.margin_t)
            right = (self.margin_l + col*self.cube_size, self.grid_bottom())
            pygame.draw.line(self.screen, self.color, left, right, 1)

    def calculate_grid_height(self):
        return self.height - self.margin_t - self.margin_b

    def calculate_grid_width(self):
        return self.width - self.margin_l - self.margin_r

    def grid_top(self):
        return self.height - (self.height - self.margin_t)

    def grid_bottom(self):
        return self.height - self.margin_b

    def grid_left(self):
        return self.width - (self.width - self.margin_l)

    def grid_right(self):
        return self.width - self.margin_r

    def fill(self, i, j, color):
        top_left = self.pixel_position(i, j);
        pygame.draw.rect(self.screen, color, (top_left['x'], top_left['y'], self.cube_size - 1, self.cube_size - 1))

    def pixel_position(self, i, j):
        grid_top = self.grid_top() + 1
        grid_left = self.grid_left() + 1

        x = grid_top + i*self.cube_size
        y = grid_left + j*self.cube_size

        return {'x': x, 'y': y}

    def render(self):
        self.grid.generate_random_food()
        for i in range(0, self.grid.row):
            for j in range(0, self.grid.col):
                if self.grid.get_state_at(i, j) == State.FOOD:
                    self.fill(i, j, PRIMARY)
                if self.grid.get_state_at(i, j) == State.SNAKE:
                    self.fill(i, j, SNAKE)

    def validate_dimension(self):
        if self.width % self.cube_size != 0:
            raise ValueError('Width must be a multiple of the display width')

        if self.height % self.cube_size != 0:
            raise ValueError('Height must be a multiple of the display height')
