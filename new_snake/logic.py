from typing import List, Tuple
from random import randint
from generic import Coordinate2DObject
from consts import MOVE_SET, BANNED_CHANGE_DIRECTIONS


class AbstractLogic:
    def run(self):
        raise NotImplementedError("You have to implement run method for every type of logic")


class CollisionLogic(AbstractLogic):
    """Collision logic task is to check if collision has occurd between two objects"""

    def run(self, object_A: Coordinate2DObject, object_B: Coordinate2DObject) -> bool:
        """Return boolean value if every coordinates are same in both objects"""
        return object_A.coordinates == object_B.coordinates


class GlobalCollisionLogic(CollisionLogic):
    """Collision logic task is to check if given object collide in any other object on the map."""

    def run(self, object: Coordinate2DObject, map_objects: List[Coordinate2DObject]) -> bool:
        return any(super(GlobalCollisionLogic, self).run(object, map_object) for map_object in map_objects)

class MapBoundCollisionLogic(AbstractLogic):
    """His task is to check if given object fall off from the map."""

    def __init__(self, map_width: int, map_height: int, separator: int):
        self.width, self.height, self.separator = map_width, map_height, separator

    def run(self, object: Coordinate2DObject,) -> bool:
        statements = [
            object.x < self.separator * 2,
            object.y < self.separator * 2,
            object.y > self.height - self.separator * 2,
            object.x > self.width - self.separator * 2
        ]
        return any(statements)


class SpawnLogic(AbstractLogic):
    """Spawn logic task is to generate x, y coordinates for newly created object."""

    def __init__(self, width: int, height: int, separator: int):
        self.width, self.height, self.separator = width, height, separator

    def run(self, map_objects: List[Coordinate2DObject]) -> Coordinate2DObject:
        """Return x, y values of newly generated position on map."""
        while True:
            x = self._generate_new_position(self.width)
            y = self._generate_new_position(self.height)
            if not GlobalCollisionLogic().run(Coordinate2DObject(x, y), map_objects):
                return Coordinate2DObject(x, y)

    def _generate_new_position(self, max: int) -> Tuple[int, int]:
        return randint(self.separator * 2, max - self.separator * 2) // self.separator * self.separator


class SnakeObjectLogic(AbstractLogic):
    def __init__(self, x_positon_start: int, y_position_start: int, separator: int):
        self.body_parts = [
            Coordinate2DObject(x_positon_start, y_position_start),
            Coordinate2DObject(x_positon_start - separator, y_position_start),
            Coordinate2DObject(x_positon_start - separator * 2, y_position_start)
        ]

    @property
    def tail(self) -> Coordinate2DObject:
        return self.body_parts[-1]

    @property
    def head(self) -> Coordinate2DObject:
        return self.body_parts[0]

    def run(self, direction: str) -> None:
        """Snake logic is just to move in direction dictated by code above it."""

        head_position_after_move = self.head + MOVE_SET[direction]
        self.body_parts = [head_position_after_move] + self.body_parts[:-1]

    def grow(self) -> None:
        self.body_parts = self.body_parts + [self.tail]


class SnakeGameLogic(AbstractLogic):
    """Whole game logic droped in one place."""

    def __init__(self, width: int, height: int, separator: int):
        self.width, self.height, self.separator = width, height, separator
        self.spawn_logic = SpawnLogic(width, height, separator)
        self.bound_logic = MapBoundCollisionLogic(width, height, separator)
        self.init_game_objects()
        self.move_direction = "w"

    def init_game_objects(self):
        self.snake = SnakeObjectLogic(200, 200, self.separator)
        self.food_position = self.spawn_logic.run(
            self.snake.body_parts
        )

    def eat_fruit(self):
        self.snake.grow()
        self.food_position = self.spawn_logic.run(
            self.snake.body_parts + [self.food_position]
        )

    def run(self, direction: str) -> bool:
        """Snake Game logic run is one whole one move in snake game."""
        self.snake.run(direction)
        if self.bound_logic.run(self.snake.head) or GlobalCollisionLogic().run(self.snake.head, self.snake.body_parts[1:]):
            return True
        elif CollisionLogic().run(self.snake.head, self.food_position):
            self.eat_fruit()
        return False


class PlayerValidMovementLogic(AbstractLogic):
    """It purpose is to check if new direction is valid with current_direction."""

    def run(self, current_direction: str, new_direction: str) -> bool:
        return new_direction != BANNED_CHANGE_DIRECTIONS[current_direction] and new_direction in ['w', 's', 'a', 'd']
