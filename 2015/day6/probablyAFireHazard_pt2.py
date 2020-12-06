file = open('probablyAFireHazard_input.txt', 'r')
instructions = file.readlines()

light_grid = [0] * 1000
for i in range(1000):
    light_grid[i] = [0] * 1000

for instruction in instructions:
    parts = instruction.split()
    start_str = parts[2]
    end_str = parts[len(parts) - 1]
    is_toggle = False
    is_on = True
    if parts[0] == 'toggle':
        is_toggle = True
        start_str = parts[1]
    elif parts[1] == 'off':
        is_on = False
    start_coords = start_str.split(',')
    end_coords = end_str.split(',')
    start_coords[0] = int(start_coords[0])
    start_coords[1] = int(start_coords[1])
    end_coords[0] = int(end_coords[0])
    end_coords[1] = int(end_coords[1])
    for x in range(start_coords[0], end_coords[0]+1):
        for y in range(start_coords[1], end_coords[1]+1):
            if is_toggle:
                light_grid[x][y] += 2
                continue
            if is_on:
                light_grid[x][y] += 1
                continue
            if light_grid[x][y] > 0:
                light_grid[x][y] -= 1

brightness = 0
for row in range(len(light_grid)):
    for col in range(len(light_grid[row])):
        brightness += light_grid[row][col]
print(brightness)
