file = open('tobogganTrajectory_input.txt', 'r')
forest = file.readlines()

slope_y = 1
slope_x = 3
trees_hit = 0

for y in range(slope_y, len(forest), slope_y):
    tree_row = forest[y].strip()
    x = y / (slope_y/slope_x)
    tree_index = int(x % (len(tree_row)))
    if tree_row[tree_index] == "#":
        trees_hit += 1

print(trees_hit)
