def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0
    for line in lines:
        nums = line.split("x")
        nums = [int(x) for x in nums]
        length, width, height = nums
        side_areas = [length * width, width * height, height * length]
        paper = 2 * sum(side_areas) + min(side_areas)
        total += paper
    return total
