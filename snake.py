import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
from canvas_objects import SnakePartObject, FoodObject, SnakeObject
from ai_tools import commit_moves, prepare_move


class Snake(tk.Canvas):
    MOVE_INCREMENT = 20
    MOVES_PER_SECOND = 10
    GAME_SPEED = 1000 // MOVES_PER_SECOND
    MOVE_DIRECTIONS = {
        "w": (0, -MOVE_INCREMENT),
        "s": (0, MOVE_INCREMENT),
        "a": (-MOVE_INCREMENT, 0),
        "d": (MOVE_INCREMENT, 0),
    }
    BANNED_CHANGE_DIRECTIONS = {
        "w": "s",
        "s": "w",
        "a": "d",
        "d": "a"
    }

    def __init__(self, game_mode=0):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )
        self.snake = SnakeObject(100, 100)
        self.food_position = FoodObject(200, 200)
        self.score = 0
        self.current_direction = "d"
        self.bind_all("<Key>", self.on_key_press)
        self.__create_game_objects()
        self.game_mode = game_mode
        self.move_memory = []
        self.perform_actions()


    def __create_game_objects(self):
        """Creates initial game objects like snake and food."""
        self.score_canvas = self.create_text(
            45,
            12,
            text=f"Score : {self.score}",
            tag="Score",
            fill="#fff",
            font=("TkDefaultFont", 14),
        )
        self.food_position.draw_object_on_canvas(self)
        self.snake.draw_object_on_canvas(self)
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def update_canvas_objects_coordinates(self, canvas_object: list):
        """Updates every given canvas object at canvas board with their current x/y position."""
        for obj in canvas_object:
            self.coords(obj.canvas_id, obj.coordinates)

    def move_snake(self, direction: str):
        """Perform_snake movement based on w/s/d/a input."""
        move_coordinates = self.MOVE_DIRECTIONS[direction]
        self.snake.move(move_coordinates)
        self.update_canvas_objects_coordinates([self.snake.body_parts[0]])

    def check_snake_collision_with_wall(self):
        """Return if snake is out of the bounds."""
        x_cord, y_cord = self.snake.head_coords
        return x_cord in (0, 600) or y_cord in (20, 620)

    def check_if_snake_ate_himself(self):
        """Retrun if snake ate himself."""
        x_cord, y_cord = self.snake.head_coords
        return any((x_cord, y_cord) == body_part.coordinates for body_part in self.snake.body_parts[1:])

    def on_key_press(self, e):
        """Event listener on every key pressed."""
        new_direction = e.keysym
        if new_direction != self.BANNED_CHANGE_DIRECTIONS[self.current_direction]:
            self.current_direction = new_direction

    def check_collision_with_fruit(self):
        """Check if snake jumped on fruit."""
        return self.snake.head_coords == self.food_position.coordinates

    def eat_fruit(self):
        """Make increase score and add respawn food in a new place."""
        self.score += 1
        self.itemconfigure(self.score_canvas, text=f"Score : {self.score}")
        self.food_position.respawn()
        self.update_canvas_objects_coordinates([self.food_position])

    def perform_actions(self):
        self.move_snake(self.current_direction)
        if self.check_snake_collision_with_wall() or self.check_if_snake_ate_himself():
            return
        elif self.check_collision_with_fruit():
            self.eat_fruit()
            self.snake.grow(self)
            if self.game_mode == 1:
                commit_moves(self.move_memory)
        if self.game_mode == 1:
            self.move_memory.append(prepare_move(self.food_position, self.snake, self.current_direction))
        self.after(self.GAME_SPEED, self.perform_actions)


class App:
    def __init__(self, mode=0):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.resizable(False, False)
        self.mode = mode

    def _set_canvas(self, canvas):
        """Setting about main board on which all the magic happens."""
        self.board = canvas
        self.board.pack()

    def start(self):
        """Prepare everything and start a game."""
        self._set_canvas(Snake(game_mode=self.mode))
        self.root.mainloop()


if __name__ == "__main__":
    my_app = App()
    my_app.start()
