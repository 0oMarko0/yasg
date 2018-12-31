from game.map.MapFactory import MapFactory

from game.snake.Snake import Snake


class Game:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self):
        self.game_map = MapFactory.build_map()
        self.snake = Snake(2, 2)

    def start(self):
        self.game_map.render_snake(self.snake.get_positions())

    def get_game_state(self):
        return self.game_map.map

    def movement(self, movement):
        if movement == self.UP:
            self.snake.move_up()
        elif movement == self.DOWN:
            self.snake.move_down()
        elif movement == self.LEFT:
            self.snake.move_left()
        elif movement == self.RIGHT:
            self.snake.move_right()

    def update(self):
        self.game_map.render_snake(self.snake.get_positions())

    def validate_snake_position(self):
        pass
