from tensorflow.keras import models
import numpy as np

model = models.load_model('ai/snake_ai_model.h5')
MOVING_MAPPING = {
    'a': 0,
    's': 1,
    'd': 2,
    'w': 3,
}
REVERSE_MOVING_MAPPING = {
    0: 'a',
    1: 's',
    2: 'd',
    3: 'w'
}

def commit_moves(moves):
    with open('ai/data_snake.csv', 'a+') as file:
        for move in moves:
            file.write(','.join(map(str, move)) + '\n')

def prepare_move(food_position, snake, current_direction, to_save=False):
    """Function to prepare data collected per move."""

    data = []
    for x in range(20, 600, 20):
        for y in range(40, 620, 20):
            if food_position.x == x and food_position.y == y:
                data.append(3)
            elif snake.body_parts[0].x == x and snake.body_parts[0].y == y:
                data.append(2)
            elif any(body_part.x == x and body_part.y == y for body_part in snake.body_parts[:-1]):
                data.append(1)
            else:
                data.append(0)
    if to_save:
        data.append(MOVING_MAPPING[current_direction])
    return data


def predict_move(snake_data):
    return REVERSE_MOVING_MAPPING[model.predict_classes(np.array([snake_data]))[0]]
