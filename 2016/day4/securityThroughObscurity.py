file = open('securityThroughObscurity_input.txt', 'r')
rooms = file.readlines()


def sort_most_used_letters(frequencies, max_length):
    frequencies['-'] = 0
    frequent_letters = ''
    for i in range(max_length):
        most_frequent = '-'
        for key in frequencies:
            if frequencies[key] > frequencies[most_frequent]:
                most_frequent = key
            elif frequencies[key] == frequencies[most_frequent] and key < most_frequent:
                most_frequent = key
        frequent_letters += most_frequent
        frequencies.pop(most_frequent, None)
    return frequent_letters


def find_checksum(test_string):
    letter_dict = dict()
    for letter in room_code:
        if letter == '-':
            continue
        if not letter.islower():
            return ''
        if letter_dict.__contains__(letter):
            count = letter_dict[letter]
            letter_dict[letter] = count + 1
        else:
            letter_dict[letter] = 1
    return sort_most_used_letters(letter_dict, 5)


real_rooms = 0

for room in rooms:
    parts = room.rsplit('-', 1)
    room_code = parts[0]

    other = parts[1]
    metadata = other.split('[')

    sector_id = metadata[0]
    checksum = metadata[1]
    # get rid of trailing ']'
    checksum = checksum[:len(checksum)-2]

    my_checksum = find_checksum(room_code)
    if my_checksum == checksum:
        real_rooms += int(sector_id)

print(real_rooms)
