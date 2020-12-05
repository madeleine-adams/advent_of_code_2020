file = open('securityThroughObscurity_input.txt', 'r')
rooms = file.readlines()

ascii_lowercase_start = ord('a')

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


def decrypt_room(ciphertext, shift):
    shift = shift % 26
    plaintext = ''
    for letter in ciphertext:
        if letter == "-":
            plaintext += " "
            continue
        ascii_num = ord(letter)
        alphabet_index = ascii_num - ascii_lowercase_start
        plain_index = (alphabet_index + shift) % 26
        plaintext += chr(plain_index + ascii_lowercase_start)
    return plaintext


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
        room_name = decrypt_room(room_code, int(sector_id))
        if room_name.__contains__('north'):
            print(room_name)
            print(sector_id)
