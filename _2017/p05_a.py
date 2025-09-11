def run(s: str) -> int:
    offsets = [int(x) for x in s.strip().split("\n")]

    position = 0
    num_steps = 0

    while True:
        if not (0 <= position < len(offsets)):
            break

        distance_to_move = offsets[position]
        offsets[position] += 1
        position += distance_to_move
        num_steps += 1

    return num_steps
