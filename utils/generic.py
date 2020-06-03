from typing import Tuple


class Coordinate2DObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates(self) -> Tuple[int, int]:
        """Return x, y coordinates of object on map."""
        return self.x, self.y


    def __add__(self, coordinate):
        return self.__class__(self.x + coordinate.x, self.y + coordinate.y)
