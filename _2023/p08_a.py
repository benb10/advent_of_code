from itertools import cycle


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    directions, _, *mappings = lines

    node_mappings = {}
    for line in mappings:
        lhs, rhs = line.split(" = ")
        a, b = rhs.replace("(", "").replace(")", "").split(", ")
        node_mappings[lhs] = (a, b)

    node = "AAA"
    num_steps = 0

    for direction in cycle(directions):
        num_steps += 1
        i = {"L": 0, "R": 1}[direction]
        node = node_mappings[node][i]
        if node == "ZZZ":
            break

    return num_steps
