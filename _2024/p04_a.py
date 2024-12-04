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

    for diff_r, diff_c in unit_vectors:
        chars = []
        for m in range(0, WORD_LENGTH):
            new_r = r + diff_r * m
            new_c = c + diff_c * m
            char = get_char(new_r, new_c, rows)
            if char is None:
                break
            chars.append(char)

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


def run(s: str) -> int:
    rows = [line.strip() for line in s.strip().split("\n")]
    num_matches = 0

    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            potential_words = get_potential_words(r, c, rows)
            matches = [w for w in potential_words if w == WORD]
            num_matches += len(matches)

    return num_matches
