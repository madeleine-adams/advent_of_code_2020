file = open('bathroomSecurity_input.txt', 'r')
lines_read = file.readlines()

position = (1, 1)


def digit_for_position(coordinate):
    digit = coordinate[0] + 1
    digit += (2-coordinate[1]) * 3
    return digit


for line in lines_read:
    for char in line:
        if char == "R" and position[0] < 2:
            position = (position[0]+ 1, position[1])
        elif char == "L" and position[0] > 0:
            position = (position[0]-1, position[1])
        elif char == "U" and position[1] < 2:
            position = (position[0], position[1] + 1)
        elif char == "D" and position[1] > 0:
            position = (position[0], position[1]-1)
    print(digit_for_position(position))

