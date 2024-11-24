def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    groups = []
    last_line = None
    for line in lines:
        if line:
            if last_line:
                groups[-1].append(int(line))
            else:
                groups.append([int(line)])
        last_line = line
    sums = [sum(group) for group in groups]
    return max(sums)
