def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        range_1, range_2 = line.split(",")
        a, b = [int(x) for x in range_1.split("-")]
        c, d = [int(x) for x in range_2.split("-")]

        range_1_contains_2 = a <= c and d <= b
        range_2_contains_1 = c <= a and b <= d
        one_contains_another = range_1_contains_2 or range_2_contains_1
        if one_contains_another:
            total += 1

    return total
