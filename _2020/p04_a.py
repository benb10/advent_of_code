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

    required_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    }

    valid_count = 0

    for passport in passports:
        field_names = set()
        sections = passport.replace("\n", " ").split(" ")

        for section in sections:
            field_name, _value = section.split(":")
            field_names.add(field_name)

        missing_fields = required_fields - field_names
        if not missing_fields:
            valid_count += 1

    return valid_count
