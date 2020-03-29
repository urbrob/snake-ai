from PIL import Image, ImageTk


class AbstarctCanvasObject:
    """Represents single object in canvas map."""

    image = None
    canvas_image = None
    tag = None

    def __init__(self, x, y, canvas_id=None):
        self.x = x
        self.y = y
        self.canvas_id = canvas_id
        self.canvas_image = ImageTk.PhotoImage(self.image)

    def draw_object_on_canvas(self, canvas):
        self._draw_object(canvas)

    def _draw_object(self, canvas):
        self.canvas_id = canvas.create_image(
            self.x, self.y, image=self.canvas_image, tag=self.tag
        )

    @property
    def coordinates(self):
        return self.x, self.y

    def move(self, x, y):
        """Change object x and y position."""
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


class FoodObject(AbstarctCanvasObject):
    image = Image.open("./assets/food.png")
    tag = "food"


class SnakePartObject(AbstarctCanvasObject):
    next = None
    image = Image.open("./assets/snake.png")
    tag = "snake"


class SnakeObject:
    """Represents snake in our game, it holds every SnakePartObject."""

    def __init__(self, x, y):
        self.body_parts = [
            SnakePartObject(x, y),
            SnakePartObject(x - 20, y),
            SnakePartObject(x - 40, y),
        ]

    def draw_object_on_canvas(self, canvas):
        """Draw every part of the snake at canvas board."""
        for body_part in self.body_parts:
            body_part.draw_object_on_canvas(canvas)

    def move(self, coordinates):
        """Move last part of the snake given coordinates (x, y)."""
        last_part_of_body = self.body_parts.pop()
        x_cord = self.body_parts[0].x + coordinates[0]
        y_cord = self.body_parts[0].y + coordinates[1]
        last_part_of_body.move(x_cord, y_cord)
        self.body_parts.insert(0, last_part_of_body)
