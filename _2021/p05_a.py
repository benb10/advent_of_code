from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    coords_to_num_lines = defaultdict(int)

    for line in lines:
        start_str, end_str = line.split(" -> ")

        x1, y1 = [int(x) for x in start_str.split(",")]
        x2, y2 = [int(x) for x in end_str.split(",")]

        is_horizontal = y1 == y2
        is_vertical = x1 == x2

        if is_horizontal:
            x_min, x_max = sorted([x1, x2])
            for x in range(x_min, x_max + 1):
                coords_to_num_lines[(x, y1)] += 1

        elif is_vertical:
            y_min, y_max = sorted([y1, y2])
            for y in range(y_min, y_max + 1):
                coords_to_num_lines[(x1, y)] += 1

    return sum(1 for c in coords_to_num_lines.values() if c > 1)
