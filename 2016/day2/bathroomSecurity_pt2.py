file = open('bathroomSecurity_input.txt', 'r')
lines_read = file.readlines()

position = (0, 2)


def digit_for_position(coordinate):
    if coordinate[1] == 4:
        return "1"
    elif coordinate[1] == 3:
        return str(coordinate[0] + 1)
    elif coordinate[1] == 2:
        return str(coordinate[0] + 5)
    elif coordinate[1] == 1:
        if coordinate[0] == 1:
            return "A"
        elif coordinate[0] == 2:
            return "B"
        else:
            return "C"
    else:
        return "D"
    return digit


def is_edge(direction, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if direction == "R":
        if y == (x - 2) or y == (6 - x):
            return True
    elif direction == "L":
        if y == (x + 2) or y == (2 - x):
            return True
    elif direction == "U":
        if y == (x + 2) or y == (6 - x):
            return True
    else:
        if y == (x - 2) or y == (2 - x):
            return True
    return False


for line in lines_read:
    for char in line:
        if is_edge(char, position):
            continue
        if char == "R":
            position = (position[0] + 1, position[1])
        elif char == "L":
            position = (position[0]-1, position[1])
        elif char == "U":
            position = (position[0], position[1] + 1)
        elif char == "D":
            position = (position[0], position[1]-1)
    print(digit_for_position(position))
