def run(s: str) -> int:
    tree_map = [line.strip() for line in s.strip().split("\n")]

    map_width = len(tree_map[0])
    coords = [(i, 3 * i % map_width) for i in range(len(tree_map))]
    num_trees = sum(1 for r, c in coords if tree_map[r][c] == "#")

    return num_trees
