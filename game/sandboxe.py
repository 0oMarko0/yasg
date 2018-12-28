from game.map.State import State
from game.map.Node import Node
from game.map.Map import Map


map = Map(10, 10)
map.set_state_at(5,5, State.FOOD)
print(map.at_position(5, 5))
print(map)
