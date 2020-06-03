from logic.game_functions import SnakeGameLogic, PlayerValidMovementLogic, GameSignals
from ui.board import SnakeBoardCanvas
from ui.objects import SnakeBodyCanvasObject, FoodCanvasObject
from ai.tools import prepare_move, commit_moves, predict_move


class SnakeGameAbstract:
    """Mixin is for createing easy template for snake game."""
    def init_game_logic(self, width, height, object_distance, game_speed):
        self.game_speed = game_speed
        self.logic = SnakeGameLogic(width, height, object_distance)

    def game_tick(self):
        self.before_move()
        next_move = self.get_next_move()
        game_signal = self.logic.run(next_move)
        if game_signal == GameSignals.LOST.value:
            self.lost()
        elif game_signal == GameSignals.ATE_FRUIT.value:
            self.ate_fruit()
        self.after_move()
        self.after(self.game_speed, self.game_tick)

    def lost(self):
        """Signal on lost game"""
        raise NotImplementedError()

    def ate_fruit(self):
        """Signal on eaten fruit."""
        raise NotImplementedError()

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
        self.after(game_speed, self.game_tick)

    def after_move(self):
        self.draw_canvas_objects(self.logic.food_position, self.logic.snake.body_parts)

    def before_move(self):
        self.clear_canvas_objects()

    def lost(self):
        exit()

    def ate_fruit(self):
        self.logic.eat_fruit()


class PlayerControlSnakeGame(CanvasSnakeGame):
    def __init__(self, width: int, height: int, object_distance: int, game_speed: int = 100):
        super().__init__(
            width, height, object_distance, game_speed
        )
        self.bind_all("<Key>", self.on_key_press)

    def on_key_press(self, event):
        """Event listener on every key pressed."""
        new_direction = event.keysym
        if PlayerValidMovementLogic().run(self.logic.move_direction, new_direction):
            self.logic.move_direction = new_direction

    def get_next_move(self):
        return self.logic.move_direction


class AiControllSnakeGame(CanvasSnakeGame):
    def get_next_move(self):
        return predict_move(prepare_move(self.logic.food_position, self.logic.snake, self.logic.move_direction))


class PlayerControlSnakeGameLearn(PlayerControlSnakeGame):
    def __init__(self, width: int, height: int, object_distance: int, game_speed: int = 100):
        super().__init__(
            width, height, object_distance, game_speed
        )
        self.move_set_memory = []

    def after_move(self):
        super().after_move()
        self.move_set_memory.append(prepare_move(self.logic.food_position, self.logic.snake, self.logic.move_direction, True))

    def ate_fruit(self):
        super().ate_fruit()
        commit_moves(self.move_set_memory)
        self.move_set_memory = []
