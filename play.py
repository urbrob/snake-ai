from logic.game_modes import PlayerControlSnakeGame, PlayerControlSnakeGameLearn
from utils.consts import WIDTH, HEIGHT, SEPARATOR
import sys, getopt
import tkinter as tk

class App:
    def __init__(self, args):
        self.root = tk.Tk()
        self.root.title("Snake")
        self.root.resizable(False, False)
        opts, args = getopt.getopt(args, "ail")
        for opt, arg in opts:
            if opt == "-l":
                self.snake_canvas = PlayerControlSnakeGameLearn(WIDTH, HEIGHT, SEPARATOR, 1000//10)
                break
            elif opt == "-ai":
                self.snake_canvas = AiControllSnakeGame(WIDTH, HEIGHT, SEPARATOR, 1000//10)
                break
        else:
            self.snake_canvas = PlayerControlSnakeGame(WIDTH, HEIGHT, SEPARATOR, 1000//10)
        self.snake_canvas.pack()
        self.root.mainloop()



if __name__ == "__main__":
    App(sys.argv[-1:])
