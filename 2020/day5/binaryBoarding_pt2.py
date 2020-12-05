file = open('binaryBoarding_input.py', 'r')
tickets = file.readlines()

total_rows = 128
total_columns = 8


def find_row(boarding_pass):
    min_row = 0
    max_row = total_rows - 1
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


claimed_seats = [False] * total_columns * total_rows
empty_seats = []

for i in range(total_rows):
    for j in range(total_columns):
        empty_seats.append((i, j))

for ticket in tickets:
    row = find_row(ticket)
    seat = find_seat(ticket)
    seat_id = row * 8 + seat
    claimed_seats[seat_id] = True

for i in range(len(claimed_seats)):
    is_taken = claimed_seats[i]
    if is_taken:
        empty_seats[i] = False

for i in range(1, len(empty_seats) - 1):
    seat_before = empty_seats[i - 1]
    seat = empty_seats[i]
    seat_after = empty_seats[i + 1]
    if seat and not seat_before and not seat_after:
        row = seat[0]
        column = seat[1]
        print(row * 8 + column)
