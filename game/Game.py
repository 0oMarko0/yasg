from game.map.State import State
from game.map.Map import Map


class Game:

    def __init__(self):
        self.map = Map(10, 10)

    def start(self):
        self.map.set_state_at(0, 0, State.SNAKE)

