class Snake:

    def __init__(self, i, j):
        self.body = [[i, j]]

    def eat(self, i, j):
        self.body.append([i, j])

    def get_positions(self):
        return self.body

    def lateral_movement(self, orientation):
        current_position = self.body[0][0]
        self.body[0][0] = current_position + orientation

    def horizontal_movement(self, orientation):
        current_position = self.body[0][1]
        self.body[0][1] = current_position + orientation

    def move_up(self):
        self.horizontal_movement(-1)

    def move_down(self):
        self.horizontal_movement(1)

    def move_left(self):
        self.lateral_movement(-1)

    def move_right(self):
        self.lateral_movement(1)


