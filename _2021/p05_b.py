from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    coords_to_num_lines = defaultdict(int)

    for line in lines:
        start_str, end_str = line.split(" -> ")

        x1, y1 = [int(x) for x in start_str.split(",")]
        x2, y2 = [int(x) for x in end_str.split(",")]

        dx = get_delta(x1, x2)
        dy = get_delta(y1, y2)

        x = x1
        y = y1

        while True:
            coords_to_num_lines[(x, y)] += 1

            if (x, y) == (x2, y2):
                break

            x += dx
            y += dy

    return sum(1 for c in coords_to_num_lines.values() if c > 1)


def get_delta(a: int, b: int) -> int:
    if a < b:
        return 1

    if a > b:
        return -1

    return 0
