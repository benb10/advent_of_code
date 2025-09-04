from itertools import pairwise
from typing import Iterator


def check_num_is_valid(num: int) -> bool:
    num_str = str(num)

    if len(num_str) != 6:
        return False

    digits = [int(c) for c in num_str]

    always_increasing = True
    has_a_double = False

    for a, b in pairwise(digits):
        if a > b:
            always_increasing = False
            break

        if a == b:
            has_a_double = True

    return always_increasing and has_a_double


def iter_nums_to_check(lower_limit: int, upper_limit: int) -> Iterator[int]:
    num = lower_limit

    while True:
        if num > upper_limit:
            return

        digits = [int(c) for c in str(num)]
        decreasing_i = next((i for i, (a, b) in enumerate(pairwise(digits)) if a > b), None)
        if decreasing_i is None:
            yield num
            num += 1
        else:
            power = len(str(num)) - decreasing_i - 2
            diff = digits[decreasing_i] - digits[decreasing_i + 1]
            num += diff * 10**power


def run(s: str) -> int:
    lower_limit, upper_limit = [int(x) for x in s.strip().split("-")]

    total = 0

    for num in iter_nums_to_check(lower_limit, upper_limit):
        num_is_valid = check_num_is_valid(num)
        if num_is_valid:
            total += 1

    return total
