from collections import Counter, defaultdict


def is_valid(path):
    counter = Counter(path)
    if counter["start"] > 1:
        return False
    if counter["end"] > 1:
        return False
    small_caves = {x for x in path if x.islower() and x != "start" and x != "end"}
    if any(counter[x] > 2 for x in small_caves):
        return False
    duplicate_small_caves = [x for x in small_caves if counter[x] > 1]
    return len(duplicate_small_caves) <= 1


assert is_valid(["start", "b", "A", "b"]) is True
assert is_valid(["start", "b", "d", "b", "A", "c", "A", "b"]) is False


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
        for x in next_options:
            new_path = path + [x]
            if not is_valid(new_path):
                continue
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

    pp_paths(paths)

    return len(paths)
