import tkinter as tk
from PIL import Image, ImageTk
from canvas_objects import SnakePartObject, FoodObject, SnakeObject


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600,
            height=620,
            background="black",
            highlightthickness=0
        )
        self.snake_head = SnakeObject(100, 100)
        self.food_position = FoodObject(200, 200)
        self.score = 0
        self.create_game_objects()

    def create_game_objects(self):
        self.create_text(45, 12, text=f"Score : {self.score}", tag="Score", fill="#fff", font=("TkDefaultFont", 14))
        self.food_position.draw_object_on_canvas(self)
        self.snake_head.draw_object_on_canvas(self)
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")


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

if __name__ =="__main__":
    my_app = App()
    my_app.start()
