file = open('highEntropyPassphrases_input.txt', 'r')
passphrases = file.readlines()


def is_valid_passphrase(split_phrase):
    for i in range(len(split_phrase)):
        word_a = split_phrase[i]
        for j in range(i+1, len(split_phrase)):
            word_b = split_phrase[j]
            if word_a == word_b:
                return False
    return True


valid_count = 0
for passphrase in passphrases:
    words = passphrase.split()
    if is_valid_passphrase(words):
        valid_count += 1

print(valid_count)