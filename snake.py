import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
from canvas_objects import SnakePartObject, FoodObject, SnakeObject


class Snake(tk.Canvas):
    MOVE_INCREMENT = 20
    MOVES_PER_SECOND = 15
    GAME_SPEED = 1000 // 15
    MOVE_DIRECTIONS = {
        "w": (0, -MOVE_INCREMENT),
        "s": (0, MOVE_INCREMENT),
        "a": (-MOVE_INCREMENT, 0),
        "d": (MOVE_INCREMENT, 0)
    }

    def __init__(self):
        super().__init__(
            width=600,
            height=620,
            background="black",
            highlightthickness=0
        )
        self.snake = SnakeObject(100, 100)
        self.food_position = FoodObject(200, 200)
        self.score = 0
        self.create_game_objects()

    def create_game_objects(self):
        self.create_text(45, 12, text=f"Score : {self.score}", tag="Score", fill="#fff", font=("TkDefaultFont", 14))
        self.food_position.draw_object_on_canvas(self)
        self.snake.draw_object_on_canvas(self)
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def update_canvas_objects_coordinates(self, canvas_object: list):
        for obj in canvas_object:
            self.coords(obj.canvas_id, obj.coordinates)

    def move_snake(self, direction: str):
        move_coordinates = self.MOVE_DIRECTIONS[direction]
        self.snake.move(move_coordinates)
        self.update_canvas_objects_coordinates(self.snake.body_parts)

    def perform_actions(self):
        self.move_snake("d")
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
        snake = Snake()
        self._set_canvas(snake)
        snake.perform_actions()
        self.root.mainloop()

if __name__ =="__main__":
    my_app = App()
    my_app.start()
