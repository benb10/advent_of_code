from itertools import pairwise


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        is_nice = check_is_nice(line)
        if is_nice:
            total += 1

    return total


def check_is_nice(s: str) -> bool:
    disallowed_sub_strings = ["ab", "cd", "pq", "xy"]
    if any(x in s for x in disallowed_sub_strings):
        return False

    vowel_count = sum(1 for c in s if c in "aeiou")
    if vowel_count < 3:
        return False

    has_a_double_letter = False
    for a, b in pairwise(s):
        if a == b:
            has_a_double_letter = True
            break

    if not has_a_double_letter:
        return False

    return True
