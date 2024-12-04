def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0
    for line in lines:
        nums = line.split("x")
        nums = [int(x) for x in nums]
        length, width, height = nums
        perimeters = [2 * (length + width), 2 * (width + height), 2 * (height + length)]
        ribbon_length = min(perimeters) + length * width * height
        total += ribbon_length
    return total
