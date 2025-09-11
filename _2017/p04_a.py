def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    num_valid = 0

    for line in lines:
        words = line.split(" ")

        seen = set()
        has_duplicate = False

        for word in words:
            if word in seen:
                has_duplicate = True
                break
            seen.add(word)

        if not has_duplicate:
            num_valid += 1

    return num_valid
