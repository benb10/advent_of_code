def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    num_valid = 0

    for line in lines:
        words = line.split(" ")
        sorted_words = ["".join(sorted(word)) for word in words]

        seen = set()
        has_duplicate = False

        for sorted_word in sorted_words:
            if sorted_word in seen:
                has_duplicate = True
                break
            seen.add(sorted_word)

        if not has_duplicate:
            num_valid += 1

    return num_valid
