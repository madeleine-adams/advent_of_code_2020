file = open('perfectlySphericalHousesInAVacuum_input.txt', 'r')
instructions = file.readline()

houses_visited = set()
santa_position = (0, 0)
robo_santa_position = (0, 0)
houses_visited.add(santa_position)

for i in range(len(instructions)):
    direction = instructions[i]
    is_santa = False
    if i % 2 == 0:
        position = robo_santa_position
    else:
        is_santa = True
        position = santa_position
    if direction == "^":
        position = (position[0], position[1] + 1)
    elif direction == ">":
        position = (position[0] + 1, position[1])
    elif direction == "v":
        position = (position[0], position[1] - 1)
    elif direction == "<":
        position = (position[0] - 1, position[1])
    if is_santa:
        santa_position = position
    else:
        robo_santa_position = position
    houses_visited.add(position)

print(len(houses_visited))
