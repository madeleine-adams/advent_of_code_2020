file = open('passportProcessing_input.txt', 'r')
batch = file.readlines()

current_passport = list()
passports = list()
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
good_passports = 0
bad_passports = 0

# build list of passports
for line in batch:
    if len(line.strip()) == 0:
        if len(current_passport) > 0:
            passports.append(current_passport)
            current_passport = list()
        continue
    current_passport.append(line)

for passport in passports:
    meets_requirements = list()
    for field in required_fields:
        meets_requirements.append(False)
    for line in passport:
        entries = line.split()
        for entry in entries:
            parts = entry.split(":")
            field_name = parts[0]
            if required_fields.__contains__(field_name):
                index = required_fields.index(field_name)
                meets_requirements[index] = True
    if not meets_requirements.__contains__(False):
        good_passports += 1

print(good_passports)
