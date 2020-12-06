file = open('customCustoms_input.txt', 'r')
batch = file.readlines()

current_form = list()
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
    current_form.append(line)

for form in forms:
    group_total = 0
    group_size = len(form)
    answers = dict()
    for person in form:
        for letter in person:
            if answers.__contains__(letter):
                answers[letter] = answers[letter] + 1
            else:
                answers[letter] = 1
    for key in answers:
        if answers[key] == group_size:
            group_total += 1
    running_total += group_total
print(running_total)
