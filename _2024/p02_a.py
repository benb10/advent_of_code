from itertools import pairwise


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    reports = [[int(x) for x in line.split(" ")] for line in lines]

    num_safe = 0
    for report in reports:
        diffs = [num_1 - num_2 for num_1, num_2 in pairwise(report)]
        all_increasing = all(1 <= diff <= 3 for diff in diffs)
        all_decreasing = all(-3 <= diff <= -1 for diff in diffs)
        is_safe = all_increasing or all_decreasing
        if is_safe:
            num_safe += 1

    return num_safe
