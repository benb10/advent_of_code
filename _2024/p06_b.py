from copy import deepcopy


def get_guard_position(rows: list[str]) -> tuple[int, int]:
    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char == "^":
                return r, c
    raise ValueError("Could not found guard")


def turn_right(direction: str) -> str:
    return {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N",
    }[direction]


def get_next_step(r: int, c: int, direction: str) -> tuple[int, int]:
    if direction == "N":
        return r - 1, c
    if direction == "E":
        return r, c + 1
    if direction == "S":
        return r + 1, c
    if direction == "W":
        return r, c - 1
    raise ValueError(f"Unknown direction {direction}")


def check_is_on_grid(r: int, c: int, rows: list[str]) -> bool:
    num_rows = len(rows)
    num_columns = len(rows[0])
    return (0 <= r < num_rows) and (0 <= c < num_columns)


def take_step(rows: list[str], guard_r: int, guard_c: int, guard_direction: str) -> tuple[int, int, str]:
    next_r, next_c = get_next_step(guard_r, guard_c, guard_direction)
    if not check_is_on_grid(next_r, next_c, rows):
        return next_r, next_c, guard_direction
    if rows[next_r][next_c] == "#":
        # can't go forwards - just turn right
        return guard_r, guard_c, turn_right(guard_direction)
    return next_r, next_c, guard_direction


def run_simulation(
    rows: list[str], guard_r: int, guard_c: int, guard_direction: str
) -> tuple[list[tuple[int, int, str]], bool]:
    steps = [(guard_r, guard_c, guard_direction)]
    steps_set = {(guard_r, guard_c, guard_direction)}
    found_loop = False

    while True:
        guard_r, guard_c, guard_direction = take_step(rows, guard_r, guard_c, guard_direction)
        if not check_is_on_grid(guard_r, guard_c, rows):
            break

        if (guard_r, guard_c, guard_direction) in steps_set:
            found_loop = True
            break

        steps.append((guard_r, guard_c, guard_direction))
        steps_set.add((guard_r, guard_c, guard_direction))

    return steps, found_loop


def run(s: str) -> int:
    rows = [line.strip() for line in s.strip().split("\n")]

    guard_start_r, guard_start_c = get_guard_position(rows)
    guard_direction = "N"
    steps, _ = run_simulation(rows, guard_start_r, guard_start_c, guard_direction)

    positions_to_check = {(guard_r, guard_c) for guard_r, guard_c, guard_direction in steps}
    positions_to_check -= {(guard_start_r, guard_start_c)}
    total = 0

    print("AAA", len(positions_to_check))

    for obstacle_r, obstacle_c in positions_to_check:
        new_rows = deepcopy(rows)
        row_to_change = new_rows[obstacle_r]
        new_row = "".join("#" if c == obstacle_c else char for c, char in enumerate(row_to_change))
        new_rows[obstacle_r] = new_row
        steps, found_loop = run_simulation(new_rows, guard_start_r, guard_start_c, guard_direction)
        if found_loop:
            total += 1

    return total
