from collections import defaultdict
from itertools import pairwise

from more_itertools import windowed


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        is_nice = check_is_nice(line)
        if is_nice:
            total += 1

    return total


def check_is_nice(s: str) -> bool:
    pairs = [(i, a + b) for i, (a, b) in enumerate(pairwise(s))]
    pair_to_starting_indices = defaultdict(list)

    for i, pair in pairs:
        pair_to_starting_indices[pair].append(i)

    has_valid_pair = False

    for pair, indices in pair_to_starting_indices.items():
        if len(indices) < 2:
            continue

        min_i = min(indices)
        max_i = max(indices)
        if max_i - min_i >= 2:
            # pair is not right next to each other
            has_valid_pair = True
            break

    if not has_valid_pair:
        return False

    has_valid_tripe = False
    for a, b, c in windowed(s, 3):
        if a == c:
            has_valid_tripe = True
            break

    if not has_valid_tripe:
        return False

    return True
