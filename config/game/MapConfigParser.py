import json
import os


from config.Parser import Parser


class MapConfigParser:

    def __init__(self):
        self.grid_config = {}
        self.parser = Parser('/Users/marco/Workspace/Python/snake/config/game/default_map_config.json') # Get relative path
        self.parser.get_config_file()
        self.config_file = self.parser.get_config_file()
        self.build_map_config()

    def build_map_config(self):
        config = json.load(self.config_file)

        self.grid_config['CUBE_SIZE'] = config['cube_size']
        self.grid_config['GRID_WIDTH'] = config['grid_width']
        self.grid_config['GRID_HEIGHT'] = config['grid_height']
        self.grid_config['MARGIN_LEFT'] = config['margin_left']
        self.grid_config['MARGIN_RIGHT'] = config['margin_right']
        self.grid_config['MARGIN_TOP'] = config['margin_top']
        self.grid_config['MARGIN_BOTTOM'] = config['margin_bottom']
        self.grid_config['SHOW_GRID'] = config['show_grid']

    def get_grid_config(self):
        return self.grid_config




