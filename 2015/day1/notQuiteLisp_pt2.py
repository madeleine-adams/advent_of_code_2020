file = open('notQuiteLisp_input.txt', 'r')

floor = 0
has_entered_basement = False
index = 0

while True:
    character = file.read(1)
    index += 1
    if not character:
        break
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1
    if floor < 0 and not has_entered_basement:
        print(index)
        has_entered_basement = True

print(floor)
