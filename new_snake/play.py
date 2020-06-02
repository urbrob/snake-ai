from game_modes import PlayerControlSnakeGame
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake")
    root.resizable(False, False)
    snake_canvas = PlayerControlSnakeGame(800, 800, 20, 1000//10)
    snake_canvas.pack()
    root.mainloop()
