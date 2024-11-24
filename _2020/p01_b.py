from itertools import combinations


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]

    for x, y, z in combinations(nums, 3):
        if x + y + z == 2020:
            return x * y * z
