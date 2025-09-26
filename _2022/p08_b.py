from math import prod
from typing import Iterable


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [[int(c) for c in line] for line in lines]
    num_rows = len(nums)
    num_columns = len(nums[0])

    max_scenic_score = 0

    for r in range(num_rows):
        for c in range(num_columns):
            scenic_score = get_scenic_score(r, c, nums)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def get_scenic_score(r: int, c: int, nums: list[list[int]]) -> int:
    tree_height = nums[r][c]

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]
    visible_tree_counts = []

    for diff_r, diff_c in directions:
        num_trees_visible = 0
        for other_tree_height in iter_tree_heights(
            r=r,
            c=c,
            diff_r=diff_r,
            diff_c=diff_c,
            nums=nums,
        ):
            num_trees_visible += 1
            if other_tree_height >= tree_height:
                break

        visible_tree_counts.append(num_trees_visible)

    return prod(visible_tree_counts)


def iter_tree_heights(r: int, c: int, diff_r: int, diff_c: int, nums: list[list[int]]) -> Iterable[int]:
    num_rows = len(nums)
    num_columns = len(nums[0])

    current_r = r
    current_c = c

    while True:
        current_r += diff_r
        current_c += diff_c
        if not (0 <= current_r < num_rows):
            break
        if not (0 <= current_c < num_columns):
            break

        yield nums[current_r][current_c]
