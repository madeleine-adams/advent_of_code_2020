file = open('iWasToldThereWouldBeNoMath_input.txt', 'r')
lines_read = file.readlines()

total = 0

for line in lines_read:
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    top = length * width
    side = length * height
    front = width * height

    total += 2*top + 2*side + 2*front

    if top <= side and top <= front:
        total += top
    elif side <= top and side <= front:
        total += side
    else:
        total += front


print(total)
