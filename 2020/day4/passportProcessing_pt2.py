file = open('passportProcessing_input.txt', 'r')
batch = file.readlines()

current_passport = list()
passports = list()
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid_hex_letters = ["a", "b", "c", "d", "e", "f"]
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


def check_is_valid(field_name, field_value):
    if field_name == "byr":
        year = int(field_value)
        return 1920 <= year <= 2002
    elif field_name == "iyr":
        year = int(field_value)
        return 2010 <= year <= 2020
    elif field_name == "eyr":
        year = int(field_value)
        return 2020 <= year <= 2030
    elif field_name == "hgt":
        if len(field_value) <= 2:
            return False
        height = int(field_value[:len(field_value)-2])
        unit = field_value[len(field_value)-2:]
        if unit == "cm":
            return 150 <= height <= 193
        elif unit == "in":
            return 59 <= height <= 76
        else:
            return False
    elif field_name == "hcl":
        if field_value[0] != "#":
            return False
        if len(field_value) != 7:
            return False
        for i in range(1, 7):
            if field_value[i].isdigit():
                continue
            elif valid_hex_letters.__contains__(field_value[i]):
                continue
            else:
                return False
        return True
    elif field_name == "ecl":
        return valid_ecl.__contains__(field_value)
    elif field_name == "pid":
        if len(field_value) != 9:
            return False
        return field_value.isdigit()
    else:
        return False


for passport in passports:
    meets_requirements = list()
    for field in required_fields:
        meets_requirements.append(False)
    for line in passport:
        entries = line.split()
        for entry in entries:
            parts = entry.split(":")
            name = parts[0]
            value = parts[1]
            if required_fields.__contains__(name):
                is_valid = check_is_valid(name, value)
                if is_valid:
                    index = required_fields.index(name)
                    meets_requirements[index] = True
    if not meets_requirements.__contains__(False):
        good_passports += 1

print(good_passports)
