def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    num_valid = 0

    for line in lines:
        start, middle, password = line.split(" ")

        min_count_str, max_count_str = start.split("-")
        min_count = int(min_count_str)
        max_count = int(max_count_str)

        char = middle.replace(":", "")

        char_count = sum(1 for c in password if c == char)
        is_valid = min_count <= char_count <= max_count

        if is_valid:
            num_valid += 1

    return num_valid
