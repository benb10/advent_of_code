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


def get_coord_to_index(coords):
    coord_to_index = {}
    for i, coord in enumerate(coords):
        if coord not in coord_to_index:
            coord_to_index[coord] = i
    return coord_to_index


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    line_1, line_2 = lines

    coords_1 = get_coords(line_1)
    coords_2 = get_coords(line_2)

    coord_to_index_1 = get_coord_to_index(coords_1)
    coord_to_index_2 = get_coord_to_index(coords_2)

    intersections = set(coords_1) & set(coords_2)
    intersections -= {(0, 0)}

    closest_intersection = min(intersections, key=lambda x: coord_to_index_1[x] + coord_to_index_2[x])

    return coord_to_index_1[closest_intersection] + coord_to_index_2[closest_intersection]
