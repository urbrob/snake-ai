import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
from canvas_objects import SnakePartObject, FoodObject, SnakeObject


class Snake(tk.Canvas):
    MOVE_INCREMENT = 20
    MOVES_PER_SECOND = 15
    GAME_SPEED = 1000 // 15
    MOVE_DIRECTIONS = {
        "Up": (0, -MOVE_INCREMENT),
        "Down": (0, MOVE_INCREMENT),
        "Left": (-MOVE_INCREMENT, 0),
        "Right": (MOVE_INCREMENT, 0),
    }

    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0
        )
        self.snake = SnakeObject(100, 100)
        self.food_position = FoodObject(200, 200)
        self.score = 0
        self.current_direction = "Right"
        self.bind_all("<key>", self.on_key_press)
        self.__create_game_objects()
        self.perform_actions()

    def __create_game_objects(self):
        """Creates initial game objects like snake and food."""
        self.create_text(
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
        x_cord, y_cord = self.snake.body_parts[0].coordinates
        return x_cord in (0, 600) or y_cord in (20, 620)

    def check_if_snake_ate_himself(self):
        """Retrun if snake ate himself."""
        x_cord, y_cord = self.snake.body_parts[0].coordinates
        return any((x_cord, y_cord) in body_part.coordinates for body_part in self.snake.body_parts[1:])

    def on_key_press(self, e):
        new_direction = e.keysym
        self.direction = new_direction

    def perform_actions(self):
        self.move_snake(self.current_direction)
        if self.check_snake_collision_with_wall() or self.check_if_snake_ate_himself():
            return
        self.after(self.GAME_SPEED, self.perform_actions)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.resizable(False, False)

    def _set_canvas(self, canvas):
        """Setting about main board on which all the magic happens."""
        self.board = canvas
        self.board.pack()

    def start(self):
        """Prepare everything and start a game."""
        self._set_canvas(Snake())
        self.root.mainloop()


if __name__ == "__main__":
    my_app = App()
    my_app.start()
