import random

from game.map.Node import Node
from game.map.State import State


class Map:

    def __init__(self, row, col):
        self.map = [[Node() for j in range(col)] for i in range(row)]
        self.row = row
        self.col = col

    def at_position(self, i, j):
        return self.map[i][j]

    def get_state_at(self, i, j):
        return self.at_position(i, j).get_state()

    def set_state_at(self, i, j, state):
        self.at_position(i, j).set_state(state)

    def generate_random_food(self):
        random_row = random.randint(0, self.row)
        random_col = random.randint(0, self.col)

        self.set_state_at(random_row, random_col, State.FOOD)

    def render_snake(self, snake):
        for row in snake:
            self.set_state_at(row[0], row[1], State.SNAKE)

    def __str__(self):
        return '\n'.join(' | '.join(map(str, self.row)) for self.row in self.map)

