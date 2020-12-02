file = open('iWasToldThereWouldBeNoMath_input.txt', 'r')
lines_read = file.readlines()

total_paper = 0
total_ribbon = 0

for line in lines_read:
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    total_ribbon += length * width * height

    top = length * width
    side = length * height
    front = width * height

    total_paper += 2*top + 2*side + 2*front

    if top <= side and top <= front:
        total_paper += top
        total_ribbon += 2*length + 2*width
    elif side <= top and side <= front:
        total_paper += side
        total_ribbon += 2*length + 2*height
    else:
        total_paper += front
        total_ribbon += 2*width + 2*height


print(total_paper)
print(total_ribbon)
