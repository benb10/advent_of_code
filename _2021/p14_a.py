def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    start = lines[0]
    rule_lines = lines[2:]

    pol = start.strip()

    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in rule_lines}

    for i in range(10):
        new_pol = ""

        for a, b in zip(pol, pol[1:]):
            new_pol += a
            new_pol += rules.get(a + b, "")

        new_pol += pol[-1]
        pol = new_pol

    from collections import Counter

    c = Counter(pol)
    most_common = max(c.items(), key=lambda t: t[1])
    least_common = min(c.items(), key=lambda t: t[1])

    return most_common[1] - least_common[1]
