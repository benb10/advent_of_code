def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    in_code_total = 0
    encoded_total = 0

    for line in lines:
        in_code_total += len(line)
        encoded_total += get_encoded_length(line)

    return encoded_total - in_code_total


def get_encoded_length(s: str) -> int:
    num_chars = 0

    for char in s:
        if char == '"':
            num_chars += 2
        elif char == "\\":
            num_chars += 2
        else:
            num_chars += 1

    return num_chars + 2  # +2 for the start and end quote
