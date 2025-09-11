DIR_TO_LEFT = {
    "R": "U",
    "U": "L",
    "L": "D",
    "D": "R",
}

DIR_TO_UNIT_VECTOR = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1),
}


def move(x: int, y: int, direction: str) -> tuple[int, int]:
    dx, dy = DIR_TO_UNIT_VECTOR[direction]
    return x + dx, y + dy


def get_neighbour_sum(x: int, y: int, coords_to_num: dict[tuple[int, int], int]) -> int:
    total = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue

            total += coords_to_num.get((x + dx, y + dy), 0)

    return total


def run(s: str) -> int:
    n = int(s.strip())

    coords_to_num = {(0, 0): 1, (1, 0): 1}
    x = 1
    y = 0
    direction = "R"

    while True:
        # if square on left is free, go there, otherwise go straight
        left_dir = DIR_TO_LEFT[direction]
        left_x, left_y = move(x, y, left_dir)
        sq_on_left_is_free = (left_x, left_y) not in coords_to_num
        if sq_on_left_is_free:
            direction = left_dir

        # move to the new square
        x, y = move(x, y, direction)
        neighbour_sum = get_neighbour_sum(x, y, coords_to_num)
        coords_to_num[(x, y)] = neighbour_sum

        if neighbour_sum > n:
            return neighbour_sum
