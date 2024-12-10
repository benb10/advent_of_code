def get_neighbours(rows: list[str], r: int, c: int) -> list[tuple[int, int]]:
    potential_neighbours = [
        (r, c + 1),
        (r + 1, c),
        (r, c - 1),
        (r - 1, c),
    ]
    num_rows = len(rows)
    num_columns = len(rows[0])
    return [(a, b) for a, b in potential_neighbours if (0 <= a < num_rows) and 0 <= b < num_columns]


def get_score(rows: list[str], r: int, c: int) -> int:
    target_nums = "123456789"
    paths = {((r, c),)}

    for target_num in target_nums:
        new_paths = set()
        for path in paths:
            curr_r, curr_c = path[-1]
            neighbours = get_neighbours(rows, curr_r, curr_c)
            next_options = [(a, b) for a, b in neighbours if rows[a][b] == target_num]
            for next_option in next_options:
                new_path = path + (next_option,)
                new_paths.add(new_path)

        paths = new_paths

    return len(paths)


def run(s: str) -> int:
    rows = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char == "0":
                score = get_score(rows, r, c)
                total += score

    return total
