def run(s: str) -> int:
    offsets = [int(x) for x in s.strip().split("\n")]

    position = 0
    num_steps = 0

    while True:
        if not (0 <= position < len(offsets)):
            break

        offset = offsets[position]
        distance_to_move = offset
        offset_diff = -1 if offset >= 3 else 1
        offsets[position] += offset_diff
        position += distance_to_move
        num_steps += 1

    return num_steps
