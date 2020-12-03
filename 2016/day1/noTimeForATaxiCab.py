file = open('noTimeForATaxiCab_input.txt', 'r')
lines_read = file.readlines()

instructions = lines_read[0]

steps = instructions.split(", ")

x_blocks = 0
y_blocks = 0
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

    if not is_facing_forward:
        blocks = -blocks

    if is_on_y_axis:
        y_blocks += blocks
    else:
        x_blocks += blocks

print(abs(x_blocks) + abs(y_blocks))