def run(s: str) -> int:
    blocks = [int(x) for x in s.strip().split("\t")]

    seen_states = {tuple(blocks)}

    while True:
        run_step(blocks)

        block_state = tuple(blocks)
        if block_state in seen_states:
            break
        seen_states.add(block_state)

    return len(seen_states)


def run_step(blocks: list[int]) -> None:
    block_index, block = max(enumerate(blocks), key=lambda x: (x[1], -x[0]))

    blocks[block_index] = 0

    for i in range(block):
        place_block_index = (block_index + 1 + i) % len(blocks)
        blocks[place_block_index] += 1
