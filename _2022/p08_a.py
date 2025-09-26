from typing import Iterable


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [[int(c) for c in line] for line in lines]

    visible_tree_coords = set()

    for line in iter_line_coords(nums):
        max_height = -1
        for r, c in line:
            height = nums[r][c]

            if height > max_height:
                visible_tree_coords.add((r, c))
                max_height = height

    return len(visible_tree_coords)


def iter_line_coords(nums: list[list[int]]) -> Iterable[Iterable[tuple[int, int]]]:
    num_rows = len(nums)
    num_columns = len(nums[0])

    for r in range(num_rows):
        yield ((r, c) for c in range(num_columns))
        yield ((r, c) for c in reversed(range(num_columns)))

    for c in range(num_columns):
        yield ((r, c) for r in range(num_rows))
        yield ((r, c) for r in reversed(range(num_rows)))
