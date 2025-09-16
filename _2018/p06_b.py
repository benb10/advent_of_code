from math import floor
from statistics import mean


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    points = [tuple(int(x) for x in line.split(", ")) for line in lines]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    x_mean = floor(mean(xs))
    y_mean = floor(mean(ys))

    max_distance = 10_000
    points_in_region = set()

    n = 0

    while True:
        square_size = 2 * n + 1
        x_min = x_mean - n
        x_max = x_min + square_size
        y_min = y_mean - n
        y_max = y_min + square_size

        border_points = [
            *((x_min, y) for y in range(y_min, y_max)),
            *((x_max - 1, y) for y in range(y_min, y_max)),
            *((x, y_min) for x in range(x_min, x_max)),
            *((x, y_max - 1) for x in range(x_min, x_max)),
        ]

        new_points_to_add = [
            (x, y) for x, y in border_points if get_sum_of_all_distances((x, y), points) < max_distance
        ]
        if not new_points_to_add:
            break

        points_in_region.update(new_points_to_add)

        n += 1

    return len(points_in_region)


def get_sum_of_all_distances(point: tuple[int, int], other_points: list[tuple[int, int]]) -> int:
    x, y = point
    total = 0

    for other_point in other_points:
        x1, y1 = other_point
        total += abs(x - x1) + abs(y - y1)

    return total
