def run(s: str) -> int:
    blocks = [int(x) for x in s.strip().split("\t")]
    num_steps = 0
    state_to_num_steps = {tuple(blocks): 0}

    while True:
        run_step(blocks)
        num_steps += 1

        block_state = tuple(blocks)
        if block_state in state_to_num_steps:
            return num_steps - state_to_num_steps[block_state]

        state_to_num_steps[block_state] = num_steps


def run_step(blocks: list[int]) -> None:
    block_index, block = max(enumerate(blocks), key=lambda x: (x[1], -x[0]))

    blocks[block_index] = 0

    for i in range(block):
        place_block_index = (block_index + 1 + i) % len(blocks)
        blocks[place_block_index] += 1
