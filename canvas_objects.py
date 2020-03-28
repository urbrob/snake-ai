from PIL import Image, ImageTk


class AbstarctCanvasObject:
    image = None
    canvas_image = None
    tag = None

    def __init__(self, x, y, canvas_id=None):
        self.x = x
        self.y = y
        self.canvas_id = None
        self.canvas_image = ImageTk.PhotoImage(self.image)

    def draw_object_on_canvas(self, canvas):
        self._draw_object(canvas)

    def _draw_object(self, canvas):
        self.canvas_id = canvas.create_image(self.x, self.y, image=self.canvas_image, tag=self.tag)

    @property
    def coordinates(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.x}, {self.y}"

class FoodObject(AbstarctCanvasObject):
    image = Image.open("./assets/food.png")
    tag = "food"


class SnakePartObject(AbstarctCanvasObject):
    next = None
    image = Image.open("./assets/snake.png")
    tag = "snake"

    def __add__(self, coords):
        return SnakePartObject(self.x + coords[0], self.y + coords[1], canvas_id=self.canvas_id)


class SnakeObject(AbstarctCanvasObject):
    """Represents snake in our game, it holds every SnakePartObject."""

    def __init__(self, x, y):
        self.body_parts = [SnakePartObject(x, y), SnakePartObject(x - 20, y), SnakePartObject(x - 40, y)]

    def draw_object_on_canvas(self, canvas):
        for body_part in self.body_parts:
            body_part.draw_object_on_canvas(canvas)

    def move(self, coordinates):
        self.body_parts = [self.body_parts[0] + coordinates] + self.body_parts[:-1]
