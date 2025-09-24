from more_itertools import chunked

from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    output = run_intcode(nums)

    num_blocks = 0

    for x, y, tile_id in chunked(output.outputs, 3):
        if tile_id == 2:
            num_blocks += 1

    return num_blocks
