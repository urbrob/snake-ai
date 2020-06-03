from utils.generic import Coordinate2DObject

WIDTH = 800
HEIGHT = 800
SEPARATOR = 20
MOVE_SET = {
    "w": Coordinate2DObject(x=0, y=-SEPARATOR),
    "s": Coordinate2DObject(x=0, y=SEPARATOR),
    "a": Coordinate2DObject(x=-SEPARATOR, y=0),
    "d": Coordinate2DObject(x=SEPARATOR, y=0)
}
BANNED_CHANGE_DIRECTIONS = {
    "w": "s",
    "s": "w",
    "a": "d",
    "d": "a"
}
