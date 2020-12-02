file1 = open('reportRepair_input.txt', 'r')
lines_read = file1.readlines()


def calculate_answer(lines, expected_sum, addend_count, start_index=0):
    for i in range(start_index, len(lines)):
        number = int(lines[i])
        if number > expected_sum:
            continue
        elif number == expected_sum and addend_count == 1:
            return number

        if addend_count > 1:
            partial_product = calculate_answer(lines, expected_sum-number, addend_count-1, i+1)
            if partial_product == -1:
                continue
            return number * partial_product
    return -1


print(calculate_answer(lines_read, 2020, 2))
print(calculate_answer(lines_read, 2020, 3))
