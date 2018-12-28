from config.game.MapConfigParser import MapConfigParser;

grid_parser = MapConfigParser()
config = grid_parser.get_grid_config()

CUBE_SIZE = config['CUBE_SIZE']
GRID_WITH = config['GRID_WIDTH']
GRID_HEIGHT = config['GRID_HEIGHT']
MARGIN_LEFT = config['MARGIN_LEFT']
MARGIN_RIGHT = config['MARGIN_RIGHT']
MARGIN_TOP = config['MARGIN_TOP']
MARGIN_BOTTOM = config['MARGIN_BOTTOM']
SHOW_GRID = True if config['SHOW_GRID'] == "true" else False
