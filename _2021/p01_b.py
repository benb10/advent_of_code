from itertools import pairwise

from more_itertools import windowed


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]
    sums_of_triples = [sum(x) for x in windowed(nums, 3)]

    total = 0

    for a, b in pairwise(sums_of_triples):
        if b > a:
            total += 1

    return total
