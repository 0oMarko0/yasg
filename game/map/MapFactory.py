import math

from game.config.MapConfig import *
from game.map.Map import Map


class MapFactory:

    @staticmethod
    def build_map():
        row = math.floor((GRID_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM) / CUBE_SIZE)
        col = math.floor((GRID_WITH - MARGIN_LEFT - MARGIN_RIGHT) / CUBE_SIZE)

        return Map(row, col)

