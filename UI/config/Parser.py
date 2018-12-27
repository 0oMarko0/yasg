class Parser:

    def __init__(self, path):
        self.FILE_PATH = path
        self.config_file = self.import_config()

    def import_config(self):
        return open(self.FILE_PATH, 'r')

    def get_config_file(self):
        return self.config_file
