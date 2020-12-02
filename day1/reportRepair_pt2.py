file1 = open('reportRepair_input.txt', 'r')
lines_read = file1.readlines()


def calculate_answer(lines, expected_sum, addend_count, start_index=0):
    for i in range(start_index, len(lines)):
        number = int(lines[i])
        if number > expected_sum:
            continue
        elif number == expected_sum and addend_count == 1:
            return number
        if addend_count > 2:
            if i+1 > len(lines):
                continue
            partial_product = calculate_answer(lines, expected_sum-number, addend_count-1, i+1)
            if partial_product == -1:
                continue
            print(number*partial_product)
        else:
            for j in range(i+1, len(lines)):
                second_number = int(lines[j])
                if number + second_number == expected_sum:
                    if start_index == 0:
                        print(number * second_number)
                    return number * second_number
    return -1


calculate_answer(lines_read, 2020, 2)
calculate_answer(lines_read, 2020, 3)
