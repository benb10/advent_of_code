def get_coords(line: str) -> list[tuple[int, int]]:
    movements = line.split(",")

    coords = [(0, 0)]
    x = 0
    y = 0

    for movement in movements:
        direction = movement[0]
        distance = int(movement[1:])
        dx, dy = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }[direction]
        for i in range(distance):
            x += dx
            y += dy
            coords.append((x, y))

    return coords


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    line_1, line_2 = lines

    coords_1 = get_coords(line_1)
    coords_2 = get_coords(line_2)

    intersections = set(coords_1) & set(coords_2)
    intersections -= {(0, 0)}

    closest_intersection = min(intersections, key=lambda x: abs(x[0]) + abs(x[1]))

    return abs(closest_intersection[0]) + abs(closest_intersection[1])
