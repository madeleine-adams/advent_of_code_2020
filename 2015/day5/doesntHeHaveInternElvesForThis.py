file = open('doesntHeHaveInternElvesForThis_input.txt', 'r')
lines = file.readlines()

vowels = ['a', 'e', 'i', 'o', 'u']
forbidden_combos = ['ab', 'cd', 'pq', 'xy']


def has_enough_vowels(text):
    vowel_count = 0
    for letter in text:
        if vowels.__contains__(letter):
            vowel_count += 1
    return vowel_count >= 3


def has_double_letter(text):
    prev_letter = text[0]
    for letter in text[1:]:
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False


def no_forbidden_combos(text):
    prev_letter = text[0]
    for letter in text[1:]:
        combo = prev_letter + letter
        if forbidden_combos.__contains__(combo):
            return False
        prev_letter = letter
    return True


nice_strings = 0

for line in lines:
    line = line.strip()
    if has_double_letter(line) and has_enough_vowels(line)  and no_forbidden_combos(line):
        nice_strings += 1

print(nice_strings)