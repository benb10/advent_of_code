from collections import Counter


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    double_count = 0
    triple_count = 0

    for line in lines:
        counter = Counter(line)

        if any(v == 2 for v in counter.values()):
            double_count += 1
        if any(v == 3 for v in counter.values()):
            triple_count += 1

    return double_count * triple_count
