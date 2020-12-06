file = open('doesntHeHaveInternElvesForThis_input.txt', 'r')
lines = file.readlines()


def has_sandwich(text):
    for i in range(1, len(text)-1):
        prev_letter = text[i - 1]
        next_letter = text[i + 1]
        if prev_letter == next_letter:
            return True
    return False


def has_repeat_pair(text):
    for i in range(len(text) - 2):
        pair_a = text[i:i+2]
        for j in range(i+2, len(text)-1):
            pair_b = text[j:j+2]
            if pair_a == pair_b:
                return True
    return False


nice_strings = 0

for line in lines:
    line = line.strip()
    if has_sandwich(line) and has_repeat_pair(line):
        nice_strings += 1

print(nice_strings)
