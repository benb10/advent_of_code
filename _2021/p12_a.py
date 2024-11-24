from collections import defaultdict


def get_paths(s):
    edges = [x.strip().split("-") for x in s.strip().split("\n")]
    node_to_adj = defaultdict(set)

    for a, b in edges:
        node_to_adj[a].add(b)
        node_to_adj[b].add(a)

    node_to_adj = dict(node_to_adj)

    incomplete_paths = [["start"]]
    complete_paths = []

    while True:
        if not incomplete_paths:
            break

        path = incomplete_paths.pop(0)

        next_options = node_to_adj[path[-1]]
        next_options = [x for x in next_options if not (x.islower() and x in path)]
        for x in next_options:
            new_path = path + [x]
            if new_path[-1] == "end":
                complete_paths.append(new_path)
            else:
                incomplete_paths.append(new_path)

    return complete_paths


def pp_paths(paths):
    for x in sorted([",".join(path) for path in paths]):
        print(x)


def run(s: str) -> int:
    paths = get_paths(s)
    return len(paths)
