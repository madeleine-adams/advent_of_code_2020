file = open('tobogganTrajectory_input.txt', 'r')
woods = file.readlines()


def how_many_trees_hit(forest, slope_x, slope_y):
    trees_hit = 0
    for y in range(slope_y, len(forest), slope_y):
        tree_row = forest[y].strip()
        x = y / (slope_y/slope_x)
        tree_index = int(x % (len(tree_row)))
        if tree_row[tree_index] == "#":
            trees_hit += 1

    return trees_hit


path_a = how_many_trees_hit(woods, 1, 1)
path_b = how_many_trees_hit(woods, 3, 1)
path_c = how_many_trees_hit(woods, 5, 1)
path_d = how_many_trees_hit(woods, 7, 1)
path_e = how_many_trees_hit(woods, 1, 2)

print(path_a * path_b * path_c * path_d * path_e)
