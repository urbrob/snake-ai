from typing import Tuple
from utils.generic import Coordinate2DObject
from PIL import Image, ImageTk


class CanvasObject(Coordinate2DObject):
    """Represents single object in canvas map."""
    image_src = None
    tag = 'generic'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.canvas_image = ImageTk.PhotoImage(file=self.image_src)

    @property
    def draw_data(self) -> dict:
        """Returns dictionary of data required to draw object."""
        return {
            'x': self.x,
            'y': self.y,
            'image': self.canvas_image,
            'tag': self.tag
        }


class FoodCanvasObject(CanvasObject):
    """Represents food object in canvas map"""
    image_src = "assets/food.png"
    tag = "food"


class SnakeBodyCanvasObject(CanvasObject):
    """Represents body part object in canvas map"""
    image_src = "assets/snake.png"
    tag = "snake"
