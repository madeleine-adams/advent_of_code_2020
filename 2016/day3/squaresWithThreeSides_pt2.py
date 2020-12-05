file = open('squaresWithThreeSides_input.txt', 'r')
lines_read = file.readlines()


def is_valid_triangle(lengths):
    if lengths[0] >= lengths[1] and lengths[0] >= lengths[2]:
        if lengths[1] + lengths[2] > lengths[0]:
            return True
    elif lengths[1] >= lengths[0] and lengths[1] >= lengths[2]:
        if lengths[0] + lengths[2] > lengths[1]:
            return True
    elif lengths[2] >= lengths[0] and lengths[2] >= lengths[1]:
        if lengths[0] + lengths[1] > lengths[2]:
            return True


good_triangles = 0
triangle_a = []
triangle_b = []
triangle_c = []

for line in lines_read:
    dimensions_str = line.split()
    dimensions = [int(dimensions_str[0]), int(dimensions_str[1]), int(dimensions_str[2])]
    triangle_a.append(dimensions[0])
    triangle_b.append(dimensions[1])
    triangle_c.append(dimensions[2])

    if len(triangle_a) == 3:
        if is_valid_triangle(triangle_a):
            good_triangles += 1
        if is_valid_triangle(triangle_b):
            good_triangles += 1
        if is_valid_triangle(triangle_c):
            good_triangles += 1
        triangle_a = []
        triangle_b = []
        triangle_c = []


print(good_triangles)
