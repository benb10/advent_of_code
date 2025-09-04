def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]
    return sum(nums)
