file = open('inverseCaptcha_input.txt', 'r')
captcha = file.readline().strip()

running_total = 0
length = len(captcha)

for i in range(length):
    first_char = captcha[i]

    second_index = int((i + length/2) % length)
    second_char = captcha[second_index]

    if first_char == second_char:
        running_total += int(first_char)
print(running_total)
