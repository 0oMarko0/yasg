from config.colors.ColorParser import ColorParser

color_parser = ColorParser()
colors = color_parser.get_colors()

BACKGROUND = colors['BACKGROUND']
FOREGROUND = colors['FOREGROUND']
DANGER = colors['COLOR_6']
WARNING = colors['COLOR_5']
PRIMARY = colors['COLOR_3']
SECONDARY = colors['COLOR_1']
SNAKE = colors['COLOR_2']
BLACK = colors['COLOR_0']
