file = open('squaresWithThreeSides_input.txt', 'r')
lines_read = file.readlines()

good_triangles = 0

for line in lines_read:
    dimensions_str = line.split()
    dimensions = [int(dimensions_str[0]), int(dimensions_str[1]), int(dimensions_str[2])]

    if dimensions[0] >= dimensions[1] and dimensions[0] >= dimensions[2]:
        if dimensions[1] + dimensions[2] > dimensions[0]:
            good_triangles += 1
    elif dimensions[1] >= dimensions[0] and dimensions[1] >= dimensions[2]:
        if dimensions[0] + dimensions[2] > dimensions[1]:
            good_triangles += 1
    elif dimensions[2] >= dimensions[0] and dimensions[2] >= dimensions[1]:
        if dimensions[0] + dimensions[1] > dimensions[2]:
            good_triangles += 1

print(good_triangles)
