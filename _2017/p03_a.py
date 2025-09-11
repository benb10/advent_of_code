from math import ceil, sqrt


def run(s: str) -> int:
    n = int(s.strip())

    if n == 1:
        return 0

    x = ceil(sqrt(n))
    edge_size = x + 1 if x % 2 == 0 else x
    previous_sq = (edge_size - 2) ** 2
    start_of_lap_n = previous_sq + 1

    rem = n - start_of_lap_n
    side_index = rem // (edge_size - 1)
    side_rem = rem % (edge_size - 1)

    dist_from_middle = edge_size // 2

    if side_index == 0:
        dx = 0
        dy = 1
        side_start_x = dist_from_middle
        side_start_y = -dist_from_middle + 1
    elif side_index == 1:
        dx = -1
        dy = 0
        side_start_x = dist_from_middle - 1
        side_start_y = dist_from_middle
    elif side_index == 2:
        dx = 0
        dy = -1
        side_start_x = -dist_from_middle
        side_start_y = dist_from_middle - 1
    elif side_index == 3:
        dx = 1
        dy = 0
        side_start_x = -dist_from_middle + 1
        side_start_y = -dist_from_middle
    else:
        raise ValueError(side_index)

    x = side_start_x + side_rem * dx
    y = side_start_y + side_rem * dy

    return abs(x) + abs(y)
