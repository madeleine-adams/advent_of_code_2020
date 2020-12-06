import math

position = (0, 0)
memory_map = dict()
current_value = 1
memory_map[position] = current_value
memory_index = 1


def find_value(coordinate, value_map):
    value = 0
    coords_to_check = [(coordinate[0], coordinate[1]+1),
                       (coordinate[0], coordinate[1]-1),
                       (coordinate[0]+1, coordinate[1]),
                       (coordinate[0]+1, coordinate[1]+1),
                       (coordinate[0]+1, coordinate[1]-1),
                       (coordinate[0]-1, coordinate[1]),
                       (coordinate[0]-1, coordinate[1]+1),
                       (coordinate[0]-1, coordinate[1]-1)]
    for coord in coords_to_check:
        if value_map.__contains__(coord):
            value += value_map[coord]
    return value


def find_next_position(coordinate, value_map, index):
    x = coordinate[0]
    y = coordinate[1]
    if x == 0 and y == 0:
        return 1, 0
    has_above_neighbor = value_map.__contains__((x, y+1))
    has_below_neighbor = value_map.__contains__((x, y-1))
    has_right_neighbor = value_map.__contains__((x+1, y))
    has_left_neighbor = value_map.__contains__((x-1, y))
    if has_left_neighbor and not has_above_neighbor:
        return x, y+1
    if has_above_neighbor and not has_right_neighbor:
        return x+1, y
    if has_below_neighbor and not has_left_neighbor:
        return x-1, y
    return x, y-1


while current_value < 347991:
    memory_index += 1
    position = find_next_position(position, memory_map, memory_index)
    current_value = find_value(position, memory_map)
    memory_map[position] = current_value
print(current_value)
