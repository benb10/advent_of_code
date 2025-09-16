from collections import defaultdict

# 1.2 s


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    points = [tuple(int(x) for x in line.split(", ")) for line in lines]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)

    xy_to_closest_point_index = {}

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            point_index_to_distance = {i: abs(x1 - x) + abs(y1 - y) for i, (x1, y1) in enumerate(points)}
            closest_point_index, min_distance = min(point_index_to_distance.items(), key=lambda a: a[1])
            is_a_tie = sum(1 for d in point_index_to_distance.values() if d == min_distance) > 1

            xy_to_closest_point_index[(x, y)] = None if is_a_tie else closest_point_index

    infinite_area_point_indices = set()

    border_points = [
        *((x_min, y) for y in range(y_min, y_max + 1)),
        *((x_max, y) for y in range(y_min, y_max + 1)),
        *((x, y_min) for x in range(x_min, x_max + 1)),
        *((x, y_max) for x in range(x_min, x_max + 1)),
    ]
    for x, y in border_points:
        closest_point_index = xy_to_closest_point_index[(x, y)]
        if closest_point_index is not None:
            infinite_area_point_indices.add(closest_point_index)

    point_index_to_area_size = defaultdict(int)
    for point_index in xy_to_closest_point_index.values():
        if point_index in infinite_area_point_indices:
            continue

        point_index_to_area_size[point_index] += 1

    return max(point_index_to_area_size.values())
