def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0

    for line in lines:
        side_lengths = [int(x) for x in line.split(" ") if x]
        side_lengths.sort()
        *other_sides, longest_side = side_lengths
        is_valid = sum(other_sides) > longest_side
        if is_valid:
            total += 1

    return total
