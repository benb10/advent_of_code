from itertools import combinations


def run(s: str) -> str | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    for line_1, line_2 in combinations(lines, 2):
        similar_chars = [a for a, b in zip(line_1, line_2) if a == b]
        is_solution = len(similar_chars) == len(line_1) - 1
        if is_solution:
            return "".join(similar_chars)

    return None
