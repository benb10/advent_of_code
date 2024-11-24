def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    start = lines[0]
    rule_lines = lines[2:]

    pol = start.strip()

    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in rule_lines}

    from collections import defaultdict

    pair_count = defaultdict(int)

    for a, b in zip(pol, pol[1:]):
        pair_count[a + b] += 1

    for i in range(40):
        new_pair_count = defaultdict(int)

        for pair, count in pair_count.items():
            if pair in rules:
                new_pair_count[pair[0] + rules[pair]] += count
                new_pair_count[rules[pair] + pair[1]] += count
            else:
                new_pair_count[pair] += count

        pair_count = new_pair_count

    char_count = defaultdict(int)

    for pair, count in pair_count.items():
        char_count[pair[0]] += count / 2
        char_count[pair[1]] += count / 2

    char_count[pol[0]] += 0.5
    char_count[pol[-1]] += 0.5

    most_common = max(char_count.items(), key=lambda t: t[1])
    least_common = min(char_count.items(), key=lambda t: t[1])

    return most_common[1] - least_common[1]
