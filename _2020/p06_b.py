def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    groups: list[list[str]] = []
    last_line = ""

    for line in lines:
        if line:
            if last_line:
                # append to last group
                groups[-1].append(line)
            else:
                # make a new group
                groups.append([line])

        last_line = line

    total = 0

    for group in groups:
        everyone_yes_questions = set(group[0])
        for line in group[1:]:
            everyone_yes_questions &= set(line)

        total += len(everyone_yes_questions)

    return total
