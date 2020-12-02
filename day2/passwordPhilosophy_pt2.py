file1 = open('passwordPhilosophy_input.txt', 'r')
lines_read = file1.readlines()
old_valid_count = 0
new_valid_count = 0


def is_valid_old(letter_rule, test_password):
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


def is_valid_new(letter_rule, test_password):
    my_tuple = letter_rule.split(" ")
    positions_str = my_tuple[0]
    letter = my_tuple[1]
    positions = positions_str.split("-")
    position_a = int(positions[0])-1
    position_b = int(positions[1])-1
    letter_count = 0
    if test_password[position_a] == letter:
        letter_count += 1
    if test_password[position_b] == letter:
        letter_count += 1
    return letter_count == 1


for i in range(len(lines_read)):
    line = lines_read[i]
    a_tuple = line.split(": ")
    rule = a_tuple[0]
    password = a_tuple[1]
    if is_valid_old(rule, password):
        old_valid_count += 1
    if is_valid_new(rule, password):
        new_valid_count += 1

print(old_valid_count)
print(new_valid_count)