class AbstarctCanvasObject:
    image = None
    canvas_image = ImageTk.PhotoImage(image)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_object_on_canvas(self, canvas):
        canvas.create_image(self.x, self.y image=self.canvas_image)


class FoodObject:
    image = Image.open("/assets/food.png")


class SnakePartObject:
    image = Image.open("/assets/snake.png")
