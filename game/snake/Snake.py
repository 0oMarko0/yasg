class Snake:

    def __init__(self, i, j):
        self.body = [(i, j)]

    def eat(self, i, j):
        self.body.append((i, j))
