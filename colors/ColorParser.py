import json


class ColorParser:

    def __init__(self):
        self.colors = []
        self.FILE_PATH = '/Users/marco/Workspace/Python/snake/default_color_config.json'
        self.config_file = self.import_color()
        self.build_color()

    def import_color(self):
        return open(self.FILE_PATH, 'r')

    def convert_hex_to_rgb(self, hex):
        hex_striped = hex.lstrip('#')
        return tuple(int(hex_striped[i:i+2], 16) for i in (0, 2, 4))

    def build_color(self):
        colors = json.load(self.config_file)
        self.colors = list(map(self.convert_hex_to_rgb, colors['color']))

        tmp = {
            'BACKGROUND': self.convert_hex_to_rgb(colors['background']),
            'FOREGROUND': self.convert_hex_to_rgb(colors['foreground'])
        }

        for i in range(0, len(self.colors)):
            color_name = 'COLOR_{}'.format(i)
            tmp[color_name] = self.colors[i]

        self.colors = tmp

    def get_colors(self):
        return self.colors




