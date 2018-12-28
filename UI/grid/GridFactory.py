from game.config.MapConfig import *
from UI.grid.Grid import Grid


class GridFactory:

    @staticmethod
    def build_grid(screen, game_map):
        return Grid(screen, game_map, CUBE_SIZE, GRID_WITH, GRID_HEIGHT, SHOW_GRID,
                    MARGIN_LEFT, MARGIN_RIGHT, MARGIN_TOP, MARGIN_BOTTOM)

