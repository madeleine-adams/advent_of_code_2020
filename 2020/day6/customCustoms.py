file = open('customCustoms_input.txt', 'r')
batch = file.readlines()

current_form = ''
forms = list()
running_total = 0

# build list of customs forms
for line in batch:
    line = line.strip()
    if len(line) == 0:
        if len(current_form) > 0:
            forms.append(current_form)
            current_form = list()
        continue
    current_form += line

for form in forms:
    answers = set()
    for letter in form:
        answers.add(letter)
    running_total += len(answers)
print(running_total)
