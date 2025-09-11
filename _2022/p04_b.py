def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        range_1, range_2 = line.split(",")
        a, b = [int(x) for x in range_1.split("-")]
        c, d = [int(x) for x in range_2.split("-")]

        ranges_overlap = not b < c and not d < a
        if ranges_overlap:
            total += 1

    return total
