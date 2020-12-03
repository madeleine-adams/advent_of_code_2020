file = open('bathroomSecurity_input.txt', 'r')
lines_read = file.readlines()

position = (0, 2)


def digit_for_position(coordinate):
    digit = coordinate[0] + 1
    digit += (2-coordinate[1]) * 3
    return digit

def is_edge(direction, coordinate):
    if direction == "R":

    elif direction == "L":

    elif direction == "U":

    else:


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
