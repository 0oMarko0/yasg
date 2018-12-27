from UI.config.grid.Grid import *
from UI.grid.Grid import Grid


class GridFactory:

    @staticmethod
    def build_grid(screen):
        return Grid(screen, CUBE_SIZE, GRID_WITH, GRID_HEIGHT, SHOW_GRID,
                    MARGIN_LEFT, MARGIN_RIGHT, MARGIN_TOP, MARGIN_BOTTOM)

