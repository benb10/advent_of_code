def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0
    digit_names_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in lines:
        index_to_num = {}

        for i, char in enumerate(line):
            if char.isdigit():
                index_to_num[i] = int(char)
            else:
                for digit_name, num in digit_names_to_int.items():
                    if line[i : i + len(digit_name)] == digit_name:
                        index_to_num[i] = num

        _, first_digit = min(index_to_num.items(), key=lambda t: t[0])
        _, last_digit = max(index_to_num.items(), key=lambda t: t[0])
        num = int(str(first_digit) + str(last_digit))
        total += num

    return total
