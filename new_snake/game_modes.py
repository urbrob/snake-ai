from logic import SnakeGameLogic, PlayerValidMovementLogic
from board import SnakeBoardCanvas
from canvas_objects import SnakeBodyCanvasObject, FoodCanvasObject

class SnakeGameAbstract:
    """Mixin is for createing easy template for snake game."""
    def init_game_logic(self, width, height, object_distance, game_speed):
        self.game_speed = game_speed
        self.logic = SnakeGameLogic(width, height, object_distance)

    def game_tick(self):
        self.before_move()
        next_move = self.get_next_move()
        self.logic.run(next_move)
        self.after_move()

    def after_move(self):
        """Additional function to easy extend logic AFTER move."""
        pass

    def before_move(self):
        """Additional function to easy extend logic BEFORE move."""
        pass

    def get_next_move(self, *args, **kwargs) -> str:
        """This function should implement how snake should get his next move."""
        raise NotImplementedError()


class CanvasSnakeGame(SnakeGameAbstract, SnakeBoardCanvas):
    def __init__(self, width: int, height: int, object_distance: int, game_speed: int = 100):
        super().__init__(
            width,
            height,
            object_distance,
            game_speed
        )
        self.init_game_logic(width, height, object_distance, game_speed)

    def after_move(self):
        self.clear_canvas_objects()

    def before_move(self):
        self.draw_canvas_objects(self.logic.food_position, self.logic.snake.body_parts)

class PlayerControlSnakeGame(CanvasSnakeGame):
    def __init__(self, width: int, height: int, object_distance: int, game_speed: int = 100):
        super().__init__(
            width, height, object_distance, game_speed
        )
        self.bind_all("<Key>", self.on_key_press)
        self.after(game_speed, self.game_tick)

    def on_key_press(self, event):
        """Event listener on every key pressed."""
        new_direction = event.keysym
        if PlayerValidMovementLogic().run(self.logic.move_direction, new_direction):
            self.logic.move_direction = new_direction

    def get_next_move(self):
        return self.logic.move_direction
