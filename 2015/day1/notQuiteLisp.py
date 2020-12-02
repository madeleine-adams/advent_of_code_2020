file = open('notQuiteLisp_input.txt', 'r')

floor = 0

while True:
    character = file.read(1)
    if not character:
        break
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1

print(floor)
