from itertools import combinations


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]

    for x, y in combinations(nums, 2):
        if x + y == 2020:
            return x * y
