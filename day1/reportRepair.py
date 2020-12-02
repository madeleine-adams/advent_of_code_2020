file1 = open('reportRepair_input.txt', 'r')
lines_read = file1.readlines()


def calculate_answer(lines):
    for i in range(len(lines)):
        number = int(lines[i])
        if number >= 2020:
            continue
        for j in range(i, len(lines)):
            second_number = int(lines[j])
            if number + second_number == 2020:
                print(number * second_number)
                return


calculate_answer(lines_read)
