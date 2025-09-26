def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    accumulator = 0
    i = 0
    indices_visited = set()

    while True:
        if i in indices_visited:
            return accumulator

        indices_visited.add(i)
        operation, value_str = lines[i].split(" ")

        if operation == "nop":
            i += 1

        elif operation == "acc":
            accumulator += int(value_str)
            i += 1

        elif operation == "jmp":
            i += int(value_str)

        else:
            raise ValueError(f"Unknown operation: {operation}")
