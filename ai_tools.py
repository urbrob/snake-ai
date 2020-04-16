def commit_moves(moves):
    with open('data_snake.csv', 'w') as file:
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
    data.append(current_direction)
    return data


def predict_move(snake_data):
    pass
