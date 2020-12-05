import hashlib

hash_input = "bgvyzdsv"

found_hash = False
number = 0

while not found_hash:
    hash_attempt = (hash_input + str(number)).encode("utf8")
    hash_result = hashlib.md5(hash_attempt).hexdigest()
    if hash_result[0:5] == "00000":
        print(number)
        found_hash = True
    number += 1
