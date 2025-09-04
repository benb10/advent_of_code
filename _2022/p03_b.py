from more_itertools import chunked


def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96

    return ord(char) - 38


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0

    for group in chunked(lines, 3):
        rs_1, rs_2, rs_3 = group
        in_common = set(rs_1) & set(rs_2) & set(rs_3)
        assert len(in_common) == 1
        char = list(in_common)[0]
        priority = get_priority(char)
        total += priority

    return total
