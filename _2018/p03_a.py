from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    coords_to_rect_count: dict[tuple[int, int], int] = defaultdict(int)

    for line in lines:
        _a, _b, c, d = line.split(" ")
        distances_str = c.replace(":", "")
        left_dist, top_dist = [int(x) for x in distances_str.split(",")]
        width, height = [int(x) for x in d.split("x")]

        for dr in range(height):
            for dc in range(width):
                r = top_dist + dr
                c = left_dist + dc
                coords_to_rect_count[(r, c)] += 1

    num_overlapping_coords = sum(1 for v in coords_to_rect_count.values() if v > 1)

    return num_overlapping_coords
