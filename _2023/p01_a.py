def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        first_digit = next(c for c in line if c.isdigit())
        last_digit = next(c for c in reversed(line) if c.isdigit())
        num = int(first_digit + last_digit)
        total += num

    return total
