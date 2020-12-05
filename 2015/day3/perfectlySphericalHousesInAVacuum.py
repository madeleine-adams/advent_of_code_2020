file = open('perfectlySphericalHousesInAVacuum_input.txt', 'r')
instructions = file.readline()

houses_visited = set()
position = (0, 0)
houses_visited.add(position)

for direction in instructions:
    if direction == "^":
        position = (position[0], position[1] + 1)
    elif direction == ">":
        position = (position[0] + 1, position[1])
    elif direction == "v":
        position = (position[0], position[1] - 1)
    elif direction == "<":
        position = (position[0] - 1, position[1])
    houses_visited.add(position)

print(len(houses_visited))
