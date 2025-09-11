def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    passports = []
    last_line = ""

    for line in lines:
        if line:
            if last_line:
                passports[-1] += " " + line
            else:
                passports.append(line)

        last_line = line

    valid_count = 0

    for passport in passports:
        is_valid = passport_is_valid(passport)
        if is_valid:
            valid_count += 1

    return valid_count


REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

ALLOWED_COLOUR_CHARS = set("0123456789abcdef")
ALLOWED_EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def passport_is_valid(passport: str) -> bool:
    field_names = set()
    sections = passport.replace("\n", " ").split(" ")
    field_data = {}

    for section in sections:
        field_name, value = section.split(":")
        field_names.add(field_name)
        field_data[field_name] = value

    missing_fields = REQUIRED_FIELDS - field_names
    if missing_fields:
        return False

    byr = field_data["byr"]
    valid_byr = byr.isdigit() and 1920 <= int(byr) <= 2002
    if not valid_byr:
        return False

    iyr = field_data["iyr"]
    valid_iyr = iyr.isdigit() and 2010 <= int(iyr) <= 2020
    if not valid_iyr:
        return False

    eyr = field_data["eyr"]
    valid_eyr = eyr.isdigit() and 2020 <= int(eyr) <= 2030
    if not valid_eyr:
        return False

    hgt = field_data["hgt"]

    height_str = hgt[:-2]
    height_units = hgt[-2:]
    if not height_str.isdigit():
        return False

    height = int(height_str)
    height_valid = height_units == "cm" and (150 <= height <= 193) or height_units == "in" and (59 <= height <= 76)
    if not height_valid:
        return False

    hcl = field_data["hcl"]
    hcl_valid = hcl[0] == "#" and all(c in ALLOWED_COLOUR_CHARS for c in hcl[1:])
    if not hcl_valid:
        return False

    ecl = field_data["ecl"]
    ecl_valid = ecl in ALLOWED_EYE_COLOURS
    if not ecl_valid:
        return False

    pid = field_data["pid"]
    pid_valid = len(pid) == 9 and pid.isdigit()
    if not pid_valid:
        return False

    return True
