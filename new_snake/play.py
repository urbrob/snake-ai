from game_modes import PlayerControlSnakeGame
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.resizable(False, False)
        self.snake_canvas = PlayerControlSnakeGame(800, 800, 20, 1000//10)
        self.snake_canvas.pack()
        self.root.mainloop()


if __name__ == "__main__":
    App()
