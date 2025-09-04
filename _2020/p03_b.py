def run(s: str) -> int:
    tree_map = [line.strip() for line in s.strip().split("\n")]

    map_width = len(tree_map[0])

    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    total = 1
    for dr, dc in slopes:
        coords = [(i * dr, i * dc % map_width) for i in range(len(tree_map) // dr)]
        num_trees = sum(1 for r, c in coords if tree_map[r][c] == "#")
        total *= num_trees

    return total
