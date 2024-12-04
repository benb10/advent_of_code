from itertools import pairwise


def check_is_safe_no_tolerance(report: list[int]) -> bool:
    diffs = [num_1 - num_2 for num_1, num_2 in pairwise(report)]
    all_increasing = all(1 <= diff <= 3 for diff in diffs)
    all_decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return all_increasing or all_decreasing


def check_is_safe_with_tolerance(report: list[int]) -> bool:
    if check_is_safe_no_tolerance(report):
        return True

    for i in range(len(report)):
        shortened_report = [x for j, x in enumerate(report) if i != j]
        if check_is_safe_no_tolerance(shortened_report):
            return True

    return False


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    reports = [[int(x) for x in line.split(" ")] for line in lines]

    num_safe = 0
    for report in reports:
        is_safe = check_is_safe_with_tolerance(report)
        if is_safe:
            num_safe += 1

    return num_safe
