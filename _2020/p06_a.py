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
        all_yes_questions = {x for line in group for x in line}
        total += len(all_yes_questions)

    return total
