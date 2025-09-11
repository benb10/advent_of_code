from itertools import pairwise


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]

    total = 0

    for a, b in pairwise(nums):
        if b > a:
            total += 1

    return total
