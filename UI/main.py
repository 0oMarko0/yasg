from Parser.colors import ColorParser

color_parser = ColorParser()
color_parser.import_config()

print(color_parser.get_colors())