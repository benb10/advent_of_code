def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]
    fuel_reqs = [n // 3 - 2 for n in nums]
    return sum(fuel_reqs)
