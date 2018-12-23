from cube.CubeFactory import CubeFactory
from cube.State import State


class Grid:

    def __init__(self, screen, cube_dimension):
        self.grid = [[]]
        self.cube_dimension = cube_dimension
        self.width, self.height = screen.get_size()
        self.validate_dimension()
        self.cube_factory = CubeFactory(screen, cube_dimension)

    def build(self):
        for i in range(0, self.width):
            row = []
            for j in range(0, self.height):
                coords = {'i': i * self.cube_dimension,'j': j * self.cube_dimension}
                cube = self.cube_factory.create_cube(State.INACTIVE, coords)
                row.append(cube)
            self.grid.append(row)

    def draw(self):
        for row in self.grid:
            for cube in row:
                cube.draw()

    def get_cube(self, coords):
        i = coords['i'] % self.height
        j = coords['j'] % self.width

        return self.grid[i][j]

    def change_cube_state(self, coords, state):
        cube = self.get_cube(coords)
        cube.change_state(state)
        cube.fill()
        self.update_cube(coords, cube)

    def update_cube(self, coords, cube):
        self.grid[coords['i']][coords['j']] = cube

    def validate_dimension(self):
        if self.width % self.cube_dimension != 0:
            raise ValueError('Width must be a multiple for the display width')

        if self.height % self.cube_dimension != 0:
            raise ValueError('Height must be a multiple for the display height')