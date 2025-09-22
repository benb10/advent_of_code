from copy import deepcopy

from .common import run_intcode


def run(s: str) -> int | None:
    nums = [int(x) for x in s.strip().split(",")]

    for noun in range(100):
        for verb in range(100):
            new_nums = deepcopy(nums)
            new_nums[1] = noun
            new_nums[2] = verb

            output = run_intcode(new_nums)

            if output.nums[0] == 19690720:
                return 100 * noun + verb

    return None
