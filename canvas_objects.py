class AbstarctCanvasObject:
    image = None
    canvas_image = ImageTk.PhotoImage(image)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_object_on_canvas(self, canvas):
        self._draw_object(self, canvas)

    def _draw_object(self, canvas):
        canvas.create_image(self.x, self.y, image=self.canvas_image)


class FoodObject(AbstarctCanvasObject):
    image = Image.open("/assets/food.png")


class SnakePartObject(AbstarctCanvasObject):
    next = None
    image = Image.open("/assets/snake.png")

class SnakeObject:
    """Represents snake in our game, it holds every SnakePartObjectobject."""

    def __init__(self, x, y):
        self.body_parts = [SnakePartObject(x, y), SnakePartObject(x - 20, y), SnakePartObject(x - 40, y)]
