import tkinter as tk
from typing import List
from ui.objects import CanvasObject, FoodCanvasObject, SnakeBodyCanvasObject


class SnakeBoardCanvas(tk.Canvas):
    def __init__(self, width: int, height: int, object_distance: int, game_speed: int = 100):
        super().__init__(
            width=width,
            height=height,
            background="black",
            highlightthickness=0
        )
        self.width = width
        self.height = height
        self.object_distance = object_distance
        self._draw_board()
        self.score_canvas = self._draw_score(0)
        self.current_objects = []

    def _draw_board(self) -> None:
        margin = self.object_distance // 2 + self.object_distance
        self.create_rectangle(
            margin,
            margin,
            (self.width // self.object_distance) * self.object_distance - margin,
            (self.height // self.object_distance) * self.object_distance - margin,
            outline="#525d69"
        )

    def _draw_score(self, score: int) -> int:
        return self.create_text(
            self.width // 2,
            self.object_distance // 2 ,
            text=f"Score : {score}",
            tag="Score",
            fill="#fff",
            font=("TkDefaultFont", 14),
        )

    def draw_canvas_objects(self, fruit, snake_parts):
        self.draw_canvas_object(FoodCanvasObject(*fruit.coordinates))
        for part in snake_parts:
            self.draw_canvas_object(SnakeBodyCanvasObject(*part.coordinates))

    def draw_canvas_object(self, canvas_object: CanvasObject) -> int:
        x, y, image, tag = canvas_object.draw_data.values()
        canvas_object.id = self.create_image(
            x,
            y,
            image=image,
            tag=tag
        )
        self.current_objects.append(canvas_object)

    def clear_canvas_objects(self):
        for canvas_object in self.current_objects:
            self.delete_canvas_object(canvas_object.id)
        self.current_objects = []

    def delete_canvas_object(self, object_id: int) -> None:
        self.delete(object_id)
