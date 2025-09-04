def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    num_valid = 0

    for line in lines:
        start, middle, password = line.split(" ")

        pos_1_str, pos_2_str = start.split("-")
        pos_1 = int(pos_1_str)
        pos_2 = int(pos_2_str)

        char = middle.replace(":", "")

        is_valid = (password[pos_1 - 1] == char) != (password[pos_2 - 1] == char)

        if is_valid:
            num_valid += 1

    return num_valid
