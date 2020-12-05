file = open('binaryBoarding_input.py', 'r')
tickets = file.readlines()

total_rows = 128
total_columns = 8


def find_row(boarding_pass):
    min_row = 0
    max_row = total_rows-1
    for letter in boarding_pass[:7]:
        if letter == 'F':
            max_row = max_row - int((max_row - min_row) / 2) - 1
        elif letter == 'B':
            min_row = min_row + int((max_row - min_row) / 2) + 1
    return max_row


def find_seat(boarding_pass):
    min_seat = 0
    max_seat = total_columns - 1
    for letter in boarding_pass[7:]:
        if letter == 'R':
            min_seat = min_seat + int((max_seat - min_seat) / 2) + 1
        elif letter == 'L':
            max_seat = max_seat - int((max_seat - min_seat) / 2) - 1
    return max_seat


highest_id = -1

for ticket in tickets:
    row = find_row(ticket)
    seat = find_seat(ticket)
    seat_id = row * 8 + seat
    if seat_id > highest_id:
        highest_id = seat_id

print(highest_id)
