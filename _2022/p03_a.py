def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96

    return ord(char) - 38


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0

    for line in lines:
        comp_1 = line[: len(line) // 2]
        comp_2 = line[len(line) // 2 :]
        in_common = set(comp_1) & set(comp_2)
        assert len(in_common) == 1
        char = list(in_common)[0]
        priority = get_priority(char)
        total += priority

    return total
