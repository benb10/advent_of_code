from copy import deepcopy


def run(s: str) -> int | None:
    lines = [line.strip() for line in s.strip().split("\n")]

    program = []

    for line in lines:
        operation, value_str = line.split(" ")
        program.append((operation, int(value_str)))

    # run normally to get indices_visited
    _, _, init_indices_visited = run_program(program)

    for i in init_indices_visited:
        # see if we can change this line
        operation, value = program[i]
        if operation == "acc":
            continue

        new_operation = {"nop": "jmp", "jmp": "nop"}[operation]
        new_program = deepcopy(program)
        new_program[i] = (new_operation, value)

        completed, accumulator, _ = run_program(new_program)
        if completed:
            return accumulator

    return None


def run_program(program) -> tuple[bool, int, set[int]]:
    accumulator = 0
    i = 0
    indices_visited = set()

    while True:
        if i == len(program):
            return True, accumulator, indices_visited

        if i in indices_visited:
            return False, accumulator, indices_visited

        indices_visited.add(i)
        operation, value = program[i]

        if operation == "nop":
            i += 1

        elif operation == "acc":
            accumulator += value
            i += 1

        elif operation == "jmp":
            i += value

        else:
            raise ValueError(f"Unknown operation: {operation}")
