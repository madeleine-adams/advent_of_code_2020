import hashlib
import random
import os


def animate(output):
    animation_text = ''
    for letter in output:
        if letter == '_':
            rand_int = random.randint(33, 126)
            animation_text += chr(rand_int)
        else:
            animation_text += letter
    os.system('clear')
    print(animation_text)


hash_input = "ffykfhsq"

found_hash = False
number = 0
password = '________'

while password.__contains__('_'):
    if number % 50000 == 0:
        animate(password)
    hash_attempt = (hash_input + str(number)).encode("utf8")
    hash_result = hashlib.md5(hash_attempt).hexdigest()
    if hash_result[0:5] == "00000":
        possible_index = hash_result[5]
        if not possible_index.isdigit() or not (0 <= int(possible_index) <= 7):
            number += 1
            continue
        index = int(possible_index)
        if password[index] != '_':
            number += 1
            continue
        password = password[:index] + hash_result[6] + password[index+1:]
        animate(password)
    number += 1
