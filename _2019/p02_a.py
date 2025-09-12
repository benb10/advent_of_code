from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]
    nums[1] = 12
    nums[2] = 2

    output = run_intcode(nums)

    return output[0]
