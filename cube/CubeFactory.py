from cube.Cube import Cube


class CubeFactory:
    def __init__(self, screen, dimension):
        self.screen = screen
        self.dimension = dimension

    def create_cube(self, state, coords):
        return Cube(self.screen, self.dimension, state, coords)
