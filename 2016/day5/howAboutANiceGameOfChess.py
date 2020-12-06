import hashlib

hash_input = "ffykfhsq"

found_hash = False
number = 0
numbers_left = 8

while numbers_left > 0:
    hash_attempt = (hash_input + str(number)).encode("utf8")
    hash_result = hashlib.md5(hash_attempt).hexdigest()
    if hash_result[0:5] == "00000":
        print(hash_result[5])
        numbers_left -= 1
    number += 1
