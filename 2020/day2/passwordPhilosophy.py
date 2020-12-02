file1 = open('passwordPhilosophy_input.txt', 'r')
lines_read = file1.readlines()
valid_count = 0


def is_valid(letter_rule, test_password):
    my_tuple = letter_rule.split(" ")
    total_range = my_tuple[0]
    letter = my_tuple[1]
    min_max = total_range.split("-")
    minimum = int(min_max[0])
    maximum = int(min_max[1])
    letter_count = 0
    for character in test_password:
        if character == letter:
            letter_count += 1
    if minimum <= letter_count <= maximum:
        return True
    return False


for i in range(len(lines_read)):
    line = lines_read[i]
    a_tuple = line.split(": ")
    rule = a_tuple[0]
    password = a_tuple[1]
    if is_valid(rule, password):
        valid_count += 1

print(valid_count)