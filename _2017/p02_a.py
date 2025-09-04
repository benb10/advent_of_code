def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        line = line.replace("\t", " ")
        nums = [int(x) for x in line.split(" ")]
        checksum = max(nums) - min(nums)
        total += checksum

    return total
