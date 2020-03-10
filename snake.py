import tkinter as tk
from PIL import Image, ImageTk

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600,
            height=620,
            background="black",
            highlightthickness=0
        )
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 200)
        self.score = 0
        self._load_assets()
        self.create_objects()

    def _load_assets(self):
        self.snake_body_image = Image.open("/assets/snake.png")
        self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
        self.food_image = Image.open("/assets/food.png")
        self.food = ImageTk.PhotoImage(self.food_image)

    def create_objects(self):
        for x, y in self.snake_positions:
            self.create_image(x, y image=self.snake_body)


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.resizable(False, False)

    def _set_canvas(self, canvas):
        """Setting about main board on which all the magic happens."""
        self.board = canvas
        self.pack()

    def start(self):
        """Prepare everything and start a game."""
        self._set_canvas(Snake())
        self.root.mainloop()

if __name__ =="__main__":
    my_app = App()
    my_app.start()
