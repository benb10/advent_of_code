def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    in_code_total = 0
    in_memory_total = 0

    for line in lines:
        in_code_total += len(line)
        in_memory_total += get_num_in_memory_chars(line)

    return in_code_total - in_memory_total


HEX_DIGITS = set("0123456789abcdef")


def get_num_in_memory_chars(line: str) -> str:
    assert line[0] == line[-1] == '"'
    inner = line[1:-1]

    i = 0
    num_chars = 0

    while i < len(inner):
        if inner[i : i + 2] in ["\\\\", '\\"']:
            num_chars += 1
            i += 2
            continue

        is_hex_char = (
            inner[i] == "\\"
            and len(inner[i : i + 4]) == 4
            and inner[i + 1] == "x"
            and inner[i + 2] in HEX_DIGITS
            and inner[i + 3] in HEX_DIGITS
        )
        if is_hex_char:
            num_chars += 1
            i += 4
            continue

        # if we get here, it must be a regular char
        num_chars += 1
        i += 1

    return num_chars
