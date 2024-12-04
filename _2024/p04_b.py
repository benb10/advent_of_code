WORD = "XMAS"
WORD_LENGTH = len(WORD)


def get_potential_words(r: int, c: int, rows: list[str]) -> list[str]:
    unit_vectors = [
        (0, 1),  # right
        (1, 1),  # down right
        (1, 0),  # down
        (1, -1),  # down left
        (0, -1),  # left
        (-1, -1),  # up left
        (-1, 0),  # up
        (-1, 1),  # up right
    ]
    potential_words = []
    num_rows = len(rows)
    num_columns = len(rows[0])

    for diff_r, diff_c in unit_vectors:
        chars = []
        for m in range(0, WORD_LENGTH):
            new_r = r + diff_r * m
            new_c = c + diff_c * m
            if not (0 <= new_r < num_rows):
                break
            if not (0 <= new_c < num_columns):
                break
            chars.append(rows[new_r][new_c])

        if len(chars) == WORD_LENGTH:
            word = "".join(chars)
            potential_words.append(word)

    return potential_words


def get_char(r: int, c: int, rows: list[str]) -> str | None:
    if r < 0 or c < 0:
        return None
    try:
        return rows[r][c]
    except IndexError:
        return None


def is_x_mas(r: int, c: int, rows: list[str]) -> bool:
    if rows[r][c] != "A":
        return False

    upward_diag_coords = [(r + 1, c - 1), (r, c), (r - 1, c + 1)]
    downward_diag_coords = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]

    for coords in [upward_diag_coords, downward_diag_coords]:
        chars = {get_char(new_r, new_c, rows) for new_r, new_c in coords}
        if chars != {"M", "A", "S"}:
            return False

    return True


def run(s: str) -> int:
    rows = [line.strip() for line in s.strip().split("\n")]
    num_matches = 0

    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if is_x_mas(r, c, rows):
                num_matches += 1

    return num_matches
