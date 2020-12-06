file = open('signalsAndNoise_input.txt', 'r')
lines_read = file.readlines()

message_length = len(lines_read[0].strip())

letter_frequencies = [None] * message_length
for index in range(message_length):
    letter_frequencies[index] = dict()

for line in lines_read:
    line = line.strip()
    for i in range(len(line)):
        frequency_dict = letter_frequencies[i]
        letter = line[i]
        if frequency_dict.__contains__(letter):
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1

for i in range(message_length):
    frequency_dict = letter_frequencies[i]
    min_letter = ''
    min_freq = 999999999
    for key in frequency_dict:
        if frequency_dict[key] < min_freq:
            min_letter = key
            min_freq = frequency_dict[key]
    print(min_letter)
