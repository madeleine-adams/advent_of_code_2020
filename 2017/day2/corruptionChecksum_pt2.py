file = open('corruptionChecksum_input.txt', 'r')
spreadsheet = file.readlines()


def find_whole_quotient(values):
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            cell_a = int(values[i])
            cell_b = int(values[j])
            if cell_a / cell_b % 1 == 0:
                return cell_a / cell_b
            elif cell_b / cell_a % 1 == 0:
                return cell_b / cell_a


running_total = 0

for line in spreadsheet:
    cells = line.split()
    running_total += find_whole_quotient(cells)
print(running_total)
