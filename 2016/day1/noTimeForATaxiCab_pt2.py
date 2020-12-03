file = open('noTimeForATaxiCab_input.txt', 'r')
lines_read = file.readlines()

instructions = lines_read[0]

steps = instructions.split(", ")

x_blocks = 0
y_blocks = 0
position = (0, 0)
positions = set()
positions.add(position)

found_bunny_hq = False

# together, is_on_y_axis and is_facing_forward give you the cardinal direction you are facing
# North: is_on_y_axis = True, is_facing_forward = True
# South: True, False
# East: False, True
# West: False, False
is_on_y_axis = True
is_facing_forward = True

for step in steps:
    direction = step[0]
    blocks = int(step[1:])

    is_right_turn = direction == "R"
    is_now_facing_forward = (is_on_y_axis == is_right_turn)
    if is_facing_forward:
        is_facing_forward = is_now_facing_forward
    else:
        is_facing_forward = not is_now_facing_forward
    # turning always switches which axis you are on
    is_on_y_axis = not is_on_y_axis



    positions_traversed = list()

    if is_on_y_axis:
        for i in range(1, blocks):
            addend = i
            if not is_facing_forward:
                addend = -i
            positions_traversed.append((x_blocks, y_blocks + addend))
        if not is_facing_forward:
            blocks = -blocks
        y_blocks += blocks
    else:
        for i in range(1, blocks):
            addend = i
            if not is_facing_forward:
                addend = -i
            positions_traversed.append((x_blocks + addend, y_blocks))
        if not is_facing_forward:
            blocks = -blocks
        x_blocks += blocks

    positions_traversed.append((x_blocks, y_blocks))
    for position in positions_traversed:
        if not found_bunny_hq and position in positions:
            print(abs(position[0]) + abs(position[1]))
            found_bunny_hq = True
            break
        else:
            positions.add(position)

print(abs(x_blocks) + abs(y_blocks))