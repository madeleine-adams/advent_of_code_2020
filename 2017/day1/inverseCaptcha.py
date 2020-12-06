file = open('inverseCaptcha_input.txt', 'r')
captcha = file.readline().strip()

running_total = 0

for i in range(len(captcha)):
    first_char = captcha[i]

    if i+1 < len(captcha):
        second_char = captcha[i+1]
    else:
        second_char = captcha[0]

    if first_char == second_char:
        running_total += int(first_char)
print(running_total)
