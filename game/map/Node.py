from game.map.State import State


class Node:

    def __init__(self):
        self.state = State.INACTIVE

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def __repr__(self):
        return self.state

    def __str__(self):
        return str(self.state.value)
