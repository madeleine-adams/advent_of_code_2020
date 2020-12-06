file = open('corruptionChecksum_input.txt', 'r')
spreadsheet = file.readlines()


def find_smallest(inputs):
    smallest = int(inputs[0])
    for value in inputs:
        number = int(value)
        if number < smallest:
            smallest = number
    return smallest


def find_largest(inputs):
    largest = int(inputs[0])
    for value in inputs:
        number = int(value)
        if number > largest:
            largest = number
    return largest


checksum = 0

for line in spreadsheet:
    cells = line.split()
    minimum = find_smallest(cells)
    maximum = find_largest(cells)
    checksum += maximum - minimum
print(checksum)
