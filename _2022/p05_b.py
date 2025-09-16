def run(s: str) -> str:
    lines = [line for line in s.split("\n")]

    empty_line_index = next(i for i, line in enumerate(lines) if line == "")
    stacks_lines = lines[: empty_line_index - 1]
    instruction_lines = lines[empty_line_index + 1 :]

    stacks: list[list[str]] = []

    for line in stacks_lines[::-1]:
        stack_index = 0
        while True:
            i = 4 * stack_index + 1
            if i >= len(line):
                break

            while len(stacks) <= stack_index:
                stacks.append([])

            char = line[i]
            if char != " ":
                stacks[stack_index].append(char)

            stack_index += 1

    for line in instruction_lines:
        if not line:
            continue
        words = line.split(" ")
        _, num_crates_to_move, _, from_stack_num, _, to_stack_num = words
        num_crates_to_move = int(num_crates_to_move)
        from_stack_num = int(from_stack_num)
        from_stack_index = from_stack_num - 1
        to_stack_num = int(to_stack_num)
        to_stack_index = to_stack_num - 1

        crates_to_move = []
        for i in range(num_crates_to_move):
            crates_to_move.append(stacks[from_stack_index].pop())

        stacks[to_stack_index] += crates_to_move[::-1]

    output = ""
    for stack in stacks:
        if stack:
            output += stack[-1]

    return output
